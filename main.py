import datetime

from fastapi import FastAPI
import subprocess
from Database import *
app = FastAPI()

@app.post("/start_robot/{start_num}")
async def start_robot(start_num: int):
    command = f"python robot.py {start_num}"
    process = subprocess.Popen(command)
    pid = process.pid
    message = {
        'PID':str(pid),
        'date_start':str(datetime.datetime.now()),
        'date_end': None,
        'number_start':start_num,
        'time': None,
    }
    print(message)
    _ = await insert_start_process([message])
    return message



@app.post("/stop_robot/{pid}")
async def stop_robot(pid):
    try:
        subprocess.check_call("TASKKILL /F /PID {pid} /T".format(pid=pid))
    except:
        return {"message": f"Процесс {pid} умер в неизвестное время :(  "}



    message = {
        'PID': str(pid),
        'date_end':datetime.datetime.now(),
    }
    _ = await insert_stop_process([message])
    return message


@app.get("/select_process")
async def select_process():
    res = await select_all_process()
    return res



@app.on_event("shutdown")
async def shutdown_event():
    items = await select_active_process()
    items = [
        {
            'PID': item[1],
            'date_end': datetime.datetime.now(),
        }
     for item in items]
    print('ITEMS',items)
    await insert_stop_process(items)
