# Mojang_python

개발자를 위한 함수 정리표


## Return Information



<details>
<summary>함수 정보</summary>
<p>      info.py :
    
    
``` py
    from mojang_python.src.Mojang import userInfo
    
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
    # 여러개도 가능하나 하나만 되게 만듦. (나중에 지원할 예정)
    
    userInfo.saleStatistics(gameName) 
    
    
```
<h4>나머지는 나중에 할 예정.</h4>
</p>
</details>






