#!/bin/bash
set -o errexit  # Exit on error

echo "Updating system..."
apt-get update && apt-get install -y wget curl unzip

echo "Installing Google Chrome..."
wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i /tmp/chrome.deb || apt-get -fy install

# Ensure Chrome binary is in the correct location
ln -sf /usr/bin/google-chrome-stable /usr/bin/google-chrome

echo "Verifying Chrome installation..."
google-chrome --version || echo "Chrome installation failed"

echo "Installing ChromeDriver..."
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -q -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
unzip -o /tmp/chromedriver.zip -d /usr/local/bin/
chmod +x /usr/local/bin/chromedriver

# Ensure Chromedriver binary is in the correct location
ln -sf /usr/local/bin/chromedriver /usr/bin/chromedriver

echo "Verifying ChromeDriver installation..."
chromedriver --version || echo "ChromeDriver installation failed"

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Setup complete."





