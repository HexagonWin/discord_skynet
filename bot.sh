#! /bin/bash

###############################
## Settings for SKYnet v.1-0a##
##  Set version              ##
version="3.0-a+20210301.dev"
## Thank you for using SKYn  ##

echo "Welcome to SKYnet V. ${version}"
./splash_load.sh
./time.sh
echo "Loading status settings"
sleep 2
./status.sh
