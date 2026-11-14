ASHE - Windows desktop build
=================================

Option A: run from source (for testing)
  1. Install Python 3.11+ (tick "Add python.exe to PATH").
  2. Open PowerShell in this folder and run:
       python -m venv venv
       venv\Scripts\activate
       pip install -r requirements.txt
       python ashe.py

Option B: build ASHE.exe
  1. Double-click build.bat (it installs what it needs, then builds).
  2. The result is dist\ASHE.exe. Copy it anywhere and run it.

Notes
- The window uses Microsoft Edge WebView2, which is already on Windows 10/11.
  If it is missing, the program opens in your browser instead.
- Camera, microphone, MediaPipe and real sensor hardware are NOT included.
  Sensors are simulated; real readings can be sent to the local API.
- Educational prototype. Not a certified medical device.

What's new in this version
- Welcome banner with the astronaut's name + Good Morning / Good Evening (by the clock).
- Astronaut avatar card (replaces the photo), round + rounded-rectangle buttons.
- Medical Card: name, medical conditions, height, weight (stored on this device only).
- Voice chat mute button. Any critical/danger alert un-mutes automatically and plays an alarm tone.
- Sudoku (easy / medium / hard) in the Games tab.
- 11 new space wallpapers (nebulae, planets, deep space). Your own pictures: put them in the
  "wallpapers" folder next to ashe.py / ASHE.exe, or use Wallpaper > Choose image.

Version 4 changes
- Games > Single-player: Piano, Xylophone, Guitar, Drums (free play + "Echo challenge").
- Wallpapers: "Savanna animals" and "Underwater" removed.
- Language button label is now "AR / EN" (behaviour unchanged).
- Water alarm (Sensors tab): reminder every 60 min by default, on/off switch, interval 5-240 min, Test button.
- backup_before_v4\ashe_v3.py is the previous version of ashe.py.
