import os

contributors = {
        "Esteban": "estebanpm99",
        "Jose Carlos": "Josstos1",
        "Sergio": "sgarcia98",
        "Daniel": "DanielCordovaV",
        "Juan Pedro": "JuanCasian" }

# This is the list of issues to edit for the automation
issues = ["{} Github Basics", "{} Python Basics"]

# From here DO NOT EDIT!

command = "gh is --new --title \"{}\" -A {}"

for issue in issues:
    for key, value in contributors.items():
        os.system(command.format(issue.format(key), value))
