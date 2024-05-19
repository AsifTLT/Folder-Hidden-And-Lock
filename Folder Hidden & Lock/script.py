import os

print("\n")

hide_options = input("You Want to hide a folders and files (y/n)? or hit enter to show options!! : ")

if(hide_options is ""):
  show_options = input("you want to  show folders and files (y/n)? : ")
    
  if(show_options is "y"):
    os.system("attrib -h /s /d")
    print("your folders and files are visible ")
  elif(show_options is "n"):
    print("ok bye bye ")
    
if(hide_options is "y"):
  os.system("attrib +h /s /d")
  print("Your folders and files are hidden!!")
elif(hide_options is "n"):
  print("ok bye bye")   
       
        
    
    