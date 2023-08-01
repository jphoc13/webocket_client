Server - server.py, this is run first, via main.py.   Just run main.py file to start the server.
Client - client.py
Method1: Run this in terminal with "flask run" to run the first index method, make sure other index method commented out.
This will run the client in a thread using os library to run the file.

Have the data received by the client be put into a data base.  SQL lite for Python.

Use a scehduler to query the DB and populate the page.

Client will remain connected permanently, unless closed by user.  When open it will send messages
to a master parser that will send to a function based on the data parsed.

