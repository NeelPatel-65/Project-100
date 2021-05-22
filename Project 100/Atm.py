class Atm(object):
    def __init__(self,cardnumber,pin):

        self.cardnumber = cardnumber
        self.pin = pin
        
        

    def Balance(self):
        print("your balance is 50000")
    
    def CashWithDraw(self,amount):
        newamount=50000-amount
        print("youhave withdrawn amount "+str(amount)+".your balance is "+str(newamount))

def main():
    card_number=input("Insert Your Card Number: ")
    pin_number = input("enter your pin number: ") 
    new_user= Atm(card_number,pin_number)

    print("choose the option ")
    print("1.balanceinquiry 2.withdrawel")

    activity= int(input("enter your option"))
    if (activity == 1):
        new_user.Balance()
    elif(activity == 2):
        amount=int(input("enter the amount"))
        new_user.CashWithDraw(amount)
    else:
        print("enter A valid number")


if __name__ == "__main__":
    main()