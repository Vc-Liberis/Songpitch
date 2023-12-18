# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory
WORKDIR /app

## Copy the current directory contents into the container at /app
COPY requirements.txt .

# Copy the project files to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install additional packages using apt-get
RUN apt-get update && \
    apt-get install -y \
        wget \
        libgconf-2-4 \
        libx11-6 \
        libx11-xcb1 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxext6 \
        libxi6 \
        libxtst6 \
        libxrandr2 \
        libxss1 \
        libxxf86vm1 \
        lsb-release \
        libatk-bridge2.0-0 \
        libgtk-3-0 \
        fonts-ipaexfont \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies and download Google Chrome
RUN apt-get update && \
    apt-get install -y wget fonts-liberation libasound2 libdrm2 libgbm1 libnspr4 libnss3 libu2f-udev libvulkan1 xdg-utils && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get -y install -f

# Set the Chrome binary path as an environment variable
ENV CHROME_BIN=/usr/bin/google-chrome

# Set PYTHONUNBUFFERED environment variable
ENV PYTHONUNBUFFERED=1

# CMD to run tests when the container launches
CMD ["pytest", "tests/test_artistscrapper.py"]