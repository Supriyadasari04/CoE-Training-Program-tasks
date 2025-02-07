# find gross salary using streamlit
import streamlit as st
st.title("Gross Salaray Calculation")
basic_salary =st.number_input("Enter basic salary :", min_value= 0)
if st.button("Calculate"):
    if (basic_salary < 10000):
       
       hra = (basic_salary * 67)/100
       da = (basic_salary * 73)/100
    elif (basic_salary > 20000):
        hra = (basic_salary * 73) / 100
        da = (basic_salary * 89) / 100




    else :
        hra = (basic_salary * 69) / 100
        da = (basic_salary * 76) / 100

    gross = hra+da+basic_salary
    st.write(f"Gross Salary : {gross}")