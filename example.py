from datetime import datetime
from mojang_python.src.Mojang import userInfo
from mojang_python.src.Mojang import userSetting  
from mojang_python.src.Optifine import Cape

import datetime

async def example():
  
  name = "Dangk_" # Minecraft Nickname
  optifineCape = await Cape.optifineCapeChecker(name)
  token = await userSetting.getToken("email", "pw") # Get token by Mojang Account (can only Mojang)
  nameCheck = await userInfo.checkName(token, name) # Check if you can change your nickname to [name]
  
  if nameCheck == "DUPLICATE": # when someone is using this nickname
      uuid = await userInfo.getUUID(name) # Get [name]'s UUID (the account who is the nickname that I want to change) 
      className = userInfo(uuid) 
      avatar = await className.getProfile() # Get [name]'s profile (dict)
      nameHistory = await className.getNameHistory() # Get [name]'s name history (dict)
      

      print(f"The account name {name} is already owned.\n")
      print("Profile information. : ")
      print(f"UUID : {uuid}")
      print(f'Profile URL : {avatar["textures"]["SKIN"]["url"]}') # Profile URL
      
      if "CAPE" in avatar["textures"]:
        cape = avatar["textures"]["CAPE"]["url"] # Cape URL
        if optifineCape != None:
            print(f"Cape URL : {cape} (Minecraft) / Cape URL : {optifineCape} (Optifine)\n")
        else:
              print(f"Cape URL : {cape} (Minecraft)\n")
      
      elif optifineCape != None:
        print(f"Cape URL : {optifineCape} (Optifine) \n")
      
      else:
          print("Cape URL : None\n")
      
      if "metadata" in avatar["textures"]["SKIN"]: # Model Arms (probably not used)
        model = avatar["textures"]["SKIN"]["metadata"]["model"]
        if model == "slim":
          model = "Alex (slim)"
        elif model == "classic": 
          model = "Steve (classic)"
        print(f'Model Arms : {model}')
      
      
      print("Account Name History Information : ")
      
      for i in range(len(nameHistory)):
          nameHistoryJson = nameHistory[i] 
          if i == 0:
              print(f"{i + 1}. : {nameHistoryJson['name']} (First Account Name)")
          else:
              unixDate = nameHistoryJson["changedToAt"]
              date = datetime.datetime.fromtimestamp(unixDate / 1000).strftime('%Y-%m-%d') # convert Unix epoch time format (in milliseconds) to Year-Month-Day
              print(f"{i + 1}. : {nameHistoryJson['name']}, Changed At : {date}")
      

  elif nameCheck == "NOT_ALLOWED":
      print("Not allowed Nickname.")
  
  else:
      
      checkNameChange = await userInfo.nameChangeEligibility(token)     
      print(f"The account name {name} is a nickname that isn't currently own, and name change Eligibility is {checkNameChange}.")
      


from mojang_python import main

main.run(example()) 


