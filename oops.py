# 4 pillars of OOPs
# Encapsulation
# Access Modifiers
"""class A:
    def __init__(self,name,age,gender): #constructor
        self.__name=name#private variable can be accessed inside of same class which defines with __name
        self._age=age#protected variable can be accessed inside of same class and child class which defines with _age
        self.gender=gender #public variable can be accessed inside of same class and child class and outside of class which defines
    def display(self):
        print(self.__name)
        print(self._age)
        print(self.gender)
    def setAge(self,age):
        self._age=age
    def getAge(self):
        return self._age
a1=A("Manogna",20,"female")
a2=A("Manu",20,"female")
print(a1.display())
a1.setAge(22)
print(a1.display())
print(a2.display())"""

# Abstraction
"""from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance-=amount
    def getBalance(self):
        return self.__balance
    @abstractmethod
    def interestcalc(self):
        pass
class SavingsAccount(BankAccount):
    def interestcalc(self):
        return self.getBalance() * 0.05
a=SavingsAccount(6000)
print(a.getBalance())
a.deposit(2000)
print(a.getBalance())
a.withdraw(1000)
print(a.getBalance())
print(a.interestcalc())"""

# Inheritance
"""class Animal:
    print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bow bow")
class Cat(Animal):
    def sound(self):
        print("Meow Meow")
a=Cat()
b=Dog()
print(a.sound())
print(b.sound())
# Polymorphism"""

