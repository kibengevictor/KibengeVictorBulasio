#opening a file
file = open("example.txt", "r")

#reading the contents of the file
content = file.read()

#closing the file
file.close()

print(content)  

#opening a file using 'with' statement
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # file is automatically closed after this block

    #reading the file line by line
    file.seek(0)  # move the cursor to the beginning of the file
    for line in file:
        print(line.strip())  # strip() removes the newline character at the end of each line

        