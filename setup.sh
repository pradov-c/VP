#!/bin/bash
echo "Executing dependencies"
echo "starting"
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential -y -q
sudo pip virtualenv
sudo pip install django
sudo pip install djangorestframework
sudo pip install whitenoise
sudo pip install fabric


