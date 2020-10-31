import schedule
import sensors.rain as rain
import sensors.multi1 as multi 1
import sensors.multi2 as multi 2


def run():
    schedule.every(1).hours.do(rain.test)

    while True:
        schedule.run_pending()