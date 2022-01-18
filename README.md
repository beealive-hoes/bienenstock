# Beealive: Bienenstock

BeeAlive ist ein Projekt des Rotary Clubs Höchstadt oder so

# Installation
1. Projekt klonen oder runterladen und benötigte Packages installieren:

        $ git clone https://github.com/beealive-hoes/bienenstock.git
        $ pip install -r requirements.txt

2. Die benötigte `src/conf.py` erstellen:
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

3. [I²C Busses erstellen](https://www.instructables.com/id/Raspberry-PI-Multiple-I2c-Devices/) und dann in `src/sensors/GPIOPINS.py` eintragen

Problem: Zusätzliche I²C Busses brauchen Widerstände

# Ausführen
Autostart und Cron

### TODO:
- Cron Anleitung
- rain.py muss noch so verändert werden, dass man resetten kann
- scheduler.py wird nicht mehr gebraucht durch cron
- weight.py muss richtig implementiert werden, da funktioniert noch garnichts
- Eigentlich alle Module testen