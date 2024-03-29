# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V9o1pyqFEMrU37fERrgKNvumOpJAbkEg

### 1.Interest Computational Assignment
"""

from datetime import date
try:
  principal = float(input("How much you want to invest ?"))
  interestRate = float(input("What is fixed annual interest?"))
  interest= interestRate/100 
  #balanced amount after 30 year
  time = int(input("Time period?"))


  today = date.today()
  d1 = today.strftime("%d-%m-%Y")


  
  TotalAmount = principal*(1+(interest*time))

 
  TotalCompoundAmount = principal*pow(1+interest , time)
  
except Exception as error:
  print("An exception was thrown!")
  print(str(error))
  
  
print("Principal                         :" ,"{:.2f}".format(principal))

print("Rate of interest                  :" ,round(interestRate), "%" )

print("Today's Date                      :" ,d1 )

print("Amount at  maturity               :" ,"{:.4f}".format(TotalAmount))

print("Amount at maturity (compounding)  :" ,"{:.4f}".format(TotalCompoundAmount))

pow(2,2)

