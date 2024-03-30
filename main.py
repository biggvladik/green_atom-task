from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/start_robot/{start_num}")
def start_robot(start_num: int):
    command = f"python robot.py {start_num}"
    process = subprocess.Popen(command)
    pid = process.pid
    return {"message": f"Robot started, Process number {pid} "}

@app.post("/stop_robot/{pid}")
def stop_robot(pid):
    subprocess.check_call("TASKKILL /F /PID {pid} /T".format(pid=pid))
    return {"message": f"Robot stopped, Process number {pid} "}
