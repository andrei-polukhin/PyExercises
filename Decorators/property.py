class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

    @full_name.deleter
    def full_name(self):
        print("obj.first and obj.last - are to be deleted!")
        self.first = None
        self.last = None


bond = Employee("James", "Bond")

bond.full_name = "Jack Mondello"

print(bond.first)
print(bond.email)
print(bond.full_name)

del bond.full_name
