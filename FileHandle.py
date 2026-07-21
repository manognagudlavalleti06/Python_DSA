with open("file1.txt","w")as file:
    file.write("Hello Manu")
with open("file1.txt","r")as file:
    print(file.read())
with open("file1.txt","a")as file:
    file.write("\nPython Programming")