import pyautogui, time
time.sleep(5)
f = open("SOUTH AMERICA", 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(0.05)


# EUROPE        |   https://www.sporcle.com/games/g/europe
# AFRICA        |   https://www.sporcle.com/games/g/africa
# ASIA          |   https://www.sporcle.com/games/g/asia
# S.AMERICA     |   https://www.sporcle.com/games/g/southamerica
# N.AMERICA     |   https://www.sporcle.com/games/g/northamerica
# OCEANIA + AU  |   https://www.sporcle.com/games/g/oceania
# UNITED STATES |   https://www.sporcle.com/games/g/states
# WORLD         |   https://www.sporcle.com/games/g/world
