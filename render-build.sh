#!/bin/bash

# Install Chrome and dependencies
apt-get update && apt-get install -y wget curl unzip
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
apt-get update && apt-get install -y google-chrome-stable

# Install Chromium Driver
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -N https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip -P /tmp/
unzip /tmp/chromedriver_linux64.zip -d /tmp/
mv /tmp/chromedriver /usr/local/bin/
chmod +x /usr/local/bin/chromedriver

echo "Chrome and Chromedriver installed successfully"

# Install Python dependencies
pip install -r requirements.txt

# Install Chrome Driver
echo "Installing ChromeDriver..."
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -q -O /usr/local/bin/chromedriver "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
unzip /usr/local/bin/chromedriver -d /usr/local/bin/
chmod +x /usr/local/bin/chromedriver

echo "Chrome and ChromeDriver installed successfully!"

#!/bin/bash
set -o errexit

echo "Installing dependencies..."
apt-get update && apt-get install -y wget unzip

apt-get update && apt-get install -y chromium
pip install -r requirements.txt

echo "Installing Google Chrome..."
wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i /tmp/chrome.deb || apt-get -fy install

echo "Installing ChromeDriver..."
wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip /tmp/chromedriver.zip -d /usr/local/bin/

echo "Installation complete."

