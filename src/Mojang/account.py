import requests
import json

class userSetting:
    

    @staticmethod
    async def checkMigration(token: str) -> bool:
        resp = requests.get(f"https://api.minecraftservices.com/rollout/v1/msamigration", headers={"Authorization" : f"Bearer {token}"})
        if not resp.ok:
            return None
        
        return resp.json()["rollout"]
    
    @staticmethod
    async def getToken(email : str, password : str) -> str:

        json2 = {
            "agent" : {
                #"minecraft"
                "name" : "Minecraft", #// identifying which game is connecting, "Scrolls" returns Scrolls profile info
                #"#version" : 1 #// version of the agent (OPTIONAL)
            }, #// you don't even need this! "agent" : "minecraft" works fine too.
            "username" : str(email), #// username (legacy) or email address
            "password" : str(password), #// password
            #"clientToken" : "Mojang-API-Client", #// client token used to identify yourself (OPTIONAL)
            #"requestUser" : "true" #// request a response back containing user information (OPTIONAL)
        }
        resp = requests.post("https://authserver.mojang.com/authenticate", headers= {"Content-Type" : "application/json"}, data=json.dumps(json2))
        if not resp.ok:
            return None
    
        return resp.json()["accessToken"]

    @staticmethod
    async def redeemCode(token: str, giftcode: str) -> dict:
        resp = requests.put(url = f"https://api.minecraftservices.com/productvoucher/{giftcode}", headers={"Accept": "application/json", "Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()

    @staticmethod
    async def viewUserInformation(token) -> dict:
        resp = requests.post(url="https://api.mojang.com/user", headers={"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()
    
    @staticmethod
    async def viewMyProfile(token) -> dict:
        resp = requests.post(url = "https://api.minecraftservices.com/minecraft/profile", headers={"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()
    
    # 불안정 

    # @staticmethod
    # def changeMyName(token, username) -> bool:
    #   resp = requests.post(url = f"https://api.minecraftservices.com/minecraft/profile/name/{username}", headers= {"Authorization": f"Bearer {token}"})
    #   if not resp.ok:
    #       return False
    #   return True
    
    # #매우 불안정

    # @staticmethod
    # def changeMyProfile(token, profile : URL) -> bool:
    #     resp = requests.post("https://api.minecraftservices.com/minecraft/profile/skins", data = {"url" : profile, "variont" : "slim"}, headers=None)
    #     # pass
    #     return None
    
    #Not Working

    # @staticmethod
    # def resetMySkin(token):
    #     pass

    
    #didn't test
    
    # @staticmethod
    # def changeMyCape(token, capeID) -> bool: 
    #     resp = requests.post(url = "https://api.minecraftservices.com/minecraft/profile/capes/active", data = {"capeId" : capeID}, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
    #     if not resp.ok:
    #         return False
    #     return True
    
    # @staticmethod
    # def disableMyCape(token) -> bool:
    #     resp = requests.post(url = "https://api.minecraftservices.com/minecraft/profile/capes/active", headers= {"Authorization": f"Bearer {token}"})
    #     if not resp.ok:
    #         return False
    #     return True
