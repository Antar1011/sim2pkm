cd `dirname $0`
cd sim2pkm
python gui.py
osascript -e 'tell application "Terminal" to quit'
