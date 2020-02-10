from requests import get, post
from socket import socket, AF_INET, SOCK_STREAM
from ssl import wrap_socket
from html.parser import HTMLParser

HEADERS = {"User-Agent": "htbapi"}
BASE = "http://hackthebox.eu/api"

# to remove the links etc... from shoutbox messages
class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data

def getRequest(url, apitoken):
    return get(f"{BASE}{url}?api_token={apitoken}", headers=HEADERS)

def rawPostSSL(url, data, apitoken, datatype, recvstop):
    if not datatype == "":
        ct = f"Content-Type: application/{datatype}\r\n"
    else:
        ct = ""
    ws = wrap_socket(socket(AF_INET, SOCK_STREAM), server_side=False)
    ws.connect(("www.hackthebox.eu", 443))
    request = f"POST /api{url}?api_token={apitoken} HTTP/1.1\r\nHost: www.hackthebox.eu\r\nUser-Agent: htbapi\r\n{ct}\r\n{data}\r\n"
    ws.send(request.encode())
    data = b""
    if not recvstop == "":
        while True:
            tdata = ws.recv(1024)
            data += tdata
            if recvstop.encode() in tdata:
                break
    else:
        data = ws.recv(1024)
    return data

def shoutboxToText(shoutboxResponse):
    # Kown Issues: Boxes, Challenges or Names with those symbols in it aren't gonna show up. gonna fix this at some point, but good for now.
    f = HTMLFilter()
    shoutboxResponse = shoutboxResponse[shoutboxResponse.find("]"):]
    shoutboxResponse = shoutboxResponse.replace("\\/", "/")
    shoutboxResponse = shoutboxResponse.replace("[\"", "")
    f.feed(shoutboxResponse)
    shoutboxResponse = f.text
    shoutboxResponse = shoutboxResponse.replace("] ", "")
    shoutboxResponse = shoutboxResponse.replace("]", "")
    shoutboxResponse = shoutboxResponse.replace("\"}", "")
    shoutboxResponse = shoutboxResponse.replace("\"]}", "")
    shoutboxResponse = shoutboxResponse.replace("[Tweet", "")
    shoutboxResponse = shoutboxResponse.replace("  ", " ")
    shoutboxResponse = shoutboxResponse.replace("\n", "")
    return shoutboxResponse








