def write():
    

def main():

    quest = input("Записать -- 0, прочитать -- 1: ")

    with open("file.txt", "w") as file:
        file.write("я очень люблю милых мальчиков :3 \n") 
        file.write(":P")

    with open("file.txt", "r") as file:
        content = file.read()
        print(content)