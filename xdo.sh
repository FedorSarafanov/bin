#!/bin/bash


height=`xdpyinfo | grep dimension | egrep -o "[0-9]{3} p" | egrep -o "[0-9]{3}"`
width=`xdpyinfo | grep dimension | egrep -o "[0-9]{4}x" | egrep -o "[0-9]{4}"`

eval $(xdotool getmouselocation --shell)
# scrot '/home/lab/bin/screen.png' 
# python '/home/lab/bin/search-image.py'
# xdotool mousemove 989 881 click 1 mousemove $X $Y
d=$[height-26]
c=$[width-210]
# c=$[width-329]
xdotool mousemove $c $d click 1 mousemove $X $Y

# 376 26
# echo $X $Y

# 210 160 sleep 0.1 click 1 sleep 0.1 key Return sleep 0.1 key Return


# Новая но плохая версия

# if [ `wmctrl -l | grep -c VK` -eq 0 ]
# then
# # 	# echo "Empty string"
# # 	# zenity --warning --text "Хватит страдать хернёй"

# vk-messenger

# # 	# else
# # 	 # wmctrl -F -c "VK Messenger"
# else

# # wmctrl -s 1; wmctrl -r "VK Messenger" -t 0; wmctrl -s 0

# 	wmctrl -l | grep VK | tail | while read _ID _D _O _F _G; do 
# 		 if [ $_D -eq 0 ]
# 		 then
# 		 	wmctrl -r "VK Messenger" -t 2;
# 		 fi
# 		 if [ $_D -eq 2 ]
# 		 then
# 		 	# wmctrl -r "VK Messenger" -t 1;
# 		 	wmctrl -s 2; wmctrl -r "VK Messenger" -t 0; wmctrl -s 0;
# 		 	wmctrl -a "VK Messenger";
# 		 fi	 
# 	done
# fi