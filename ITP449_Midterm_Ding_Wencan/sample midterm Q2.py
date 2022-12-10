# Question2
import numpy as np
import pandas as pd
from decimal import Decimal

amount = int(input("Loan Amount: "))
r = float(input("Annual Interest Rate: "))*0.01/12
m = int(input("Years: "))*12
PMTF = float(amount*(r*(1+r)**m)/((1+r)**m-1))
format_float = "{:.2f}".format(PMTF)
print("Your monthly payment is: $", format_float)
print("Here is your loan history.")
loanbal = []
interest=[]
month = []
for i in np.arange(1,m+1):
    interestbalance = amount*r
    amount = amount + interestbalance - float(format_float)
    loanbal.append(amount)
    interest.append(interestbalance)
    month.append(i)
data = {"Month":month,"Interest": np.round([float(i) for i in interest],2),"Balance": np.round([float(i) for i in loanbal],2)}
df = pd.DataFrame(data=data)
df.set_index(df["Month"],drop=True,inplace=True)
print(df)
print("You will pay off the loan in", m, "months")