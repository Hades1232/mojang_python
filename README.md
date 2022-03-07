# Mojang_python
Maybe Easy Mojang [API](https://mojang-api-docs.netlify.app/index.html) Python Wrapper.</br>

I made it compatible with only the Hypixel Api Wrapper UUID I'm working on, but when I saw Api Docs, I made it because it was fun.

(Korean is [here](https://github.com/Hades1232/mojang_python/blob/master/README.ko.md))

## How to install

```
git clone https://github.com/Hades1232/mojang_python.git 
```


## Example

```py
# import class in module

from mojang_python.src.Mojang import userInfo
from mojang_python.src.Optifine import Cape

async def example():
   
   # Get uuid from username
   uuid = await userInfo.getUUID("Dangk_")
   print(f"UUID : {uuid}")

   
   # Get Profile
   className = userInfo(uuid)
   profile = await className.getProfile() # dict
   print(f'Profile URL : {profile["textures"]["SKIN"]["url"]}')


   
   # Get Cape (with getProfile)
   optifineCape = await Cape.optifineCapeChecker("Dangk_")
   profile = await className.getProfile()

   if "CAPE" in profile["textures"]:
      cape = profile["textures"]["CAPE"]["url"]
      if optifineCape != None:
         print(f"Cape URL : {cape} (Minecraft) / Cape URL : {optifineCape} (Optifine)\n")
      else:
           print(f"Cape URL : {cape} (Minecraft)\n")

   elif optifineCape != None:
      print(f"Cape URL : {optifineCape} (Optifine) \n")

   else:
     print("Cape URL : None\n")


# Run with coroutine
from mojang_python.src.Coroutines import runner

runner.run(example())


```

if you want more information, check [this](https://github.com/Hades1232/mojang_python/blob/master/example.py)

## Result 

![image](https://user-images.githubusercontent.com/80930383/157031084-450b1f0a-9232-4200-bdd3-1f3ceb42c711.png)


    
## Licence

Copyright © 2022 [Hades](https://github.com/Hades1232).
This project is Apache License 2.0 licensed.




