#!/usr/bin/env python3
import sys

def calculate(fullsalary):
    try:
        insurance = int(fullsalary)*(0.08+0.02+0.005+0.06)
        if int(fullsalary) <= 3500:
            salary = 0
        else:
            salary = int(fullsalary) - 3500 -int(insurance)
        if 0<= salary < 1500:
            newsurance=format(salary*0.03,'.2f')
        elif salary < 4500:
            newsurance=format(salary*0.1 - 105, '.2f')
        elif salary < 9000: 
            newsurance=format(salary*0.2 - 555, '.2f')
        elif salary <35000:
            newsurance=format(salary*0.25 - 1005, '.2f')
        elif salary < 55000:
            newsurance=format(salary*0.3 -2755, '.2f')
        elif salary < 80000:
            newsurance=format(salary*0.35 -5505, '.2f')
        else:
            newsurance=format(salary*0.45 -13505, '.2f')
        realsalary = float(fullsalary) - float(insurance) - float(newsurance)
        getsalary = format(realsalary,'.2f')
        return getsalary
    except:
        print("Parameter Error")
 
if __name__ == '__main__':
    salarydict={}
    for arg in sys.argv[1:]:
        id = arg.split(':')[0]
        fullsalary = arg.split(':')[1]
        idsalary = calculate(fullsalary)
        salarydict[id]=idsalary
    for key,value in salarydict.items():
        print("%s:%s"%(key,value))
   
