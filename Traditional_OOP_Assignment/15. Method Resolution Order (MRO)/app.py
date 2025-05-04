# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(A):
    def show(self):
        print("Show from C")

class D(B, C):  # D inherits from both B and C
    pass

#  object of D and call show()
d = D()
d.show()

#  observe the Method Resolution Order
print(D.__mro__)
