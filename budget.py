class Category:

    # instance attributes
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # instance methods
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": str(description)})
        return True

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append(
                {"amount": -amount, "description": str(description)})
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def get_balance(self):
        return sum([item["amount"] for item in self.ledger])

    def check_funds(self, amount):
        return True if abs(amount) <= self.get_balance() else False

    def __str__(self):
        rows = "{:*^30}".format(f"{self.name}") + "\n"
        for entry in self.ledger:
            rows += f"{entry['description'][:23].ljust(23)}" + \
                "{:.2f}".format(entry['amount']).rjust(7) + "\n"
        rows += f"Total: {self.get_balance()}"
        return rows


def create_spend_chart(categories):
    names = []
    amounts = []
    percentages = []

    for category in categories:
        total = 0
        for amount in category.ledger:
            if amount["amount"] < 0:
                total += amount["amount"]
        amounts.append(total)
        names.append(category.name)

    for amount in amounts:
        percentages.append(amount / sum(amounts) * 100)

    labels = range(100, -10, -10)
    chart = 'Percentage spent by category\n'
    for label in labels:
        chart += f'{str(label).rjust(3)}| '
        for percent in percentages:
            if percent >= label:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'

    chart += '    ' + ('---' * len(categories)) + '-\n     '

    longest = (len(max(names, key=len)))

    for length in range(longest):
        for name in names:
            if len(name) > length:
                chart += name[length] + '  '
            else:
                chart += '   '
        if length < longest - 1:
            chart += '\n     '

    return chart
