from tkinter import *
import tkinter.font as tkFont
from functions import *

class Interface:

    def __init__(self):
        self.root = Tk()

        # generating window
        self.root.title("Text to Speech Converter")
        self.root.geometry("700x375")

        # design parameters
        background_color = "#121212"
        self.root.configure(background = background_color)
        font_intro = tkFont.Font(family = 'Open Sans', size = 36, weight = 'bold')
        font_general = tkFont.Font(family = 'Open Sans', size = 16)

        # technical parameters
        type_options = [".pdf (PDF)", ".docx (Word)", ".txt (Text)"]

        # generating interface elements
        l_intro = Label(
            self.root,
            text = "Welcome to Text to Speech Converter!",
            bg = background_color,
            font = font_intro,
            padx = 25,
            pady = 5
            )
        l_intro.grid(
            row = 0,
            column = 0,
            columnspan = 3
            )

        l_textbox = Label(
            self.root,
            text = "1) Enter the path to the textfile you want to convert to speech:",
            bg = background_color,
            font = font_general
            )
        l_textbox.grid(
            row = 1,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )

        i_path = Text(
            self.root,
            height = 1,
            width = 50
            )
        i_path.grid(
            row = 2,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )

        l_filetype = Label(
            self.root,
            text = "2) Enter the extension of the file:",
            bg = background_color,
            font = font_general,
            )
        l_filetype.grid(
            row = 3,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )

        i_type = Listbox(
            self.root,
            height = len(type_options),
            width = 50
            )
        i_type.grid(
            row = 4,
            column = 0,
            sticky = W,
            padx = 25, 
            pady = 5
            )

        for i in range(1, len(type_options) + 1):
            i_type.insert(i, type_options[i - 1])

        b_generate = Button(
            self.root,
            text = "Generate",
            command = generate,
            bg = background_color,
            height = 2
            )
        b_generate.grid(
            row = 5,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )

        l_status = Label(
            self.root,
            text = "Status should be initially empty",
            bg = background_color,
            font = font_general
            )
        l_status.grid(
            row = 6,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )

        b_quit = Button(
            self.root,
            text = "Quit",
            command = self.root.destroy,
            height = 2,
            width = 5,
            bg = background_color
            )
        b_quit.grid(
            row = 7,
            column = 2,
            sticky = E,
            padx = 25
            )
        return
    
    def launch(self):
        self.root.mainloop()
        return