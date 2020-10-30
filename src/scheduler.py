import sensors.camera as camera
import sensors.multisensor as multi
import sensors.rain as rain
import sensors.mic as mic
import sensors.windspeed as wind
import schedule
import time

def run():
    schedule.every(6).hours.do(wind.measure)
    #schedule.every(6).hours.do(multi.measure)
    schedule.every(6).hours.do(rain.measure)
    #schedule.every(6).hours.do(mic.measure)
    schedule.every().day.at("9:15").do(camera.record,1,15,1)
    schedule.every().day.at("11:00").do(camera.record,1,15,2)
    schedule.every().day.at("12:15").do(camera.record,1,45,3)

    while True:
        schedule.run_pending()
        time.sleep(1)
