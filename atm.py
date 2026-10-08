class ATM:
    def __init__(self):
        self.pin = "1234"
        self.balance = 10000
        self.history = []

    def login(self):
        attempts = 3

        while attempts > 0:
            entered_pin = input("Enter your PIN: ")

            if entered_pin == self.pin:
                print("Login successful!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN! Attempts left: {attempts}")

        print("Too many incorrect attempts.")
        return False

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Invalid amount!")
                return

            self.balance += amount
            self.history.append(f"Deposited ₹{amount:.2f}")

            print("Money deposited successfully!")
            print(f"New Balance: ₹{self.balance:.2f}")

        except ValueError:
            print("Please enter a valid amount!")

    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount!")
                return

            if amount > self.balance:
                print("Insufficient balance!")
                return

            self.balance -= amount
            self.history.append(f"Withdrawn ₹{amount:.2f}")

            print("Please collect your cash.")
            print(f"Remaining Balance: ₹{self.balance:.2f}")

        except ValueError:
            print("Please enter a valid amount!")

    def mini_statement(self):
        if len(self.history) == 0:
            print("\nNo transactions yet.")
            return

        print("\n----- Mini Statement -----")

        for transaction in self.history:
            print("-", transaction)

        print(f"Current Balance: ₹{self.balance:.2f}")

    def change_pin(self):
        old_pin = input("Enter current PIN: ")

        if old_pin != self.pin:
            print("Incorrect current PIN!")
            return

        new_pin = input("Enter new 4-digit PIN: ")

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must be exactly 4 digits!")
            return

        confirm_pin = input("Confirm new PIN: ")

        if new_pin != confirm_pin:
            print("PINs do not match!")
            return

        self.pin = new_pin
        print("PIN changed successfully!")


atm = ATM()

print("===== Welcome to ATM =====")

if atm.login():

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            atm.deposit()

        elif choice == "3":
            atm.withdraw()

        elif choice == "4":
            atm.mini_statement()

        elif choice == "5":
            atm.change_pin()

        elif choice == "6":
            print("\nThank you for using ATM!")
            break

        else:
            print("Invalid choice!")