import requests
import json
import base64










gameNameList= "item_sold_minecraft", "prepaid_card_redeemed_minecraft", "item_sold_cobalt", "prepaid_card_redeemed_cobalt", "item_sold_scrolls", "item_sold_dungeons"

class userInfo:
    def __init__(self, uuid):
        self.uuid = uuid    




    @staticmethod
    async def getUUID(username: str) -> str:
        
        resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        
        if not resp.ok:
            return None
        
        try:
            return resp.json()["id"]
        
        except json.JSONDecodeError:
            return None
           
    async def getProfile(self) -> dict:
        
            
        resp = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{self.uuid}")

        
        if not resp.ok:
            return None
        
        try:
          try:
            
            key = resp.json()
            value = key["properties"][0]["value"]
            
            unJsondata = base64.b64decode(value).decode('ascii')
            
           
            data = json.loads(unJsondata)
            
            return data

          except KeyError:
              return None
        except json.JSONDecodeError:
            return None
    
    @staticmethod
    async def getUUIDs(*usernames: str) -> dict:
        count = 1
        data1 = []
        resultList = []
        if 10 < len(usernames) and not 20 < len(usernames):
            count += int(len(usernames) / 10)
        
        if 20 < len(usernames):
            return None

       

        for i in range(0, count):
         
          for x in range(0, 10):
             try: 
              
              if i == 1:
                  
                  if x == 0:
                    data1.clear()
                  data1.append(usernames[10 + x])

              else:
                data1.append(usernames[x])
             
             except:
                 break
         
         
          print(data1)
          resp = requests.post(url = "https://api.mojang.com/profiles/minecraft", json = data1, headers={"Content-Type": "application/json"})
          if not resp.ok:
                return None
          resultList.append(resp.json())     


      
        if len(resultList) == 1:
             return resultList[0]
        
        elif len(resultList) == 2:
            return resultList[0], resultList[1]

    async def getName(self) -> str:
        
        resp = requests.get(f"https://api.mojang.com/user/profile/{self.uuid}")
        
        
        if not resp.ok:
            return None
        
        try:
            return resp.json()["name"]
        
        except json.JSONDecodeError:
            return None

    async def getNameHistory(self) -> dict:
        resp = requests.get(f"https://api.mojang.com/user/profile/{self.uuid}/names")
        
        
        if not resp.ok:
            return None
        
        try:
            return resp.json()
        
        except json.JSONDecodeError:
            return None


    @staticmethod
    async def checkName(token: str , username: str) -> str: 
        resp = requests.get(f"https://api.minecraftservices.com/minecraft/profile/name/{username}/available", headers={"Authorization" : f"Bearer {token}"})
        if not resp.ok:
            return None
        
        return resp.json()["status"]


    @staticmethod
    async def saleStatistics(gameName = gameNameList) -> dict:
           
        if gameName not in gameNameList:         
            return None
        
        resp = requests.post(f"https://api.mojang.com/orders/statistics", data = json.dumps({"metricKeys" : [str(gameName)]}), headers={"Accept": "application/json", "Content-Type": "application/json"})
        if not resp.ok:           
            return None
        return resp.json()

    @staticmethod
    async def nameChangeEligibility(token) -> bool:
        resp = requests.post(url = "https://api.minecraftservices.com/minecraft/profile/namechange", headers={"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()["nameChangeAllowed"]

  
