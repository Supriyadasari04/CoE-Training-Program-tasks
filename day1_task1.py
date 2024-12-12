# find total shoppping expenditure and percentage of amount spent

s = int(input("enter sal :"))
shop1 = int(input("enter shop1 : "))
shop2 = int(input("enter shop2 : "))
shop3 = int(input("enter shop3 : "))
totals = shop1 + shop2 + shop3
print(totals)
per = (totals / s) * 100
print(per)
