#!/usr/bin/env python3
import sys
salary = int(sys.argv[1]) - 3500

try:
   if 0< salary < 1500:
        print(format(salary*0.03,'.2f'))
   elif salary < 4500:
        print(format(salary*0.1 - 105, '.2f'))
   elif salary < 9000: 
        print(format(salary*0.2 - 555, '.2f'))
   elif salary <35000:
        print(format(salary*0.25 - 1005, '.2f'))
   elif salary < 55000:
        print(format(salary*0.3 -2755, '.2f'))
   elif salary < 80000:
        print(format(salary*0.35 -5505, '.2f'))
   else:
        print(format(salary*0.45 -13505, '.2f'))
except:
    print("Parameter Error")

