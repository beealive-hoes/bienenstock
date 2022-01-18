from src.sensors import camera, multi, rain, mic, windspeed as wind, weight
import schedule
import time
import threading


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def run():
    schedule.every(6).hours.do(run_threaded, wind.measure)
    schedule.every(6).hours.do(run_threaded, weight.measure)
    schedule.every(6).hours.do(run_threaded, multi.measure_inside_1)
    schedule.every(6).hours.do(run_threaded, multi.measure_outside)
    schedule.every(6).hours.do(run_threaded, mic.measure)
    schedule.every().day.at("00:05").do(run_threaded, rain.measure)
    schedule.every().day.at("00:06").do(run_threaded, rain.reset_rainfall)
    schedule.every().day.at("9:15").do(run_threaded, camera.record, 60, 15, 1)
    schedule.every().day.at("11:00").do(run_threaded, camera.record, 60, 15, 2)
    schedule.every().day.at("12:15").do(run_threaded, camera.record, 60, 45, 3)

    while True:
        schedule.run_pending()
        time.sleep(1)


def debug():
    schedule.every(6).hours.do(run_threaded, wind.debug)
    schedule.every(6).hours.do(run_threaded, weight.debug)
    schedule.every(6).hours.do(run_threaded, multi.debug_inside_1)
    schedule.every(6).hours.do(run_threaded, multi.debug_outside)
    schedule.every(6).hours.do(run_threaded, mic.debug_record)
    schedule.every().day.at("00:05").do(run_threaded, rain.debug)
    schedule.every().day.at("00:06").do(run_threaded, rain.reset_rainfall)
    schedule.every().day.at("9:15").do(run_threaded, camera.debug)
    schedule.every().day.at("11:00").do(run_threaded, camera.debug)
    schedule.every().day.at("12:15").do(run_threaded, camera.debug)

    while True:
        schedule.run_pending()
        time.sleep(1)
