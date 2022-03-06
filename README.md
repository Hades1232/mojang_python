# Mojang_python
Maybe Easy Mojang [API](https://mojang-api-docs.netlify.app/index.html) Python Wrapper.</br>

I made it compatible with only the Hypixel Api Wrapper UUID I'm working on, but when I saw Api Docs, I made it because it was fun.



## How to install

```
git clone https://github.com/Hades1232/mojang_python.git 
```


## Return Inform



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
    
    # The maximum number of users you can get from Api is 10,
    # However, two variables can receive up to 20 people
    
    # Example : a = userInfo.getUUIDs(name1, name2, name3, ···, name10) 
    # a, b = userInfo.getUUIDs(name1, name2, name3, ···, name20)
    
    userInfo.getUUIDs(*args) 
    ----------------------------------
    
    # Function Type : staticmethod
    # Return Value : Games sales statistics
    # Retunrn Type : dict
    # gameName = "item_sold_minecraft", "prepaid_card_redeemed_minecraft", "item_sold_cobalt", "prepaid_card_redeemed_cobalt", "item_sold_scrolls", "item_sold_dungeons"
    # Many are possible, but I made only one possible (to be added later)
    
    userInfo.saleStatistics(gameName) 
    
    
```
<h4>the rest will be done later</h4>
</p>
</details>



## Licence

Copyright © 2022 [Hades](https://github.com/Hades1232).
This project is Apache License 2.0 licensed.




