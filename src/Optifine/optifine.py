import requests

class Cape:
    @staticmethod
    async def optifineCapeChecker(username):
        # username : 대문자까지 일치해야함
        resp = requests.get(f"http://s.optifine.net/capes/{username}.png")
        if not resp.ok:
            return None
        return f"http://s.optifine.net/capes/{username}.png"