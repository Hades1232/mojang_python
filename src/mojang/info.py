import requests
import json
import base64


class UserInfo:
    def __init__(self, uuid: str):
        self.uuid = uuid    


    @staticmethod
    async def get_uuid(user_name: str) -> str | None:
        
        resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{user_name}")
        
        if not resp.ok:
            return None
        
        try:
            return resp.json()["id"]
        
        except json.JSONDecodeError:
            return None
           
    async def get_account_profile(self) -> dict | None:
        
        resp = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{self.uuid}")

        if not resp.ok:
            return None
        
        try:
            
            try:
            
                key = resp.json()
                value = key["properties"][0]["value"]
            
                decoded_json_data = base64.b64decode(value).decode('ascii')
            
           
                data = json.loads(decoded_json_data)
            
                return data
            except KeyError:
                return None
        
        except json.JSONDecodeError:
            return None
    
    @staticmethod
    async def get_uuids(user_names: list) -> dict | None:
        resp = requests.post(url = "https://api.mojang.com/profiles/minecraft", json = user_names, headers={"Content-Type": "application/json"})
        if not resp.ok:
            return None
          
    async def get_account_name(self) -> str | None:
        
        resp = requests.get(f"https://api.mojang.com/user/profile/{self.uuid}")
        
        
        if not resp.ok:
            return None
        
        try:
            return resp.json()["name"]
        
        except json.JSONDecodeError:
            return None


    @staticmethod
    async def check_name_availability(token: str , user_name: str) -> str | None: 
        
        resp = requests.get(f"https://api.minecraftservices.com/minecraft/profile/name/{user_name}/available", headers={"Authorization" : f"Bearer {token}"})
        
        if not resp.ok:
            return None
        
        return resp.json()["status"]


    @staticmethod
    async def check_name_change_eligibility(token: str) -> bool | None:
        resp = requests.get(url = "https://api.minecraftservices.com/minecraft/profile/namechange", headers={"Authorization": f"Bearer {token}"})
        
        if not resp.ok:
            return None
        
        return resp.json()["nameChangeAllowed"]

    @staticmethod
    async def get_blocked_server() -> dict:
        resp = requests.get("https://sessionserver.mojang.com/blockedservers")
        return resp.text

    