import requests as req
import json
import src.conf as conf


HEADER_JSON = { 'content-type': 'application/json' }

class Server(object):

  @staticmethod
  def ping(BODY = { 'ping': 'pong' }):
    url = conf.api['endpoints']['ping']
    return req.post(url, json.dumps(BODY), headers=HEADER_JSON).json()

  @staticmethod
  def uploadVideo():
    # url = conf.api['endpoints']['stream']
    # files = { 'files' open('TODO.txt', 'rb') }
    # return req.post(url, files=files, data=data)
    print('TODO')