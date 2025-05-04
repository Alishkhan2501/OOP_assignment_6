# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Default Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Class method to change bank name


# Create instances
b1 = Bank()
b2 = Bank()

# Change bank name
Bank.change_bank_name("National Bank")

# Show that both instances reflect the new name
print(b1.bank_name)
print(b2.bank_name)

