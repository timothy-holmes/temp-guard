Project on hold. Unable to use wmi and flask simulataneously due to mutlithreading conflicts. Multithreading isn't in my wheelhouse just yet, but it's on the list. I believe concurrency is the future of computing. I did gain some experience writing unit tests and semi-integrated testing inlcuding component mocking, and had fun playing software developer with Brendan. For the time being, I'll find a pre-existing solution if I need a temperature monitor this summer ;)

# TempWatch

## Super simple monitoring of PC (Windows) CPU temperature

Lightweight localhost server (Flask) to listens for requests from front-end and returns CPU temperature.

Front-end consists of a basic line plotting (Chart.JS) of received data.

Reason for creating:
- Admin rights are required for temp monitoring and my laptop kept overheating during summer ❌
- Small app to learn about unit testing/mocking/integration testing ✔️

## How to use

1. Clone repo to somewhere... If using admins rights is a security risk, save in a folder and lock changes.
2. Change into the `temp-guard` directory (`cd temp-guard`)
3. Install dependencies: `pip install -r requirements.txt`
4. Run (Python 3.x) `python app/__init__.py` with admin rights
    - Use Task Scheduler to save admin credentials for future runs
    - Use `pythonw.exe` rather than `python.exe` to suppress the console window
5. Open browser at URL `http://127.0.0.1:4999` and watch the plot populate with CPU temps 

## TODO
- Do integration test (aka run the app with WMI access) ❌ **Tests failed**
- Investigate WMI options (or adopt OpenHardwareMonitor DLLs) to access temps of other parts of CPU ❌ **Not able to integrate without .NET**
    - Include temps from more sensors (eg. individual cores, motherboard, GPU)
