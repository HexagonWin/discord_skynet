ttime=`date`
echo System booted in $ttime > bootime.txt
whiptail --title "SKYnet - Boot time" --infobox "SKYnet System started in $ttime" 8 78
echo "20" | dialog --gauge "Set time - Bootstrap SKYnet" 10 70 0
