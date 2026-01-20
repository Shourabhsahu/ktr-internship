# Custom exception raised when the entered PIN is incorrect
class InvalidPINError(Exception):
    pass


# Custom exception raised when withdrawal amount exceeds balance
class InsufficientBalanceError(Exception):
    pass


# Custom exception raised when amount is zero or negative
class InvalidAmountError(Exception):
    pass


# This class represents a bank account
class Account:
    def __init__(self, acc_no, name, pin, balance):
        # Public details of account
        self.acc_no = acc_no
        self.name = name

        # Private data members (encapsulation)
        self.__pin = pin
        self.__balance = balance

    # Verifies whether the entered PIN is correct
    def verify_pin(self, entered_pin):
        if entered_pin != self.__pin:
            raise InvalidPINError("Incorrect PIN")

    # Returns the current balance
    def get_balance(self):
        return self.__balance

    # Adds money to the account after validation
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")
        self.__balance += amount

    # Withdraws money after checking amount and balance
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.__balance -= amount


# This class simulates the ATM machine
class ATM:
    def __init__(self, account):
        # ATM works with a specific account
        self.account = account

    # Starts the ATM session
    def start(self):
        try:
            # Asking user to enter PIN
            pin = int(input("Enter your PIN:1234 "))

            self.account.verify_pin(pin)

            # Menu keeps running until user exits
            while True:
                print("\n1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")

                choice = int(input("Choose an option: "))

                if choice == 1:
                    print(f"Your balance is: {self.account.get_balance()}")

                elif choice == 2:
                    amount = float(input("Enter deposit amount: "))
                    self.account.deposit(amount)
                    print("Deposit successful")

                elif choice == 3:
                    amount = float(input("Enter withdrawal amount: "))
                    self.account.withdraw(amount)
                    print("Please collect your cash")

                elif choice == 4:
                    print("Thank you for using the ATM")
                    break

                else:
                    print("Invalid option. Please try again.")

        # Handling incorrect PIN error
        except InvalidPINError as e:
            print(e)

        # Handling insufficient balance error
        except InsufficientBalanceError as e:
            print(e)

        # Handling invalid amount error
        except InvalidAmountError as e:
            print(e)

        # Handling wrong input types like characters instead of numbers
        except ValueError:
            print("Invalid input. Please enter numbers only.")

        # This block always executes at the end
        finally:
            print("Session ended")


# Program execution starts here
if __name__ == "__main__":
    # Creating an account with sample details
    account = Account(101, "Charlie", 1234, 5000)

    # Creating ATM object and starting session
    atm = ATM(account)
    atm.start()
