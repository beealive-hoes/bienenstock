
# config.py

server = {
  'url': 'http://localhost:9010/',
  'api_url': 'http://localhost:9010/api/'
}

# server = {
#   'url': 'http://gh.selfip.org:24252/',
#   'api_url': 'http://gh.selfip.org:24252/api/'
# }

api = {
  'endpoints': {
    'ping': server['api_url'] + 'ping',
    'stream': server['api_url'] + 'stream'
  }
}

