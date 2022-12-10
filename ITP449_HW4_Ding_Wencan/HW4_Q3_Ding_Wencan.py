# Wencan Ding
# ITP449 Spring 2022
# HW4
# Q3
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
# change the size of figure
figure(figsize=(15, 10), dpi=80)
# calculate monthly payment
amount = int(input("Loan Amount: "))
r = float(input("Annual Interest Rate: "))*0.01/12
m = int(input("Year: "))*12
PMTF = amount*(r*(1+r)**m)/((1+r)**m-1)
print("Your monthly payment is: $", PMTF)
loanbal = []
interest=[]
for i in np.arange(m):
    interestbalance = amount*r
    amount = amount + interestbalance - PMTF
    loanbal.append(amount)
    interest.append(interestbalance)
# subplot 1 monthly interest paid vs month
plt.subplot(1,2,1)
plt.xlabel("Month")
plt.ylabel("Interest paid")
plt.scatter(np.arange(m),interest)
# subplot 2 principal balance vs month
plt.subplot(1,2,2)
plt.scatter(np.arange(m),loanbal)
plt.xlabel("Month")
plt.ylabel("Loan balance")
plt.show()