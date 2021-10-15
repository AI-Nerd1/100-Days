# !/usr/bin/env python3
logo = """                                                                                                                                                                                             
    ,---,                                                                                            
  .'  .' `\              ,---,                                        ,--,                           
,---.'     \           ,---.'|            ,--,                      ,--.'|         ,---,             
|   |  .`\  |          |   | :          ,'_ /|  ,----._,.  ,----._,.|  |,      ,-+-. /  |  ,----._,. 
:   : |  '  |   ,---.  :   : :     .--. |  | : /   /  ' / /   /  ' /`--'_     ,--.'|'   | /   /  ' / 
|   ' '  ;  :  /     \ :     |,-.,'_ /| :  . ||   :     ||   :     |,' ,'|   |   |  ,"' ||   :     | 
'   | ;  .  | /    /  ||   : '  ||  ' | |  . .|   | .\  .|   | .\  .'  | |   |   | /  | ||   | .\  . 
|   | :  |  '.    ' / ||   |  / :|  | ' |  | |.   ; ';  |.   ; ';  ||  | :   |   | |  | |.   ; ';  | 
'   : | /  ; '   ;   /|'   : |: |:  | : ;  ; |'   .   . |'   .   . |'  : |__ |   | |  |/ '   .   . | 
|   | '` ,/  '   |  / ||   | '/ :'  :  `--'   \`---`-'| | `---`-'| ||  | '.'||   | |--'   `---`-'| | 
;   :  .'    |   :    ||   :    |:  ,      .-./.'__/\_: | .'__/\_: |;  :    ;|   |/       .'__/\_: | 
|   ,.'       \   \  / /    \  /  `--`----'    |   :    : |   :    :|  ,   / '---'        |   :    : 
'---'          `----'  `-'----'                 \   \  /   \   \  /  ---`-'                \   \  /  
                                                 `--`-'     `--`-'                          `--`-'   
"""

print(logo)

def function():
    for x in range(1,20):
        if x == 18:
            print("You got it")
function()

from random import randint
dice_images = ['1','2','3','4','5','6']
dice_num = randint(0,5)
print(dice_images[dice_num])

year = int(input("Your year of birth: "))
if year > 1980 and year <= 1994:
  print("You are a milennial")
elif year >1994:
  print("You are a Gen Z")

age  = int(input("Your age: "))
if age > 18:
  print(f"You are elligible to drive at age {age}.")
else:
  print(f"You are not elligible to drive at age {age}.")

pages = int(input("Number of pages: "))
words_per_page = int(input("Number of words per page: "))
total = pages * words_per_page
print(total)
