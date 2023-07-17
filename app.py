from flask import Flask, render_template
import os
import asyncio
from threading import Thread
import threading
from client_object import CLient


app = Flask(__name__)


# @app.route("/")
# def index():
#     thread = threading.Thread(target=os.startfile('client.py'), args=(1,))
#     thread.start()
#     return "hello world"

@app.route("/")
def index():
    CLient().start_cient_loop()
    return "hello world"

