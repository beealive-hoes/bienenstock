# Beealive: Bienenstock

BeeAlive ist ein Projekt des Rotary Clubs Höchstadt oder so

# Installation
`git clone https://github.com/beealive-hoes/bienenstock.git` oder `Download ZIP`

`pip install -r requirements.txt`

`src/conf.py` erstellen:
```python
server = {
    'url': 'SERVER URL',
    'api_url': 'SERVER API URL'
}

api = {
    'endpoints': {
        'ping': server['api_url'] + 'ping',
        'stream': server['api_url'] + 'stream',
        'data': server['api_url'] + 'data'
    }
}

auth = {
    'key': 'AUTHENTICIATION KEY'
}
```

[I²C Busses erstellen](https://www.instructables.com/id/Raspberry-PI-Multiple-I2c-Devices/) und dann in `src/sensors/GPIOPINS.py` eintragen

Autostart oder Cron (In-Progress xd)