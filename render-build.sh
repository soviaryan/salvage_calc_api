#!/bin/bash
set -o errexit  # Exit on error

echo "Updating system..."
apt-get update && apt-get install -y wget unzip curl

echo "Downloading and installing Google Chrome..."
wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i /tmp/chrome.deb || apt-get -fy install

# Verify Chrome installation
if ! command -v google-chrome-stable &> /dev/null
then
    echo "Chrome installation failed!"
    exit 1
fi

# Set Chrome binary path
ln -sf /usr/bin/google-chrome-stable /usr/bin/google-chrome
export CHROME_BIN="/usr/bin/google-chrome"

echo "Downloading ChromeDriver..."
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -q -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
unzip -o /tmp/chromedriver.zip -d /usr/local/bin/
chmod +x /usr/local/bin/chromedriver

# Ensure Chromedriver is in the right path
ln -sf /usr/local/bin/chromedriver /usr/bin/chromedriver
export CHROMEDRIVER_BIN="/usr/bin/chromedriver"

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Verifying installation..."
google-chrome --version || echo "Chrome install failed"
chromedriver --version || echo "ChromeDriver install failed"

echo "Setup complete."







