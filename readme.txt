Server - server.py, this is run first, via main.py.   Just run main.py file to start the server.
Client - client.py
Method1: Run this in terminal with "flask run" to run the first index method, make sure other index method commented out.
This will run the client in a thread using os library to run the file.  I am stuck here because I haven't figured out
how to grab the data to display it in a web page.

Method2: Run this with flak run, with first index method commented out.  I am stuck here because this error pops up,
and I am confused as to why: "RuntimeError: There is no current event loop in thread 'Thread-1 (process_request_thread)'".

Below are the next steps I need to work on to get this app completed.

Monitors - instead of using pytest, this will use monitoring in a web application using Flask.  Alerting
can be set up to send email or slack alerts, if certain thresholds hit.

Client will remain connected permanently, unless closed by user.  When open it will send messages
to a master parser that will send to a function based on the data parsed.

