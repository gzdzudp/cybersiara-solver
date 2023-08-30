from utils.fingerprinter    import getfinger
from colorama       import Fore
from threading      import Thread
from utils.tls      import getja3
from tls_client     import Session
from time           import time, sleep
from random         import randint


class CybersiaraSolver:
    def __init__(self) -> None:

        self.fingerprint = getfinger()
        self.useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"

        session = Session(client_identifier="Chrome116", ja3_string=getja3())
        self.session = session
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "embed.mycybersiara.com",
            "Origin": "https://www.cybersiara.com",
            "Referer": "https://www.cybersiara.com/",
            "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": self.useragent
        }



    def getcap(self):
        self.visiterid = randint(10**(6-1), 10**6 - 1)
        self.requestid = randint(10**(7-1), 10**7- 1)

        payload = {
            "MasterUrlId" : "OXR2LVNvCuXykkZbB8KZIfh162sNT8S2",
            "DeviceName" : self.useragent,
            "RequestUrl" : "https://www.cybersiara.com/book-a-demo",
            "BrowserIdentity": self.fingerprint,
            "PluginNo" : 0,
            "VisiterId": self.visiterid,
            "LanguageId" : 1,
            "RequestID" : self.requestid,
            "LangChange" : 0,
            "ClickSecond" : randint(22, 46),
            "Iscookie" : 1,
            "DeviceHeight" : 1080,
            "DeviceWidth" : 1920
        }


        r = self.session.post("https://embed.mycybersiara.com/api/CyberSiara/GetCyberSiara", headers=self.headers, data=payload)
        return r.json()


    def verifycap(self):
        cap = self.getcap()
        
        if cap["HttpStatusCode"] == 400: return "ratelimit"

        payload = {
            "RequestID" : self.requestid,
            "FPID" : self.fingerprint,
            "VisiterId" : self.visiterid
        }
        
        r = self.session.post("https://embed.mycybersiara.com/api/v2/verification/fp", headers=self.headers, data=payload)

        return r.json()
    

    def solvecap(self):
        cap = self.verifycap()
        if cap == "ratelimit": return "ratelimit"
        payload = {
            'MasterUrl': 'OXR2LVNvCuXykkZbB8KZIfh162sNT8S2',
            'DeviceName': self.useragent,
            'BrowserIdentity': self.fingerprint,
            'Protocol': 'https:',
            'VisiterId': self.visiterid,
            'second': randint(2, 3),
            'RequestID': self.requestid
        }

        r = self.session.post("https://embed.mycybersiara.com/api/v2/SubmitCaptcha/VerifiedSubmit", headers=self.headers, data=payload)

        return r.json()


def gen():
    try:
        while True:
            stime = time()
            solver = CybersiaraSolver()
            capkey = solver.solvecap()
            etime = time()
            if capkey == "ratelimit":
                print("Ratelimited")


            else:
                capkey = capkey["data"]
                if not capkey:
                    pass
                else:
                    ctime = str(int(etime - stime))
                    print(f"{Fore.LIGHTGREEN_EX}SOLVED {Fore.LIGHTWHITE_EX}| {Fore.LIGHTRED_EX}{ctime}s {Fore.LIGHTWHITE_EX}| {Fore.LIGHTYELLOW_EX}{capkey[:35]}")    
            sleep(1)
    except:
        pass
    
if __name__ == "__main__":
    for i in range(30):
        Thread(target=gen).start()