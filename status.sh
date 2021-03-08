#!/bin/bash

echo "40" | dialog --gauge "Set discord status - Bootstrap SKYnet" 10 70 0
sleep 2
status=$(whiptail --title "Set Status - SKYnet" --inputbox "Type in the Status you want" 10 30 3>&1 1>&2 2>&3)
echo "bstat = '$status'" > setstat.py
echo "Status set to $status"
echo "80" | dialog --gauge "Done setting status - Bootstrap SKYnet" 10 70 0
sleep 1
python3 main.py
