import websockets
import asyncio
import time
from client_tests import Clienttests

# The main function that will handle connection and communication
# with the server


class CLient():
    tester = Clienttests()

    async def listen(self):
        url = "ws://127.0.0.1:7890"
        # Connect to the server
        async with websockets.connect(url) as ws:
            # Send a greeting message
            await ws.send("Hello Server!")
            # Stay alive forever, listening to incoming msgs
            print(time.time())
            previous_heart_beat_time = ''
            while True:
                time.sleep(.5)
                msg = await ws.recv()
                print(msg)
                if "heartbeat" in msg:
                    current_heart_beat_time = time.time()
                    self.tester.heartbeat_test(msg, current_heart_beat_time, previous_heart_beat_time)
                    print("out of tester method")
                    previous_heart_beat_time = current_heart_beat_time


    def start_cient_loop(self):
        asyncio.get_event_loop().run_until_complete(self.listen())
