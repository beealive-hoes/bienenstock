import requests as req
import json
import src.conf as conf
import time

HEADER_JSON = {'content-type': 'application/json', 'Authorization': conf.auth['key']}


def ping():
    body = {'ping': 'pong'}
    url = conf.api['endpoints']['ping']
    return req.post(url, json.dumps(body), headers=HEADER_JSON, verify=False).json()


def upload_video(filename, video_id):
    url = f"{conf.api['endpoints']['stream']}/{video_id}"
    files = {'datei': open(filename, 'rb')}
    return req.post(url, files=files, verify=False)


def upload_data_raw(body):
    url = conf.api['endpoints']['data']
    return req.post(url, json.dumps(body), headers=HEADER_JSON, verify=False).json()


def upload_data(data_type, value):
    body = {data_type: value, "timestamp": round(time.time())}
    return upload_data_raw(body)
