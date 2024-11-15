#!/bin/bash

# Install Java 8 and Java 11
sudo apt install -y openjdk-8-jdk openjdk-11-jdk

# Install Git
sudo apt install -y git

# Install Sudo (if not already installed)
sudo apt install -y sudo

# Install Wget
sudo apt install -y wget

# Install Zip and Unzip
sudo apt install -y zip unzip

# Install Maven
sudo apt install -y maven

# Install Gradle
sudo apt install -y gradle

# Install Python 3.8 and pip
sudo apt install -y python3.8 python3-pip

# Install Virtualenv
sudo pip3 install virtualenv

# Install NodeJS v10.19
sudo apt install -y nodejs npm
sudo npm install -g n
sudo n 10.19.0

# Install Docker 20.10
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce=5:20.10.0~3-0~ubuntu-focal

# Set default Java version (optional, if both versions are installed)
sudo update-alternatives --config java
sudo update-alternatives --config javac

echo "Installation completed."

