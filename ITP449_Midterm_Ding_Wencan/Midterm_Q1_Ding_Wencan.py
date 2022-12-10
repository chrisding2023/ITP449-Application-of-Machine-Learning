# Ding Wencan
# Question 1
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
amount = int(input("Loan Amount: "))
r = float(input("Annual Interest Rate: "))*0.01/12
m = int(input("Years: "))*12
Extra = int(input("Enter the amount of your extra payment each month:"))
PMTF = float(amount*(r*(1+r)**m)/((1+r)**m-1))
print("Your monthly payment is: $", round(PMTF,3))
print("Here is your loan history.")
loanbal = []
interest=[]
month = 0
extra = []
months =[]
while amount>= 0:
    month = month+1
    months.append(month)
    interestbalance = amount*r
    amount = amount + interestbalance - PMTF - Extra
    loanbal.append(round(amount,3))
    interest.append(round(interestbalance,3))
    extra.append(Extra)
extra[-1] = Extra+amount
loanbal[-1]= loanbal[-1]-amount
data = {"Month":months,"Interest":interest,"Balance":loanbal,"Extra":extra}
df = pd.DataFrame(data)
df.set_index(df["Month"],drop=True,inplace=True)
print(df)
print("You will pay off the loan in", m, "months")

# subplot 1 monthly interest paid vs month
# subplop 2
myFig = plt.figure(figsize= (14, 8))
ax1 = myFig.add_subplot(1,2,1)
ax2 = myFig.add_subplot(1,2,2)
ax1.set(xlabel='Month', ylabel='Interest paid')
ax2.set(xlabel='Month', ylabel='Loan Balance')
ax1.plot(df.index, df['Interest'], marker='o', linestyle='-',color='blue')
ax2.plot(df.index, df['Balance'], marker='o', linestyle='-',color='red')
plt.show()