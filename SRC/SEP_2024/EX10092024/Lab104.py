import math
try:
   math.exp(1000)   # OverflowError: math range error

except Exception as e:
       print(e)
       print("try to use the lower exp value")
