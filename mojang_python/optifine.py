import requests

class Cape:
    @staticmethod
    async def get_optifine_cape(username : str) -> str | None:
        
        """
        Get a optifine cape link.

        :param username: *completely correct* username to get optifine cape
        :rtype: str | None 
        
        """
       
        resp = requests.get(f"http://s.optifine.net/capes/{username}.png")
        if not resp.ok:
            return None
        return resp.url