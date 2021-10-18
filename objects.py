class Item:
    # class attributes
    num_of_objects_created = 4

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Item.num_of_objects_created += 1
        # self.num_of_objects_created = 10
        print(f'object number {Item.num_of_objects_created} was created')

    def area(self):
        return self.num_of_objects_created ** 2

book = Item("tim", "27")
print(book.age)
print(book.num_of_objects_created)

book2 = Item("tim", 27)
print(book2.age)
print(Item.num_of_objects_created)

print(Item.__dict__)
print(book.__dict__)