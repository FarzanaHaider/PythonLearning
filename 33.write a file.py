text = "Miaw, miaw.\nI am a cat."

with open("test.txt",'w') as file: # overwrite
    file.write(text)

text = "\nHow are you?"

with open("test.txt",'a') as file: # append
    file.write(text)