from tkinter import *
import tkinter.font as tkFont
from functions import *

class Interface:

    def __init__(self):
        self.root = Tk()

        # generating window
        self.root.title("Text to Speech Converter")
        self.root.resizable(False, False)

        # design parameters
        background_color = "#121212"
        self.root.configure(background = background_color)
        font_intro = tkFont.Font(family = 'Open Sans', size = 36, weight = 'bold')
        font_general = tkFont.Font(family = 'Open Sans', size = 16)

        # technical parameters
        type_options = [".pdf (PDF)", ".docx (Word)", ".txt (Text)"]

        # generating interface elements
        # welcome label
        l_intro = Label(
            self.root,
            text = "Welcome to Text to Speech Converter!",
            bg = background_color,
            fg = "white",
            font = font_intro,
            padx = 25,
            pady = 5
            )
        l_intro.grid(
            row = 0,
            column = 0,
            columnspan = 3
            )

        # first step label to enter the path to the text file
        l_textbox = Label(
            self.root,
            text = "1) Enter a path to the file you want to convert to speech:",
            bg = background_color,
            fg = "white",
            font = font_general
            )
        l_textbox.grid(
            row = 1,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )

        # window for the filepath
        self.i_path = Text(
            self.root,
            bg = background_color,
            fg = "white",
            height = 1,
            width = 55
            )
        self.i_path.grid(
            row = 2,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )
        self.i_path.configure(state = 'normal')

        # button to clear the path input
        b_clear = Button(
            self.root,
            text = "clear",
            command = self.clear_path,
            bg = "white",
            fg = background_color,
            height = 1
            )
        b_clear.grid(
            row = 2,
            column = 0,
            sticky = NE,
            padx = 30,
            pady = 0
            )

        # second step label to choose an extension of the file
        l_filetype = Label(
            self.root,
            text = "2) Enter the extension of the file:",
            bg = background_color,
            fg = "white",
            font = font_general,
            )
        l_filetype.grid(
            row = 3,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )

        # listbox to choose the extension
        self.i_type = Listbox(
            self.root,
            bg = "white",
            fg = background_color,
            height = len(type_options),
            width = 50
            )
        self.i_type.grid(
            row = 4,
            column = 0,
            sticky = W,
            padx = 25, 
            pady = 5
            )

        # adding options
        for i in range(1, len(type_options) + 1):
            self.i_type.insert(i, type_options[i - 1])

        # button to generate audio file
        b_generate = Button(
            self.root,
            text = "Generate",
            command = self.generate_speech,
            background = "white",
            fg = background_color,
            height = 2
            )
        b_generate.grid(
            row = 5,
            column = 0,
            sticky = W,
            padx = 25,
            pady = 5
            )

        # status label
        self.l_status = Label(
            self.root,
            text = "",
            bg = background_color,
            fg = "white",
            font = font_general,
            height = 2,
            justify = LEFT
            )
        self.l_status.grid(
            row = 6,
            column = 0,
            columnspan = 2,
            sticky = W,
            padx = 25,
            pady = 5
            )

        # quit button
        b_quit = Button(
            self.root,
            text = "Quit",
            command = self.root.destroy,
            bg = "white",
            fg = background_color,
            height = 2,
            width = 5
            )
        b_quit.grid(
            row = 7,
            column = 2,
            sticky = E,
            padx = 25,
            pady = 20
            )
        return
    
    def clear_path(self) -> None:
        # method that clears the path input
        self.i_path.delete("1.0", 'end-1c')
        return
    
    def set_status(self, status) -> None:
        # method that sets the status label 
        # according to the argument of the method
        # clearing status
        if status == "clear":
            self.l_status.config(text = "")
        # user entered wrong filepath
        elif status == "invalid path":
            self.l_status.config(text = "You entered a wrong filepath.\nPlease fix it and click 'Generate' again.")
        elif status == "not file":
            self.l_status.config(text = "This filepath isn't a file.\nPlease fix the filepath and click 'Generate' again.")
        elif status == "invalid extension":
            self.l_status.config(text = "You chose a wrong file extension.\nPlease choose the correct one and click Generate again.")
        elif status == "empty path":
            self.l_status.config(text = "Please enter the path to the file you want to convert.")
        elif status == "empty extension":
            self.l_status.config(text = "Please choose an extension of the file you want to convert.")
        elif status == "generating":
            self.l_status.config(text = "The program is generating the file. Please wait...")
        elif status == "invalid language":
            self.l_status.config(text = "Unfortunately, the language of the file is not supported.")
        elif status == "done":
            self.l_status.config(text = "Done!\nThe program generated an audio file!")
        self.root.update()
        return
    
    def get_path_input(self) -> str:
        # method to extract the entered filepath
        filepath = self.i_path.get("1.0", 'end-1c')
        return filepath
    
    def get_extension_input(self) -> str:
        # method that returns selected file type
        if len(self.i_type.curselection()) == 0:
            return None
        else:
            return self.i_type.get(self.i_type.curselection()[0])
    
    def get_input(self) -> (str, str):
        # method that extracts entered filepath and 
        # selected file type and returns them
        filepath = self.get_path_input()
        extension = self.get_extension_input()
        return (filepath, extension)
    
    def generate_speech(self) -> None:
        # function that attempts to generate the speech
        # from entered filepath and extension
        self.set_status("generating")
        filepath, extension = self.get_input()
        if filepath == "":
            self.set_status("empty path")
            return
        if extension == None:
            self.set_status("empty extension")
            return
        extension = extension.split(" ")[0]
        result = filepath_check(filepath, extension)
        if result == "correct":
            success = generate_speech_audio(filepath, extension)
            if not success:
                self.set_status("invalid language")
            else:
                self.set_status("done")
        else:
            # error handler
            self.set_status(result)
        return

    def launch(self) -> None:
        # method to launch the window of the application
        self.root.mainloop()
        return