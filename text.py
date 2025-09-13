def write():
        inputuser = input("Что вы хотите вписать сюда? ")

        with open("file.txt", "w") as file:
            file.write(inputuser) 
            print("Текст вписан!")

def read():
    with open("file.txt", "r") as file:
        contant = file.read()
        print(contant)
    
def main():
    quest = input("Записать -- 0, прочитать -- 1: ")
    try:
        quest = int(quest)
    except ValueError:
        print(f"{quest} -- не число!")
    if quest == 0:
        write()
    elif quest == 1:
        read()

writenum = main()
