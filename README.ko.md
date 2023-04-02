# Mojang_python
아마도 쉬운 파이썬 모장 [API](https://mojang-api-docs.netlify.app/index.html) 래퍼.</br>


## 설치 방법

```
git clone https://github.com/Hades1232/mojang_python.git
pip install mojang_python
```


## Example


```py

# 모듈 임포트하기

from mojang_python.src.mojang import UserInfo
from mojang_python.src.optifine import Cape

async def example():
   
   # 유저네임으로 UUID 구하기   
   uuid = await UserInfo.get_uuid("Dangk_")
   print(f"UUID : {uuid}")

   
   # 프로필 구하기 
   class_name = UserInfo(uuid)
   profile = await class_name.get_account_profile() 
   print(f'Profile URL : {profile["textures"]["SKIN"]["url"]}')
   
   
   # 망토 구하기 (get_account_profile과 함께)
   optifine_cape = await Cape.get_optifine_cape("Dangk_")
   
   if "CAPE" in profile["textures"]:
      cape = profile["textures"]["CAPE"]["url"]
      if optifine_cape != None:
         print(f"Cape URL : {cape} (Minecraft) / Cape URL : {optifine_cape} (Optifine)\n")
      else:
           print(f"Cape URL : {cape} (Minecraft)\n")

   elif optifineCape != None:
      print(f"Cape URL : {optifine_cape} (Optifine) \n")

   else:
     print("Cape URL : None\n")


# 코루틴으로 실행하기
from mojang_python.src.coroutine import runner

runner.run(example())

```

더 많은 정보는, [여기](https://github.com/Hades1232/mojang_python/blob/master/example.py)

    

