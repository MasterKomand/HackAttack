#!/usr/bin/bash
pathFile="HackAttack" 
pkg install python
cd ~/../usr/bin 
# команда
touch HackAttack
echo "cd ~/$pathFile/ && python HackAttack.py" >  HackAttack
chmod +x HackAttack
cd ~/
#конец