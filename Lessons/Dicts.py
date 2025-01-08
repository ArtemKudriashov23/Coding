# Пустой словарь
my_dict = {}

# Словарь с данными
person = {
    "name": "Иван",
    "age": 25,
    "city": "Москва"
}

# Использование функции dict()
another_dict = dict(name="Ольга", age=30)

person["name"] = "Artem"
person["age"] +=1
person["profession"] = "programmer"
print(person)

profession = person.pop("profession")
print(profession)
print(person)

print(person.values())
print(person.keys())
print(person.items())