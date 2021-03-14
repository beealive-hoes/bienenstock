import src.sensors.camera as camera
import src.sensors.multi as multi
import src.sensors.rain as rain
import src.sensors.mic as mic
import src.sensors.windspeed as wind
import src.sensors.weight as weight
import schedule
import time
import threading


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def run():
    schedule.every(6).hours.do(run_threaded, wind.measure)
    schedule.every(6).hours.do(run_threaded, weight.measure)
    schedule.every(6).hours.do(run_threaded, multi.measureInside1())
    schedule.every(6).hours.do(run_threaded, multi.measureOutside())
    schedule.every(6).hours.do(run_threaded, mic.measure)
    schedule.every().day.at("00:05").do(run_threaded, rain.measure)
    schedule.every().day.at("00:06").do(run_threaded, rain.reset_rainfall)
    schedule.every().day.at("9:15").do(run_threaded, camera.record, 1, 15, 1)
    schedule.every().day.at("11:00").do(run_threaded, camera.record, 1, 15, 2)
    schedule.every().day.at("12:15").do(run_threaded, camera.record, 1, 45, 3)

    while True:
        schedule.run_pending()
        time.sleep(1)


def debug():
    schedule.every(6).hours.do(run_threaded, wind.debug)
    schedule.every(6).hours.do(run_threaded, weight.debug)
    schedule.every(6).hours.do(run_threaded, multi.debugInside1())
    schedule.every(6).hours.do(run_threaded, multi.debugOutside())
    schedule.every(6).hours.do(run_threaded, mic.debug)
    schedule.every().day.at("00:05").do(run_threaded, rain.debug)
    schedule.every().day.at("00:06").do(run_threaded, rain.reset_rainfall)
    schedule.every().day.at("9:15").do(run_threaded, camera.debug, 1, 15, 1)
    schedule.every().day.at("11:00").do(run_threaded, camera.debug, 1, 15, 2)
    schedule.every().day.at("12:15").do(run_threaded, camera.debug, 1, 45, 3)

    while True:
        schedule.run_pending()
        time.sleep(1)
