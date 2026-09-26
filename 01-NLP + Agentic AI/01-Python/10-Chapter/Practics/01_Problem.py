class Programmer:
    compnay = "Microsoft"

    def __init__(self, name, age, salary, pincode):
        self.name = name
        self.age = age
        self.salary = salary
        self.pincode = pincode

p = Programmer("Harry", 25, 50000, 123456)
print(f"Name: {p.name}, Age: {p.age}, Salary: {p.salary}, Pincode: {p.pincode}, Company: {p.compnay}")        