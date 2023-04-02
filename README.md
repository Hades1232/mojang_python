# Mojang_python
Maybe Easy Mojang [API](https://mojang-api-docs.netlify.app/index.html) Python Wrapper.</br>


(Korean is [here](https://github.com/Hades1232/mojang_python/blob/master/README.ko.md))

## How to install

```
git clone https://github.com/Hades1232/mojang_python.git
pip install mojang_python 
```


## Example

```py
# import class in module

from mojang_python.info import UserInfo
from mojang_python.optifine import Cape

async def example():
   
   # Get uuid from username
   uuid = await UserInfo.get_uuid("Dangk_")
   print(f"UUID : {uuid}")

   
   # Get Profile
   class_name = UserInfo(uuid)
   profile = await class_name.get_account_profile()
   print(f'Profile URL : {profile["textures"]["SKIN"]["url"]}')


   
   # Get Cape (with get_account_profile)
   optifine_cape = await Cape.get_optifine_cape("Dangk_")
   

   if "CAPE" in profile["textures"]:
      cape = profile["textures"]["CAPE"]["url"]
      if optifine_cape != None:
         print(f"Cape URL : {cape} (Minecraft) / Cape URL : {optifine_cape} (Optifine)\n")
      else:
           print(f"Cape URL : {cape} (Minecraft)\n")

   elif optifine_cape != None:
      print(f"Cape URL : {optifine_cape} (Optifine) \n")

   else:
     print("Cape URL : None\n")


# Run with coroutine
import asyncio

asyncio.run(example())


```

if you want more information, check [this](https://github.com/Hades1232/mojang_python/blob/master/example.py)

## Result 

![image](https://user-images.githubusercontent.com/80930383/157031084-450b1f0a-9232-4200-bdd3-1f3ceb42c711.png)





