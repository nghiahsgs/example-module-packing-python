class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello(self):
        print("hello %s and age: %s"%(self.name, self.age))
