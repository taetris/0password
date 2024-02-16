import pyperclip

def copy_to_clipboard(variable):
    pyperclip.copy(str(variable))
    print("Variable copied to clipboard.")
