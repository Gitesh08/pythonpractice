
class atm:
    
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        
    def balance_amt(self):
        print("Your balance is ", self.balance)
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(amount, "Rs withdraw successful balance is ", self.balance)
    
    def deposit(self, amount):
        self.balance += amount
        print(amount, "Rs deposit successful! Your balance is:", self.balance)

def main():
    a = atm(12010214, 1108, 28000)
    
    while True:
        print()
        print("Welcome to Zeal cheet funds!")
        print("Select an option from :")
        print("1. Check balance")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. Exit")
    
        num = int(input("Enter your choice: "))
    
        if num == 1:
            a.balance_amt()
    
        elif num == 2:
            amount = int(input("Enter the amount: "))
            a.withdraw(amount)
        
        elif num == 3:
            amount = int(input("Enter the amount: "))
            a.deposit(amount)
        
        elif num == 4:
            print("Thank you for visit us!")
            break
        
        else:
            print("invalid selection")

if __name__ == "__main__":
    main()   







        
    
    
    
        
        
        
        
        
        
        
    
    
    

       
        
    
            