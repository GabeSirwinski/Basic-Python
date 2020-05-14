import os

directory = 'C:\\Users\\Gabri\\Desktop\\Basic Python'

txtFile = ""

counter = 0

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        txtFile = (txtFile + "\n"  + directory + filename)
        counter = (counter + 1)
        continue
    else:
        continue

print("Here are the text files contained within {}: {}. \n There are {} total.".format(directory,txtFile,counter))
        
