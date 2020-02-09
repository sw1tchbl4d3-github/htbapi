import requests as req
from socket import socket, AF_INET, SOCK_STREAM
import ssl

HEADERS = {"User-Agent": "htbapi"}
BASE = "https://hackthebox.eu/api"

def postRequest(url, data, apitoken):
    return req.post(BASE + url + "?api_token=" + apitoken, data=data, headers=HEADERS)

def getRequest(url, apitoken):
    return req.get(BASE + url + "?api_token=" + apitoken, headers=HEADERS)

def rawPostSSL(url, apitoken):
    ws = ssl.wrap_socket(socket(AF_INET, SOCK_STREAM), keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE)
    ws.connect(("www.hackthebox.eu", 443))
    request = f"POST /api{url}?api_token={apitoken} HTTP/1.1\r\nHost: www.hackthebox.eu\r\n\r\n"
    ws.send(request.encode())







