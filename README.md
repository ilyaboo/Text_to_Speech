# Text to Speech Converter

This is a simple text to speech converter application developed using Python. The app allows the user to convert text files of different formats like PDF, Word, and Text files to an audio file that can be listened to. The application is developed using Python 3 and the Tkinter library is used for creating the GUI.

## Installation

To use this app, first, make sure that you have Python 3 with Tkinter package is installed on your computer. You can install python with Tkinter package [here](https://www.python.org/downloads/). 

Then, clone this repository using the following command:

```
git clone https://github.com/ilyaboo/text_to_speech.git
```
Navigate to the project directory and install the required packages using pip:

```
cd text_to_speech
pip install -r requirements.txt
```

## Usage

To launch the app, run the main.py file:

```
python main.py
```
After launching the app, follow the steps given below to convert the text file to an audio file:

- Enter the path to the text file you want to convert to speech in the text box.
- Select the extension of the file from the drop-down list.
- Click the "Generate" button to convert the file to speech.
- If the path entered is invalid, the application will display a message asking you to re-enter the path. If the file is not of the supported extension or cannot be read, the application will display a message stating the same.
- The generated audio file will be saved in the same directory as the input file.
## Technical Details

### Dependencies
The application was developed using Python 3 and the following packages:

- Tkinter: A Python interface for creating GUI applications.
- gTTS: A Python library and CLI tool to interface with Google Translate's text-to-speech API.
- PyPDF2: A Python library to work with PDF files.
- docx: A Python library to work with Word files.
### Files
The application consists of the following files:

- main.py: The main Python script that launches the application.
- interface.py: The Python module that defines the user interface of the application.
- functions.py: The Python module that defines the functions used in the application.
### Application Logic
The application has a simple logic that allows the user to enter the path to the input text file and the extension of the file. After clicking the "Generate" button, the application checks if the file exists and is of the supported extension. If everything is fine, the application reads the contents of the file and converts it to speech using the gTTS library. The generated audio file is saved in the same directory as the input file.
