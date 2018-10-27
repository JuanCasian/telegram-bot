import os

contributors = {
        "Esteban": "estebanpm99",
        "Jose Carlos": "Josstos1",
        "Sergio": "sgarcia98",
        "Daniel": "DanielCordovaV",
        "Juan Pedro": "JuanCasian" }

# This is the list of issues to edit for the automation
issues = [] 
keep_asking = True
while (keep_asking):
    print ("Please enter the title to the issue:")
    line = input()
    issues.append("{} " + line)
    print ("Do you want to add another issue? (yes/no)")
    line = input()
    if line != "yes":
        keep_asking = False


# From here DO NOT EDIT!
print ("Please review the command that are going to me sent")
command = "gh is --new --title \"{}\" -A {}"

for issue in issues:
    for key, value in contributors.items():
        print(command.format(issue.format(key), value))

print ("Is everything correct? (yes/no)")
line = input()

if (line != "yes"):
    print ("Okay, cancelling commands")
    exit()

print("Sending commands")
for issue in issues:
    for key, value in contributors.items():
        os.system(command.format(issue.format(key), value))
