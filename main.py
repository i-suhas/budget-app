class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = "{:.2f}".format(item["amount"]).rjust(7)
            items += f"{description}{amount}\n"
            total += item["amount"]
        output = title + items + f"Total: {total:.2f}"
        return output
food_category = Category("Food")
clothing_category = Category("Clothing")

food_category.deposit(1000, "Initial deposit")
food_category.withdraw(200, "Groceries")
food_category.withdraw(50, "Restaurant")

clothing_category.deposit(500, "Initial deposit")
clothing_category.withdraw(100, "Shoes")
clothing_category.transfer(200, food_category)

print(food_category)
print(clothing_category)
