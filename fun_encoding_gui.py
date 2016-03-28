#!/usr/bin/env python

from Tkinter import *
import fun_encoding as fun


class Application(Frame):
    """ My GUI Application """

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets """
        Label(self,
              text="Enter string to encode/decode"
              ).grid(row=0, column=0, columnspan=2, sticky=W+E)

        self.entry = Entry(self)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)

        Button(self,
               text="Encode",
               command=lambda: self.call_module('e')
               ).grid(row=2, column=0, sticky=W+E)
        Button(self,
               text="Decode",
               command=lambda: self.call_module('d')
               ).grid(row=2, column=1, sticky=W+E)

        self.result = Text(self, width=40, height=5, wrap=WORD)
        self.result.grid(row=3, column=0, columnspan=2)
        # disable user input
        self.result.config(state=DISABLED)
        # enable selecting
        self.result.bind("<1>", lambda e: self.result.focus_set())

    def call_module(self, mode):
        """ Call encode/decode functions """
        entry = self.entry.get()

        try:
            if mode == 'e':
                result = fun.encode(entry)
            elif mode == 'd':
                result = fun.decode(entry)
            else:
                result = "?"
            self.result.bind("<1>", lambda e: self.result.focus_set())
        except fun.FunException as e:
            result = e.value
            self.result.unbind("<1>")

        self.result.config(state=NORMAL)  # enable change
        self.result.delete(0.0, END)
        self.result.insert(0.0, result)
        self.result.config(state=DISABLED)  # disable change


def main():
    # create window
    root = Tk()
    # set title & dims
    root.title("Fun Encoding v0.1")
    Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()
