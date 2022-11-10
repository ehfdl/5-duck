class Person:
    def __init__(self, param_name):
        print('i am created!', self)
        self.name = param_name

    def talk(self):
        print('안녕하세요, 제 이름은', self.name, "입니다")

person_1 = Person("최영진")
person_1.talk()
print(person_1)
person_2 = Person('박에진')
person_2.talk()
print(person_2)