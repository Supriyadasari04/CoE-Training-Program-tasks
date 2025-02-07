# Bank Problem using Streamlit
import streamlit as st
import sys

st.title("Bank Problem using Streamlit")

class Bank:
    acc_bal = 1000
    default_pin = 1234

    def deposit(self):
        amt_deposit = st.number_input("Enter amount to be deposited:", min_value=0)
        if amt_deposit >= 100 and amt_deposit < 50000 and amt_deposit % 100 == 0:
            self.acc_bal += amt_deposit
            st.success(f"Amount deposited successfully!")
            st.write(f"Updated balance: {self.acc_bal}")
        else:
            st.error("Deposit failed. Please ensure the amount is in multiples of 100 and within the allowed range.")

    def withdraw(self):
        amt_withdraw = st.number_input("Enter amount to be withdrawn:", min_value=0)
        newbal = self.acc_bal - 500
        if amt_withdraw >= 100 and amt_withdraw % 100 == 0 and amt_withdraw <= newbal and amt_withdraw <= 20000:
            self.acc_bal -= amt_withdraw
            if self.acc_bal >= 500:
                st.success("Amount withdrawn successfully!")
                st.write(f"Updated balance: {self.acc_bal}")
            else:
                st.error("Withdrawal failed. Minimum balance of 500 must be maintained.")
        else:
            st.error("Withdrawal failed. Check the amount and try again.")

    def bal_enquiry(self):
        st.write(f"Current balance: {self.acc_bal}")

    def exit(self):
        st.info("Thank you for banking with us!")
        sys.exit()


bank = Bank()
st.write("1. Deposit\n2. Withdraw\n3. Balance Enquiry\n4. Exit")
choice = st.number_input("Enter your choice:", min_value=0, max_value=4, step=1)

if choice == 1:
    bank.deposit()
elif choice == 2:
    bank.withdraw()
elif choice == 3:
    bank.bal_enquiry()
elif choice == 4:
    bank.exit()
else:
    st.error("Invalid option. Please choose a valid number.")
