class RobloxAccount:
    def __init__(self, login, password):
        self.login = login
        self.__password = password # Приватный атрибут 
    def forgotpassword(self):
        question = input("Привет, вопрос для востановления пароля: Кличка твоего первого питомца? ")
        if question == "Нэш":
            return self.__password
        else:
            return "Вы непрвильно ответили на вопрос." 

account = RobloxAccount(login="Privet", password="qwerty")

print(account.forgotpassword())

#print(account.__password) <-- Вызовет ошибку