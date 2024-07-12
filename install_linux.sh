#!/bin/bash

# Display to user that he gonna install getoutliers

echo "Installing getoutliers..."


#Check if git is in the user's machine
if ! dpkg -s git &> /dev/null; then
    echo "git is not in your machine, Installing git..."
    sudo apt update
    sudo apt install git
else
    echo "Git is already in your machine"
    #Clone the getoutliers repository to install it in the user's machine
    git clone https://github.com/BidjorySamuel/getoutliers.git
    pip install -r requirements.txt
    pip install e .
fi

