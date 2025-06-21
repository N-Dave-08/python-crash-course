#1
with open("myname.txt", "w") as file:
    file.write("Jason Statham")

#2
with open("myname.txt", "r") as file:
    content = file.read()
    print(content)