# pip install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv()


HOST = str(os.environ.get("host"))

ACCESS_ID = str(os.environ.get("access_id"))
API_KEY = str(os.environ.get("api_key"))
VALUE_KEY = str(os.environ.get("value_key"))

HTTP = str(os.environ.get("proxy_http"))
PROXY_HTTP = {
    #"https": HTTP,
    "http": HTTP
}

SOCKS5H = str(os.environ.get("proxy_socks5h"))
PROXY_SOCKS5H = {
    "https": SOCKS5H,
    "http": SOCKS5H
}
