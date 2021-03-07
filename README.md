# Beealive: Bienenstock

Hier wird bald eine Anleitung stehen lol

- [I²C Busses erstellen](https://www.instructables.com/id/Raspberry-PI-Multiple-I2c-Devices/)
- GPIO Pins aufschreiben
- Autostart oder Cron
- conf.py erstellen:
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