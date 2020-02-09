import requests as req
import json
import config


HEADER_JSON = { 'content-type': 'application/json' }

class Server(object):

  @staticmethod
  def ping(BODY = { 'ping': 'pong' }):
    url = config.api['endpoints']['ping']
    return req.post(url, json.dumps(BODY), headers=HEADER_JSON).json()

  
