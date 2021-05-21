import random
import PySimpleGUI as sg

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

layout = [
            [sg.Text("Choose the type of password you want to create: "),
            sg.InputCombo(('Numbers',
                        'Lower Characters',
                        'Upper Characters',
                        'Symbols',
                        'Lower And Upper Characters',
                        'All Mixed (Most Secure)'),size=(20,1))],
            [sg.Text("Choose the length of your password:"),
            sg.Slider(range=(1, 32), orientation='h', size=(34, 20), default_value=16)],
            [sg.OK(),
            sg.Cancel()]
        ]

window = sg.Window('Auto Password Generator', layout)

def number():
    numberPass = numbers
    lengthNum = values[1]
    generatedNumPass = "".join([random.choice(numberPass) for _ in range(int(lengthNum))])

    layoutNum = [[sg.Text("Your Password: ")],
                 [sg.Multiline(default_text=generatedNumPass, size=(35, 3))],
                 [sg.Text("Use CTRL-C to copy.")],
                 [sg.Text("Close this window to create another type of password.")]]
    windowNum = sg.Window('Password Result', layoutNum)
    while True:
        eventNum, valueNum = windowNum.read()
        if eventNum in (sg.WIN_CLOSED, 'Exit'):
            break
def lowerChar():
    lowChars = lower
    lengthLowChar = values[1]
    generatedLowCharPass = "".join([random.choice(lowChars) for _ in range(int(lengthLowChar))])

    layoutLowChar = [[sg.Text("Your Password: ")],
                    [sg.Multiline(default_text=generatedLowCharPass, size=(35, 3))],
                    [sg.Text("Use CTRL-C to copy.")],
                    [sg.Text("Close this window to create another type of password.")]]
    windowLowChar = sg.Window('Password Result', layoutLowChar)
    while True:
        eventLowChar, valueLowChar = windowLowChar.read()
        if eventLowChar in (sg.WIN_CLOSED, 'Exit'):
            break
def upperChar():
    upChars = upper
    lengthUpChar = values[1]
    generatedUpCharPass = "".join([random.choice(upChars) for _ in range(int(lengthUpChar))])

    layoutUpChar = [[sg.Text("Your Password: ")],
                   [sg.Multiline(default_text=generatedUpCharPass, size=(35, 3))],
                   [sg.Text("Use CTRL-C to copy.")],
                   [sg.Text("Close this window to create another type of password.")]]
    windowUpChar = sg.Window('Password Result', layoutUpChar)
    while True:
        eventUpChar, valueUpChar = windowUpChar.read()
        if eventUpChar in (sg.WIN_CLOSED, 'Exit'):
            break
def symbolsFunc():
    sym = symbols
    lengthSymbols = values[1]
    generatedSymbolsPass = "".join([random.choice(sym) for _ in range(int(lengthSymbols))])

    layoutSymbols = [[sg.Text("Your Password: ")],
                    [sg.Multiline(default_text=generatedSymbolsPass, size=(35, 3))],
                    [sg.Text("Use CTRL-C to copy.")],
                    [sg.Text("Close this window to create another type of password.")]]
    windowSymbols = sg.Window('Password Result', layoutSymbols)
    while True:
        eventSymbols, valueSymbols = windowSymbols.read()
        if eventSymbols in (sg.WIN_CLOSED, 'Exit'):
            break
def lowandUp():
    lowandUpChars = lower + upper
    lengthLowAndUpChars = values[1]
    generatedLowAndUpPass = "".join([random.choice(lowandUpChars) for _ in range(int(lengthLowAndUpChars))])

    layoutLowAndUp = [[sg.Text("Your Password: ")],
                     [sg.Multiline(default_text=generatedLowAndUpPass, size=(35, 3))],
                     [sg.Text("Use CTRL-C to copy.")],
                     [sg.Text("Close this window to create another type of password.")]]
    windowLowAndUp = sg.Window('Password Result', layoutLowAndUp)
    while True:
        eventLowAndUp, valueLowAndUp = windowLowAndUp.read()
        if eventLowAndUp in (sg.WIN_CLOSED, 'Exit'):
            break
def mix():
    mixed = lower + upper + numbers + symbols
    lengthMixed = values[1]
    generatedMixed = "".join([random.choice(mixed) for _ in range(int(lengthMixed))])

    layoutMixed = [[sg.Text("Your Password: ")],
                  [sg.Multiline(default_text=generatedMixed, size=(35, 3))],
                  [sg.Text("Use CTRL-C to copy.")],
                  [sg.Text("Close this window to create another type of password.")]]
    windowMixed = sg.Window('Password Result', layoutMixed)
    while True:
        eventMixed, valueMixed = windowMixed.read()
        if eventMixed in (sg.WIN_CLOSED, 'Exit'):
            break
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if values[0] == "Numbers":
        number()
    elif values[0] == "Lower Characters":
        lowerChar()
    elif values[0] == "Upper Characters":
        upperChar()
    elif values[0] == "Symbols":
        symbolsFunc()
    elif values[0] == "Lower And Upper Characters":
        lowandUp()
    elif values[0] == "All Mixed (Most Secure)":
        mix()
    else:
        print("You must choose the password type! Shutting DOWN!")
        break
