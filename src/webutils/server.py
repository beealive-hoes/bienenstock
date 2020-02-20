import requests as req
import json
import conf as conf


HEADER_JSON = { 'content-type': 'application/json' }


class Server(object):


  @staticmethod
  def ping(BODY = { 'ping': 'pong' }):
    url = conf.api['endpoints']['ping']
    return req.post(url, json.dumps(BODY), headers=HEADER_JSON, verify = False).json()

  @staticmethod
  def uploadVideo(filename):
    url = conf.api['endpoints']['stream']
    files = {'datei': open(filename,'rb')}
    return req.post(url, files=files, verify = False)