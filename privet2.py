class Human:
    def __init__(self, character, name):
        self.character = character
        self.name = name
    def sleep(self):
        print(f"{self.name} сейчас спит!")
    def talk(self):
        print(f"{self.name}, сейчас разговаривает. Проявляется его {self.character} характер")

class Furry(Human):
    def __init__(self, character, name, suit):
        super().__init__(character, name)
        self.suit = suit
    def fursuit(self):
        print(f"Ваш {self.name} надел фурсьют {self.suit}")

furryman = Furry(name="Дурак", character="Злой", suit="Собака")
human = Human(name="Глупыш", character="Веселый")

furryman.fursuit()
human.talk()
human.sleep()