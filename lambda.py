import subprocess
import os


def lambda_handler(event, context):
    try:
        # Change directory to where your pytest script is located
        print("lambda_handler")
        # print(os.path.abspath())
        #
        # # Run pytest
        test_file_path = os.path.join(os.getcwd(), 'tests', 'test_artistscrapper.py')
        print("test file path ",test_file_path)
        result = subprocess.run(["pytest", test_file_path], capture_output=True)
        #
        # # Print the pytest result
        print(result.stdout.decode('utf-8'))

        # Return the result
        return {
            'statusCode': 200
            #'body': result.stdout.decode('utf-8')
        }
    except Exception as e:
        # Log any exceptions
        print(f"Exception: {str(e)}")
        raise
