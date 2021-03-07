import requests as req
import json
import src.conf as conf
import time

HEADER_JSON = {'content-type': 'application/json', 'Authorization': conf.auth['key']}


def ping(BODY={'ping': 'pong'}):
    url = conf.api['endpoints']['ping']
    return req.post(url, json.dumps(BODY), headers=HEADER_JSON, verify=False).json()


def uploadVideo(filename, videoId):
    url = conf.api['endpoints']['stream'] + "/" + videoId
    files = {'datei': open(filename, 'rb')}
    return req.post(url, files=files, verify=False)


def uploadDataRaw(body):
    url = conf.api['endpoints']['data']
    return req.post(url, json.dumps(body), headers=HEADER_JSON, verify=False).json()


def uploadData(dataType, value):
    body = '{ "{}": "{}", "timestamp": "{}" }'.format(dataType, value, round(time.time()))
    return uploadDataRaw(body)
