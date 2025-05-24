class Bank:
    # Class variable
    bank_name = "HBL Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    # Class method to change the class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

# Creating instances
acc1 = Bank("Alice")
acc2 = Bank("Bob")

# Display initial bank name
print("Before changing bank name:")
acc1.show_details()
acc2.show_details()

# Change bank name using class method
Bank.change_bank_name("UBL Bank")

# Display after changing bank name
print("\nAfter changing bank name:")
acc1.show_details()
acc2.show_details()
