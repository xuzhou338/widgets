if [ "$#" -ne 1 ]
then 
	read -p "Which destination? " dest
	if [ $dest = '']
	then
	echo "Destination not found..."
	fi
else
	dest=$1
	
	if [ $dest = 'bash' ]
	then
		cd ~/bash
	elif [ $dest = "WSDoc" ]
	then
		cd ~/Library/WebServer/Documents
	elif [ $dest = "DS" ]
	then
		cd ~/Documents/DataScience
	elif [ $dest = "ds_tools" ]
	then
		cd ~/Documents/DataScience/ds_tools
	elif [ $dest = "ds_projects" ]
	then
		cd ~/Documents/DataScience/ds_projects
	elif [ $dest = "widgets" ]
	then
		cd ~/Documents/DataScience/widgets
	elif [ $dest = "kaggle" ]
	then
		cd ~/Documents/DataScience/kaggle
	elif [ $dest = "chapeau" ]
	then
		cd ~/Documents/chapeau
	else
		echo "Destination not found..."
	fi
fi


