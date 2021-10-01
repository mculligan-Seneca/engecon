from engecon import *





"""
Question 2:
To calculate the worth of a bond today, sum together the present worth of the face value (a future amount)
 and the coupons (an annuity) at an appropriate interest rate. For example,
  if money can earn 12 percent compounded semiannually,
   a bond maturing in 15 years with a face value of $5000 and a coupon rate of 7 percent is today worth
P = 5000(P/F,6%,30)+(5000×0.07/2)(P/A,6%,30) = 5000(0.17411) + 175(13.765)
= 3279.43
The bond is worth about $3279 today.
"""

coupon_rate=0.07
coupon_m=2 #Happens to be semi annually
n=15 #years
r=0.12
m=2
interest=r/m
bond_amt=5000

pv_lumpSum=(bond_amt*presWorthFact(interest,m*n))
coupon_pv=(bond_amt*coupon_rate/coupon_m)*seriesPresWorthFact(interest,m*n)
bond_pv=pv_lumpSum+coupon_pv
print(f'Present value of bond {bond_pv}')




print("Question 3")
#Atot=A'+G(A/G,i,n)
#Pv=?
#pv=[A'+g((A/G,i,n))](P/A,i,n)

k=6
g=50
n=4#years
aprime=500
r=0.12
m=12
interest=((1+r/m)**k)-1 #effective interest
atot=aprime+(g*gradientUniSeriesFact(interest,n*m/k))# 8 repair bills over 4 years
pv=atot*seriesPresWorthFact(interest,n*m/k)

print(f'Present worth of car is {pv}')
