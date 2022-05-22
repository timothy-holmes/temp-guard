# TempWatch

## Super simple monitoring of PC (Windows) CPU temperature

Lightweight localhost server (Flask) to listens for requests from front-end and returns CPU temperature.

Front-end consists of a basic line plotting (Chart.JS) of received data.

Reason for creating:
- Admin rights are required for temp monitoring and my laptop kept overheating during summer
- Small app to learn about unit testing/mocking/integration testing

## How to use

1. Clone repo to somewhere... If using admins rights is a security risk, save in a folder and lock changes.
2. Run (Python 3.x) backend/server.py with admin rights
    - Use Task Scheduler to save admin credentials for future runs
    - Use pythonw.exe rather than python.exe to suppress the console window
3. Open from browser and watch the plot populate with CPU temps 

## TODO
- Do integration test (aka run the app with WMI access)
- Investigate WMI options (or adopt OpenHardwareMonitor DLLs) to access temps of other parts of CPU
    - Include temps from more sensors (eg. individual cores, motherboard, GPU)
