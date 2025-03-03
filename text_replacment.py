import pyautogui
import time
import msvcrt

# Variables
i = 0

# Asks user for the text to input
input_text = pyautogui.prompt(text='Enter your text here:', title='Text Replacment', default='')

# Prints next character in the text
def print_char():
    char_index = 0
    if char_index < len(input_text):
        pyautogui.write(input_text[char_index])
        char_index += 1
        time.sleep(2)
    else:
        quit

while i == 0:
    key = msvcrt.getch()
    if key:
        print_char