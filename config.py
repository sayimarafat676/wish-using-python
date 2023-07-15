# Specify which file (without .py extension) in the arts folder should be used
artFile = "default"
with open(f"arts/{artFile}.py", encoding="utf-8") as file:
    mainArt = file.read()

# Speed of art
speed = 0.0015
# Print code in the beginning
codePrint = False
codingSpeed = 0.00015
codeColor = 'red'
# Audio
playAudio = True
audio = 'HappyBirthday.MP3'
# Random color is chosen from the list
color = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
# Change the keys of the dict to change the color codes
# If you change the color codes for blink, remove blink(none) and random, you have to change it in the pprint() function of PyBirthdayWish.py too.
colorCodes = {
    '①': 'grey',
    '②': 'red',
    '③': 'green',
    '④': 'yellow',
    '⑤': 'blue',
    '⑥': 'magenta',
    '⑦': 'cyan',
    '⑧': 'white',
    '⑨': 'blink',
    '⑩': 'none',
    '®': 'random'
}
