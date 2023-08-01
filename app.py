from flask import Flask, render_template
import os
import time
import sqlite3
import threading
import asyncio

app = Flask(__name__)


@app.route("/")
async def index():
    # log_reader = LogReader()
    thread = threading.Thread(target=os.startfile('client.py'), args=(1,))
    thread.start()
    time.sleep(5)
    con = sqlite3.connect("heartbeat.db", check_same_thread=False)
    cur = con.cursor()
    res = cur.execute("SELECT time, message, type FROM responses ORDER BY time DESC")
    print(f"Response: {res}")
    time.sleep(1)

    #return LogReader().follow("std.log")
    return res.fetchall()

# @app.route("/")
# def index():
#     CLient().start_cient_loop()
#     return "hello world"

