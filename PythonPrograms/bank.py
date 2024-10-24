class Account:

    def __init__(self):
     self._balance =0
#Getter
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        global balance
        self._balance += n

    def withdraw(self,n):
        global balance 
        self._balance -= n 

def main():
    account = Account()
    print("Blanace:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()