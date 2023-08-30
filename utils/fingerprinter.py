from subprocess     import check_output
from random         import randint
from re             import sub

def encodefinger(fingerprint: str) -> str:
    return check_output(["node", 'utils/encodedata.js', fingerprint]).decode('utf-8').strip()

def getfinger():
    navigator_info = {
        "mimeTypes": {"length": randint(2, 99)},
        "appCodeName": "Mozilla",
        "appName": "Netscape",
        "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "cookieEnabled": True,
        "deviceMemory": 8,
        "language": "pl-PL",
        "languages": ['pl-PL', 'de-PL', 'de', 'pl', 'en-US', 'en'],
        "onLine": True,
        "platform": "Win32",
        "product": "Gecko",
        "productSub": "20030107",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "vendor": "Google Inc.",
        "plugins": {"length": randint(5, 92)}
    }

    screen_info = {
        "availWidth": 1920,
        "availHeight": 1032,
        "width": 1920,
        "height": 1080,
        "colorDepth": 24,
        "pixelDepth": randint(21, 98),
        "isExtended": False,
        "orientation": {
            "angle": 0,
            "type": "landscape-primary"
        }
    }

    return encodefinger((
        str(navigator_info["mimeTypes"]["length"])
        + sub(r"\D+", "", navigator_info["userAgent"])
        + str(navigator_info["plugins"]["length"])
        + str(screen_info["height"] or "")
        + str(screen_info["width"] or "")
        + str(screen_info["pixelDepth"] or "")
    ))
