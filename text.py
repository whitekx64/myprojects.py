def question():
    quest = input("Записать -- 0, прочитать -- 1: ")
    return quest

def write(text):
    with open("file.txt", "w") as file:
        file.write(text) 

def read():
    with open("file.txt", "r") as file:
        contant = file.read()
        print(contant)

def main():
    question(writetext)
    write(writetext)
    read()

writetext = question