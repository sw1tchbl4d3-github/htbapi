import http.client
import requests as req
import urllib

HEADERS = {"User-Agent": "htbapi"}
BASE = "https://hackthebox.eu/api"

def postRequest(url, data, apitoken):
    return req.post(BASE + url + "?api_token=" + apitoken, data=data, headers=HEADERS)

def getRequest(url, apitoken):
    return req.get(BASE + url + "?api_token=" + apitoken, headers=HEADERS).json()

def postHTTPC(url, data, apitoken):
    conn = http.client.HTTPConnection("hackthebox.eu")
    conn.request("POST", "/api" + url + "?api_token=" + apitoken, urllib.parse.urlencode({"api_token": apitoken}) ,HEADERS)
    response = conn.getresponse()
    print(response.msg)
    






