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

        # init variables
        num_cols = 3

        # create objects
        # row 0
        Label(self,
              text="Enter string to encode or decode"
              ).grid(row=0, column=0, columnspan=num_cols, sticky=W+E)

        # row 1
        self.entry = Entry(self)
        self.entry.grid(row=1, column=0, columnspan=num_cols, sticky=W+E)

        # row 2
        Button(self,
               text="Encode",
               command=lambda: self.call_module('e')
               ).grid(row=2, column=0, sticky=W+E)
        Button(self,
               text="Decode",
               command=lambda: self.call_module('d')
               ).grid(row=2, column=1, sticky=W+E)
        Button(self,
               text="Clear",
               command=self.call_clear
               ).grid(row=2, column=2, sticky=W+E)

        # row 3
        self.result = Text(self, width=40, height=5, wrap=WORD)
        self.result.grid(row=3, column=0, columnspan=num_cols)
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
        self.result.delete(0.0, END)  # clear Text
        self.result.insert(0.0, result)  # add result
        self.result.config(state=DISABLED)  # disable change

    def call_clear(self):
        self.entry.delete(0, END)  # clear Entry
        self.result.config(state=NORMAL)  # enable change
        self.result.delete(0.0, END)  # clear Text
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
