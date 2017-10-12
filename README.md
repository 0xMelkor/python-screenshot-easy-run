# The easy way

1. Install Python2.7 on your machine: [Official repo](https://www.python.org/download/releases/2.7/)

2. Get precompiled `pyscreenshots-1.0.0.000.zip`: [Download link](https://github.com/insanediv/python-screenshot-easy-run/raw/master/pyscreenshots-1.0.0.000.zip)

3. Unzip the archive and double click `setup64.exe` or `setup32.exe` (Depending if you installed Python2.7 64 bit or 32 bit)

4. Setup will generate `start_daemon.bat`. Double click and, when asked, paste the screenshots destination folder in the terminal

That's it!

# If for some reason you need to regenerate the installers
Clone this repo and install `py2exe` dependencies in your python env.
Then run
`python py2exe_setup.py py2exe`
