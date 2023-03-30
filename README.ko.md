# Mojang_python
아마도 쉬운 파이썬 모장 [API](https://mojang-api-docs.netlify.app/index.html) 래퍼.</br>






## 설치 방법

```
pip install mojang-python
```


## Example


```py
async def example():
   
   # 유저네임으로 UUID 구하기   
   uuid = await userInfo.getUUID("Dangk_")
   print(f"UUID : {uuid}")

   
   # 프로필 구하기 (dict)
   className = userInfo(uuid)
   profile = await className.getProfile() # dict
   print(f'Profile URL : {profile["textures"]["SKIN"]["url"]}')
   
   
   # 망토 구하기 (getProfile과 함께)
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


# 코루틴으로 실행하기
from mojang_python.src.Coroutines import runner

runner.run(example())


```


    

