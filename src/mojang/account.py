import requests
import json
from typing import Literal
import re
from urllib import parse

class UserSetting:

    @staticmethod
    async def check_migration(token: str) -> bool | None:
        resp = requests.get(f"https://api.minecraftservices.com/rollout/v1/msamigration", headers={"Authorization" : f"Bearer {token}"})
        if not resp.ok:
            return None
        
        return resp.json()["rollout"]
    
    @staticmethod
    async def get_microsoft_token(email: str, password: str) -> str:
        
        login_ready_url = "https://login.live.com/oauth20_authorize.srf?client_id=000000004C12AE6F&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=service::user.auth.xboxlive.com::MBI_SSL&display=touch&response_type=token&locale=en"
        xbox_live_url = "https://user.auth.xboxlive.com/user/authenticate"
        xsts_url = "https://xsts.auth.xboxlive.com/xsts/authorize"
        login_mc_url = "https://api.minecraftservices.com/authentication/login_with_xbox"


        session = requests.Session()
        login_ready_resp_text = session.get(url = login_ready_url, allow_redirects=True).text
        url_post = re.search("urlPost:'(.+?)'", login_ready_resp_text).group()[9:-1]
        sfttag =  re.search("sFTTag:'(.+?)'", login_ready_resp_text).group()[8:-1]
        sfttag_value = re.search('value="(.+?)"', sfttag).group()[7:-1]
    
        url_post_dict = {
            "login" : email,
            "loginfmt" : email,
            "passwd" : password,
            "PPFT" : sfttag_value
        }

        url_post_resp = session.post(url=url_post, data=url_post_dict, headers={"Content-Type" : "application/x-www-form-urlencoded"}, allow_redirects=True)
        

        if "#" not in url_post_resp.url:
            raise requests.HTTPError("401: Unauthorized (wrong email or password)")
        

        raw_login_data = url_post_resp.url.split("#")[1]
        login_data = dict(item.split("=") for item in raw_login_data.split("&")) 
        login_data["access_token"] = requests.utils.unquote(login_data["access_token"]) 
        login_data["refresh_token"] = requests.utils.unquote(login_data["refresh_token"]) 
        
        xbox_live_dict = {
            "Properties": {
                "AuthMethod": "RPS",
                "SiteName": "user.auth.xboxlive.com",
                "RpsTicket": login_data["access_token"] 
            },
            "RelyingParty": "http://auth.xboxlive.com",
            "TokenType": "JWT"
        }

        xbox_live_resp = session.post(url = xbox_live_url, json=xbox_live_dict, headers = {"Content-Type": "application/json", "Accept": "application/json"})
        
        if not xbox_live_resp.ok:
            raise requests.HTTPError(f"{xbox_live_resp.status_code}: {xbox_live_resp.reason}")

        xbox_live_token = xbox_live_resp.json()["Token"]
        xbox_live_uhs = xbox_live_resp.json()["DisplayClaims"]["xui"][0]["uhs"]

        xsts_dict = {
            "Properties": {
                "SandboxId": "RETAIL",
                "UserTokens": [
                    xbox_live_token
                ]
            },
            "RelyingParty": "rp://api.minecraftservices.com/",
            "TokenType": "JWT"
        }

        xsts_resp = session.post(url = xsts_url, json = xsts_dict, headers={"Content-Type": "application/json", "Accept": "application/json"})
        
        if not xsts_resp.ok:
            raise requests.HTTPError(f"{xsts_resp.status_code}: {xsts_resp.reason}")
        
        xsts_token = xsts_resp.json()["Token"]
        xsts_uhs = xsts_resp.json()["DisplayClaims"]["xui"][0]["uhs"]

        if xsts_uhs != xbox_live_uhs:
            raise Exception(f"Unexcepted Error: Hash {xsts_uhs} must equal Hash {xbox_live_uhs}")

        login_mc_dict = {
            "identityToken" : f"XBL3.0 x={xsts_uhs};{xsts_token}",
            "ensureLegacyEnabled" : True
        }
        
        login_mc_resp = session.post(url = login_mc_url, json = login_mc_dict, headers={"Content-Type" : "application/json"})

        if not login_mc_resp.ok:
            raise requests.HTTPError(f"{login_mc_resp.status_code}: {login_mc_resp.reason}")

        return login_mc_resp.json()["access_token"]


    @staticmethod
    async def get_monjang_token(email: str, password: str) -> str:

        json_value = {
            "agent" : {    
                "name" : "Minecraft",
            },
            "username" : str(email),
            "password" : str(password),
        }
        resp = requests.post("https://authserver.mojang.com/authenticate", headers= {"Content-Type" : "application/json"}, data=json.dumps(json_value))
        
        if not resp.ok:
            raise requests.HTTPError(f"{resp.status_code}: {resp.reason}")
    
        return resp.json()["accessToken"]

    @staticmethod
    async def redeem_code(token: str, gift_code: str) -> dict | None:
        resp = requests.put(url = f"https://api.minecraftservices.com/productvoucher/{gift_code}", headers={"Accept": "application/json", "Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()

    @staticmethod
    async def get_user_information(token: str) -> dict | None:
        resp = requests.get(url= "https://api.mojang.com/user", headers={"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()
    
    @staticmethod
    async def get_user_profile(token: str) -> dict | None:
        resp = requests.get(url = "https://api.minecraftservices.com/minecraft/profile", headers={"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()
   
    @staticmethod
    async def change_account_name(token: str, user_name: str) -> bool:
        resp = requests.put(url = f"https://api.minecraftservices.com/minecraft/profile/name/{user_name}", headers= {"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return False
        return True
    

    @staticmethod
    async def change_account_profile(token: str, profile_url: str, variont = Literal["alex", "steve"]) -> bool:
        variont_value_dict = {"alex" : "slim", "steve" : "classic"}

        resp = requests.post(
            url = "https://api.minecraftservices.com/minecraft/profile/skins", 
            data = {"url" : profile_url, "variont" : variont_value_dict[variont]},
            headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        )
        if not resp.ok:
            return False
        return True
    

    @staticmethod
    async def reset_account_skin(token: str) -> bool:
        resp = requests.delete(url = f"https://api.minecraftservices.com/minecraft/profile/skins/active", headers= {"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return False
        return True

    
    @staticmethod
    async def change_account_cape(token: str, cape_id: str) -> bool:
        # cape_id: get_user_profile()
        resp = requests.put(
            url = "https://api.minecraftservices.com/minecraft/profile/capes/active", 
            data = {"capeId" : cape_id}, 
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        )
        if not resp.ok:
            return False
        return True
    
    @staticmethod
    async def disable_account_cape(token: str) -> bool:
        resp = requests.delete(url = "https://api.minecraftservices.com/minecraft/profile/capes/active", headers= {"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return False
        return True

    @staticmethod
    async def change_account_password(token: str, old_password: str, new_password: str) -> bool:
        resp = requests.put(
            url = "https://api.mojang.com/users/password", 
            data = {"oldPassword" : old_password, "password" : new_password},
            headers= {"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        if not resp.ok:
            return False
        return True

    @staticmethod
    async def get_credit_card_info(token: str) -> list | None:
        resp = requests.get(url = "https://api.mojang.com/creditcards", headers= {"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()

    @staticmethod
    async def get_owned_game(token: str) -> dict | None:
        resp = requests.get(url = "https://api.minecraftservices.com/entitlements/mcstore", headers= {"Authorization": f"Bearer {token}"})
        if not resp.ok:
            return None
        return resp.json()


