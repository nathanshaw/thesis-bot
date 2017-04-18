import os, sys

# read in the thesis
# print results to a text file
# use the say command to playback the thesis
stop_chars = ["-", '"', "'"]
allowed_chars = [
'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I',
'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '1', '2',
'3', '4', '5', '6', '7', '8', '9',',','.', ' '
]

def readTxtFile(filePath):
    text = ""
    finalText = ""
    with open(filePath, "r") as f:
        text = f.read()
    for char in text:
        if char in allowed_chars:
            finalText += char

    return finalText

def writeTxtFile(filePath, contents):
    with open(filePath, "w") as f:
        f.write(contents)

def sayWords(thesis):
    voice = "Fred"
    command = "say -v " + voice + " " + thesis[:10000]
    os.system(command)

thesis = "hello world"
sayWords(thesis)
writeTxtFile("text.txt", thesis)
thesis = readTxtFile("thesis/Thesis_txt.txt")
print(thesis)
sayWords(thesis)
writeTxtFile("text.txt", thesis)
