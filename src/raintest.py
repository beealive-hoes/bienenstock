import schedule
import sensors.rain as rain


def run():
    schedule.every(1).hours.do(rain.test)

    while True:
        schedule.run_pending()