import requests as req
import json
import conf as conf
import time


HEADER_JSON = { 'content-type': 'application/json', 'Authorization': 'apidm28MWd902kDMa09UADK19SKD10DAKd29D' }


class Server(object):

  @staticmethod
  def ping(BODY = { 'ping': 'pong' }):
    url = conf.api['endpoints']['ping']
    return req.post(url, json.dumps(BODY), headers=HEADER_JSON, verify = False).json()

  @staticmethod
  def uploadVideo(filename, id):
    url = conf.api['endpoints']['stream']+ "/" + id
    files = {'datei': open(filename,'rb')}
    return req.post(url, files=files, verify = False)

  @staticmethod
  def uploadDataRaw(body):
    url = conf.api['endpoints']['data']
    return req.post(url, json.dumps(body), headers=HEADER_JSON, verify = False).json()

  @staticmethod
  def uploadData(type, value):
    body = '{ "{}": "{}", "timestamp": "{}" }'.format(type, value, round(time.time()))
    return Server.uploadDataRaw(body)

