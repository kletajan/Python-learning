class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")
        
cat1 = Cat('Andy', 2)
cat2 = Cat('Phoebe', 3)

print(cat1.name)
print(cat1.info())
print(cat1.make_sound())