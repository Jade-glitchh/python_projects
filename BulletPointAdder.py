# Adds wikipedia bullet points to 
# the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

#TODO: Seperate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)  #join to get a single string value
pyperclip.copy(text)

