from pathlib import Path

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
    elif not filepath.endswith(extension):
        return "invalid extension"
    else:
        return "correct"