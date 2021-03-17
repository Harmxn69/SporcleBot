import pyautogui, time
time.sleep(5)
f = open("world-countries", 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(0.05)


# EUROPE (countries)    |   https://www.sporcle.com/games/g/europe
# UNITED STATES         |   https://www.sporcle.com/games/g/states
# WORLD (countries)     |   https://www.sporcle.com/games/g/world