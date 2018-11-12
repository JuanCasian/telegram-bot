#Function that finds the text after a keyword

def findWord(text, keyword):
    alltext = str(text).lower()
    keyword = str(keyword)
    if keyword in alltext:
        newtext = alltext.replace(keyword,"")
    result = newtext
    print (result)
    return result

