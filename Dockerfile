FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt
COPY .. ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --index-url=https://pypi.org/simple/


RUN yum -y install \
    wget \
    GConf2 \
    libX11 \
    libX11-xcb \
    libXcomposite \
    libXcursor \
    libXdamage \
    libXext \
    libXi \
    libXtst \
    libXrandr \
    libXScrnSaver \
    libXss \
    libXxf86vm \
    redhat-lsb \
    atk \
    gtk3 \
    ipa-gothic-fonts \
    xorg-x11-fonts-100dpi \
    xorg-x11-fonts-75dpi \
    xorg-x11-utils \
    xorg-x11-fonts-cyrillic \
    xorg-x11-fonts-Type1 \
    xorg-x11-fonts-misc \
    && yum clean all

# Install Google Chrome
#RUN wget https://dl.google.com/linux/chrome/rpm/stable/x86_64/google-chrome-stable-114.0.5735.90-1.x86_64.rpm && \
    #yum -y localinstall google-chrome-stable-114.0.5735.90-1.x86_64.rpm && \
    #rm google-chrome-stable-114.0.5735.90-1.x86_64.rpm

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
    yum -y localinstall google-chrome-stable_current_x86_64.rpm && \
    rm google-chrome-stable_current_x86_64.rpm

# Set the Chrome binary path as an environment variable
ENV CHROME_BIN=/usr/bin/google-chrome

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda.lambda_handler" ]