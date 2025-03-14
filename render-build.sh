#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "Updating package lists..."
apt-get update

echo "Installing required dependencies..."
apt-get install -y wget curl unzip gnupg software-properties-common

echo "Adding Google Chrome's signing key..."
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

echo "Adding Google Chrome repository..."
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list

echo "Installing Google Chrome..."
apt-get update && apt-get install -y google-chrome-stable

# Verify Chrome installation
if ! command -v google-chrome &> /dev/null
then
    echo "Chrome installation failed!"
    exit 1
fi

echo "Installing ChromeDriver..."
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -N https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip -P /tmp/
unzip /tmp/chromedriver_linux64.zip -d /tmp/
mv /tmp/chromedriver /usr/local/bin/
chmod +x /usr/local/bin/chromedriver

# Verify ChromeDriver installation
if ! command -v chromedriver &> /dev/null
then
    echo "ChromeDriver installation failed!"
    exit 1
fi

echo "Chrome and ChromeDriver installed successfully!"

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Build script execution completed."



