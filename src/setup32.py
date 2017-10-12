import os

VIRTUAL_ENV_DIR = 'venv'

if not os.path.exists(VIRTUAL_ENV_DIR):
    os.makedirs(VIRTUAL_ENV_DIR)

os.system("virtualenv -p 2.7 %s" % VIRTUAL_ENV_DIR)
os.system("%s\Scripts\pip install -r lib\\requirements.txt" % VIRTUAL_ENV_DIR)

with open("start_daemon.bat", "w") as start_script:
    start_script.write('set /p folder="Paste the destination folder path: "')
    start_script.write('\n')
    start_script.write('start venv\Scripts\python.exe app\pyscreen.py %folder%')