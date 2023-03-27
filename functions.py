from pathlib import Path
from gtts import gTTS
from PyPDF2 import PdfReader

def filepath_check(filepath, extension):
    # checks the filepath and returns an
    # according status
    path = Path(filepath)
    # check if the path exists
    if not path.exists():
        return "invalid path"
    # check if it is a file
    elif not path.is_file():
        return "not file"
    # check if extension is correct
    elif not filepath.endswith(extension):
        return "invalid extension"
    else:
        return "correct"
    
def generate_speech(filepath, extension):
    # function that generates the audio file
    # from filepath and extension
    # creating a name for recording
    name = filepath
    if "/" in filepath:
        name = filepath.split("/")[-1]
    if "." in name:
        name = name.split(".")[0]
    name += ".mp3"

    text = ""
    if extension == ".txt":
        file = open(filepath, "r")
        for line in file:
            text += line
        file.close()
    elif extension == ".pdf":
        reader = PdfReader(filepath)
        for page in reader.pages:
            text += page.extract_text()
    audio = gTTS(text = text, lang = "en", slow = False)
    audio.save(name)
    return