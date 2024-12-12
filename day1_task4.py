# Bank Problem


class Bank():
   print("Welcome to ABC bank")
   acc_bal = 1000
   def deposit(self):
       amt_deposit = int(input("Enter amount to be deposited : "))
       if (amt_deposit>=100 and amt_deposit < 50000 and amt_deposit%100 == 0):
           print("Amount deposited")
           self.acc_bal = self.acc_bal + amt_deposit
           print("Updated balace is :",self.acc_bal)
       else:
           print("Deposit failed")

   def withdraw(self):
       amt_withdraw=int(input("Enter amount to be withdrawn : "))
       newbal= self.acc_bal - 500
       if (amt_withdraw >=100 and amt_withdraw%100 ==0 and amt_withdraw <= newbal and amt_withdraw <= 20000):

           self.acc_bal = self.acc_bal - amt_withdraw
           if(self.acc_bal >=500):
               print("Amount withdrawn successfully")

               print("Amount after withdraw : ",self.acc_bal)
           else :
               print("Account shld maintain min bal")




       else :
           print("Withdraw Failed")


   def options(self):
       print("1.Deposit\n 2.Withdraw \n 3.Bal Enquiry\n 4.EXIT")
       print("Choose your option")
       op = int(input("Enter your choice :"))
       if (op ==1):
           obj.deposit()
       elif (op ==2):
           obj.withdraw()

   def validation(self):
       c = 1
       while(c <=3):
           default_pin = 1234
           pin = int(input("Enter pin : "))
           if (pin == default_pin):
               obj.options()
           else:
               if c<3:
                   print("Invalid pin number. Please re-enter the pin")
               else :
                   print("Accoutn blocked")
           c = c + 1
obj=Bank()
obj.validation()