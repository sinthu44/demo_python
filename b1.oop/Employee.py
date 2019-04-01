from Person import *

class Employee(Person):
    def __init__(self, chayNhanh='500km'):
        self.chayNhanh = chayNhanh

    def chay(self):
        return self.chayNhanh
