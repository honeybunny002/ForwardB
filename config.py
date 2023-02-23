import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5653332521:AAFcQTmaQ4kFlex1RiVGvuzD2rgTHM3mo1s"
    APP_ID =27307346 
    API_HASH = "ab2ff146d9e34248742343824e5976ac"
    TG_USER_SESSION = "BQGgrVIAGVj4xUfN5t2bj4sLKLFjjomIr_nB643RF_Ws2TGAxdDonYlmLNxL5fHjVjapDniJ0wgMhYjiSzmv7m1gVNJpIwWcryEI3Ci6uA8vLZvsOwiFy0HGlBx_0tUU4F3l2HD8V5i53GHXq1fjkuNrbW60Us7A424S10O5fYmuIxy7fMjs1-oEif3lwgSb-Jjp3uYdLuBwqCCzHKLJQKu9cmTWyS55WXo3QtodHv5vZJPvNjWbOhhivuVr-JaIkdM8U730HYHC1BFXBBpIKQhUMaNPw_tCjONXkqHk1dlB-ESbzDJJsXQhyyJ_kCN_LCg4XsMZDgNJejXL-OX2ndL26ENh1QAAAAFpcMmuAA"
    DB_URI = "redis-cli -u redis://default:XJfv6dGJTdwfE79FClSN5LUYXtXDZsOb@redis-18662.c273.us-east-1-2.ec2.cloud.redislabs.com:18662"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
