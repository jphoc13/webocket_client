import websockets
import asyncio
import time
import logging
import sqlite3

logging.basicConfig(filename="std.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# The main function that will handle connection and communication
# with the server

con = sqlite3.connect("heartbeat.db", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS responses(time, message, type)")

async def listen():
    url = "ws://127.0.0.1:7890"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send a greeting message
        await ws.send("Hello Server!")
        # Stay alive forever, listening to incoming msgs
        # print(time.time())
        previous_heart_beat_time = ''
        while True:
            msg = await ws.recv()
            # logger.info(msg)
            if "heartbeat" in msg:
                try:
                    cur.execute(f"""INSERT INTO responses VALUES({time.time()}, "heartbeat", 'heartbeat')""")
                    con.commit()
                    await ws.send("Heart BEat code")
                except Exception as e:
                    logging.info(e)

            else:
                try:
                    cur.execute(f"""INSERT INTO responses VALUES({time.time()}, "not heartbeat", 'not heartbeat')""")
                    con.commit()
                except Exception as e:
                    logging.info(e)
        con.close()


asyncio.get_event_loop().run_until_complete(listen())
