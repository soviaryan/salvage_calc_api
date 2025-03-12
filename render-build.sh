#!/bin/bash

# Install Chrome for Selenium
if ! command -v google-chrome-stable &> /dev/null
then
    echo "Installing Chrome..."
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
    sudo apt-get update
    sudo apt-get install -y google-chrome-stable
else
    echo "Chrome is already installed."
fi
