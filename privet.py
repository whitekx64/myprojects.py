class Children:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def typi(self):
        print(f"Имя вашего ребнка: {self.name}, возвраст: {self.age}")
    def death(self):
        print(f"Ваш ребенок {self.name} умер в возврасте {self.age} лет :c")
        
firstchildren = Children(name="Петя", age=12)