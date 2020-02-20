
# config.py

server = {
  'url': 'https://ddns1.maanex.tk:5041/',
  'api_url': 'https://ddns1.maanex.tk:5041/api/'
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

