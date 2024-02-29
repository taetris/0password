import pyperclip

# copies the password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(str(password))
    print("Variable copied to clipboard.")
