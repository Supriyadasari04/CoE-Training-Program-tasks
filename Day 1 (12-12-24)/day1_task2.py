# find gross salary

basic_salary =int(input("enter basic salary :"))
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
print("gross sal :",gross)