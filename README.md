# Mojang_python
Maybe Easy Mojang [API](https://mojang-api-docs.netlify.app/index.html) Python Wrapper.</br>

I made it compatible with only the Hypixel Api Wrapper UUID I'm working on, but when I saw Api Docs, I made it because it was fun.

korean is [here](https://github.com/Hades1232/mojang_python/blob/master/README.ko.md)

## How to install

```
git clone https://github.com/Hades1232/mojang_python.git 
```


## Example

```py
# import class in module

from mojang_python.src.Mojang import userInfo
from mojang_python.src.Optifine import Cape

# Get uuid from username
uuid = userInfo.getUUID("Dangk_")
print(f"UUID : {uuid}")

# Get Profile

className = userInfo(uuid)
profile = className.getProfile() # dict
print(f'Profile URL : {avatar["textures"]["SKIN"]["url"]}')


# Get Cape (with getProfile)

optifineCape = Cape.optifineCapeChecker("Dangk_")
profile = className.getProfile()

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

```



    
## Licence

Copyright © 2022 [Hades](https://github.com/Hades1232).
This project is Apache License 2.0 licensed.




