import os

directory = 'C:\\Users\\Gabri\\Desktop\\Basic Python'

txtFile = ""

counter = 0

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        time = os.path.getmtime(os.path.join(directory,filename))
        txtFile = (txtFile + "\n"  + os.path.join(directory,filename) + '\nmtime: ' + str(time) + "\n")
        counter = (counter + 1)
        continue
    else:
        continue

print("Here are the text files contained within {}:\n {}. \n \nThere are {} total.".format(directory,txtFile,counter))
        
