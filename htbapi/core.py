from requests import get, post
from socket import socket, AF_INET, SOCK_STREAM
from ssl import wrap_socket

HEADERS = {"User-Agent": "htbapi"}
BASE = "http://hackthebox.eu/api"

def postRequest(url, data, apitoken):
    return post(BASE + url + "?api_token=" + apitoken, data=data, headers=HEADERS)

def getRequest(url, apitoken):
    return get(BASE + url + "?api_token=" + apitoken, headers=HEADERS)

def rawPostSSL(url, data, apitoken):
    if data != "":
        ct = "\r\nContent-Type: application/json"
    else:
        ct = ""
    ws = wrap_socket(socket(AF_INET, SOCK_STREAM), server_side=False)
    ws.connect(("www.hackthebox.eu", 443))
    request = f"POST /api{url}?api_token={apitoken} HTTP/1.1\r\nHost: www.hackthebox.eu{ct}\r\nUser-Agent: htbapi\r\n\r\n{data}\r\n"
    ws.send(request.encode())
    print(request)
    return ws.recv(1024)







