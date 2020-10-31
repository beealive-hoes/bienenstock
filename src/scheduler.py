import sensors.camera as camera
import sensors.multi1 as multi1
import sensors.multi2 as multi2
import sensors.rain as rain
import sensors.mic as mic
import sensors.windspeed as wind
import sensors.weight as weight
import schedule
import time

def run():
    schedule.every(6).hours.do(wind.measure)
    #schedule.every(6).hours.do(weight.measure)
    schedule.every(6).hours.do(multi1.measure)
    schedule.every(6).hours.do(multi2.measure)
    schedule.every(6).hours.do(rain.measure)
    #schedule.every(6).hours.do(mic.measure)
    schedule.every().day.at("00:05").do(rain.measure())
    schedule.every().day.at("00:06").do(rain.reset_rainfall())
    #schedule.every().day.at("9:15").do(camera.record,1,15,1)
    #schedule.every().day.at("11:00").do(camera.record,1,15,2)
    #schedule.every().day.at("12:15").do(camera.record,1,45,3)

    while True:
        schedule.run_pending()
        time.sleep(1)
