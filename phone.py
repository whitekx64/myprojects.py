class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
class PhoneBook:
    def __init__(self):
        self.contacts = {}
    def addcontact(self, contact_object):
        """
        Этот метод добавляет новый вписанный контакт
        """
        if contact_object.name not in self.contacts:
            self.contacts[contact_object.name] = contact_object.phone_number
            print(f"'{contact_object.name}' был добавлен")
        else:
            print(f"Контант '{contact_object.name}' существует")
    def delcontact(self, contact_object):
        """
        Этот метод удаляет вписанный контакт
        """
        if contact_object.name in self.contacts:
            del self.contacts[contact_object.name]
            print(f"Контакт '{contact_object.name}' удален")
        else:
            print(f"Контакта '{contact_object.name}' несуществует")
    def findcontact(self, contact_object):
        """
        Этот метод выполняет поиск вписанного контакта
        """
        if contact_object.name in self.contacts:
            return print(f"Контакт {contact_object.name} был найден, его номер -- {contact_object.phone_number}")
        else:
            return print(f"Контакта {contact_object.name} не существует")
    def allcontacts(self):
        return print(f"Список контактов: {self.contacts}")


my_phonebook = PhoneBook()


contact = Contact(name= "FFFF", phone_number= 666)
contact1 = Contact(name= "Гойда слон", phone_number= 9424125412)
#Здесь вписать контакт, который хотите добавить(addcontact), удалить(delcontact) или найти(findcontact). Шаблон: "my_phonebook.действие(contact_object=выбранный контакт)"
my_phonebook.findcontact(contact_object=contact)
my_phonebook.addcontact(contact_object=contact)
my_phonebook.findcontact(contact_object=contact)
my_phonebook.addcontact(contact_object=contact1)
my_phonebook.allcontacts()