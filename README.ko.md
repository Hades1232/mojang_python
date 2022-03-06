# Mojang_python
아마도 간단한(?) 파이썬 모장 [API](https://mojang-api-docs.netlify.app/index.html) 래퍼.</br>

현재 작업중인 Hypixel Api Wrapper UUID만 호환되게 하려고 만들었는데 Api Docs를 보니 재밌길래 만들어봤습니다. 




## 설치 방법

```
git clone https://github.com/Hades1232/mojang_python.git 
```


## 사용 방법



<details>
<summary>지원하는 모든 Api 사용 방법 보기</summary>
<p>      info.py :
    
    
``` py
    from mojang_python import Mojang    
    userInfo = Mojang.userInfo
    
    # Function Type : staticmethod
    # Return Value : Minecraft User UUID 
    # Return Type : str
    
    uuid = userInfo.getUUID(username)
    ----------------------------------
    
    # Class 
    
    class1 = userInfo(uuid)     
    ----------------------------------
    
    # Return Value : User's Minecraft Profile 
    # Return Type : dict
    
    class1.getProfile(self) 
    ----------------------------------
    
    # Return Value : User's Minecraft Nickname
    # Return Type : str
    
    class1.getName(self) 
    ----------------------------------
    
    # Return Value : User's Name History
    # Return Type : dict
    
    class1.getNameHistory(self) 
    ----------------------------------
    
    # Function Type : staticmethod
    # Return Value : Users' UUIDs
    # Return Type : dict
    
    # Api에서 최대로 받을 수 있는 유저 수는 10명, 
    # 그러나 변수 2개로 받으면 최대 20명까지 가능함.
    
    # Example : a = userInfo.getUUIDs(name1, name2, name3, ···, name10) 
    # a, b = userInfo.getUUIDs(name1, name2, name3, ···, name20)
    
    userInfo.getUUIDs(*args) 
    ----------------------------------
    
    # Function Type : staticmethod
    # Return Value : Games sales statistics
    # Retunrn Type : dict
    # gameName = "item_sold_minecraft", "prepaid_card_redeemed_minecraft", "item_sold_cobalt", "prepaid_card_redeemed_cobalt", "item_sold_scrolls", "item_sold_dungeons"
    # 여러개도 가능하나 하나만 되게 만듦. (귀찮아서 그런건 아니고 ㅎㅎ)
    
    userInfo.saleStatistics(gameName) 
    
    
```
<h4>나머지는 나중에 할 예정.</h4>
</p>
</details>



## 라이센스




