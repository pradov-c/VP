#!/bin/bash
echo "Executing dependencies"
echo "starting"
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential -y -q
sudo pip install django
sudo pip install fabric
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv

