# TempWatch

## Super simple monitoring of PC (Windows) CPU temperature

Lightweight localhost server (Flask) to listens for requests from front-end and returns CPU temperature.

Front-end consists of a basic line plotting (Chart.JS) of received data.

Reasons for creating:
- Procrastination
- Admin rights are required for temp monitoring and my laptop kept overheating during summer
- The first one...

## How to use

1. Clone repo to somewhere... If using admins rights is a security risk, save in a folder and lock changes.
2. Run (Python 3.x) backend/server.py with admin rights
    - Use Task Scheduler to save admin credentials for future runs
    - Use pythonw.exe rather than python.exe to suppress the console window
3. Open from browser and watch the plot populate with CPU temps 

## TODO
- Finish front-end
- Write unit tests
- Do unit testing
- Do integration test (aka run the goddam app)
- Investigate WMI options (or adopt OpenHardwareMonitor DLLs) to access temps of other parts of CPU