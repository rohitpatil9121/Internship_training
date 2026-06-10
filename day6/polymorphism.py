# print(len("hello"))
# print(len("hello"))
# print(len("hello"))

class cat:
    def make_sound(self):
        return "meowwww"

class dog:
    def make_sound(self):
        return "bhauuuuuu"

def animal_sound_test(animal_object):
    print(animal_object.make_sound())

cat1 = cat()
dog1 = dog()

animal_sound_test(cat1)
animal_sound_test(dog1)

