
from mojang_python.src.mojang import UserInfo
from mojang_python.src.mojang import UserSetting  
from mojang_python.src.optifine import Cape


async def example():
  
  name = "Dangk_" # Minecraft Nickname
  optifine_cape = await Cape.get_optifine_cape(name)
  token = await UserSetting.get_microsoft_token("email", "password") # Get token by migrated Microsoft Account 
  name_check = await UserInfo.check_name_availability(token, name) # Check if you can change your nickname to [name]
  
  if name_check == "DUPLICATE": # when someone is using this nickname
      uuid = await UserInfo.get_uuid(name) # Get [name]'s UUID 
      class_name = UserInfo(uuid) 
      avatar = await class_name.get_account_profile() # Get [name]'s profile 
      

      print(f"The account name {name} is already owned.\n")
      print("Profile information. : ")
      print(f"UUID : {uuid}")
      print(f'Profile URL : {avatar["textures"]["SKIN"]["url"]}') # Profile URL
      
      if "CAPE" in avatar["textures"]:
        cape = avatar["textures"]["CAPE"]["url"] # Cape URL
        if optifine_cape != None:
            print(f"Cape URL : {cape} (Minecraft) / Cape URL : {optifine_cape} (Optifine)\n")
        else:
              print(f"Cape URL : {cape} (Minecraft)\n")
      
      elif optifine_cape != None:
        print(f"Cape URL : {optifine_cape} (Optifine) \n")
      
      else:
          print("Cape URL : None\n")
      
      if "metadata" in avatar["textures"]["SKIN"]: # Model Arms (probably not used)
        model = avatar["textures"]["SKIN"]["metadata"]["model"]
        if model == "slim":
          model = "Alex (slim)"
        elif model == "classic": 
          model = "Steve (classic)"
        print(f'Model Arms : {model}')
      
      

  elif name_check == "NOT_ALLOWED":
      print("Not allowed Nickname.")
  
  else:
      check_name_change = await UserInfo.check_name_change_eligibility(token)   
      print(f"The account name {name} is a nickname that isn't currently own, and name change Eligibility is {check_name_change}.")
      


from mojang_python.src.coroutine import runner

runner.run(example()) 


