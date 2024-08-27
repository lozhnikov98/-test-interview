from tkinter import *
from tkinter import filedialog


def counter():
    output.delete("0.0","end")
    filename = filedialog.askopenfilename()
    with open(filename) as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
    text = text.lower()
    words = text.split()
    nonrep_words = list()
    for word in words:
        if word in nonrep_words:
            pass
        else:
            nonrep_words.append(word)
    output.insert("end","Amount of words: %d\n" % len(words))
    output.insert("end","Amount of nonrepeatable words: %d\n" % len(nonrep_words))

root = Tk()

frame = Frame(root)
frame.grid()

title = Label(frame, text="Word counter")
title.grid(row=1, column=1)

import_btn = Button(frame, text="Load file...", command=counter)
import_btn.grid(row=2, column=1, pady=4)

output = Text(frame, width=45, height=3)
output.grid(row=4, columnspan=3)


root.mainloop()