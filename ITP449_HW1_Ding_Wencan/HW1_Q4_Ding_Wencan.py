#Ding_Wencan
#ITP449 Fall 2021
#HW1
#Question 4
loan = input("Loan Amount:")
AIR = input("Annual Interest Rate:")
Year = input("Years:")
i = float(AIR)/12/100
n = float(Year)*12
PMT = float(loan)*i*(1+i)**n
PMT2 = (1+i)**n-1
PMTF =PMT/PMT2
print("Your monthly payment is: $",PMTF)

