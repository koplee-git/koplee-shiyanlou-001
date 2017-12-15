#!/usr/bin/env python3
import os
import sys

class Config(object):
    def __init__(self,configfile):
        self.config={}
        self.configfile=configfile
        with open(self.configfile,'r') as f:
            for line in f:
                lst=line.strip('\n').split('=')
                self.config[lst[0]]=lst[1]
    @property
    def get_dict(self):
        return self.config
class UserData(object):
    def __init__(self,userdatafile):
        self.userdata={}
        self.userdatafile=userdatafile
        with open(self.userdatafile,'r') as f:
            for line in f:
                print(line)
                lst=line.strip().strip('\n').split(',')
                self.userdata[lst[0]]=lst[1]
        print("nimei%s"%self.userdata)
    @property
    def get_dict(self):
        return self.userdata
    @staticmethod
    def calculator(rate,fullsalary):
        try:
            insurance =int(fullsalary)*float(rate)
            if int(fullsalary) <=3500:
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
            salarylst=[]
            salarylst.append(realsalary) 
            salarylst.append(newsurance) 
            salarylst.append(insurance) 
            return salarylst
        except:
            print('error')
    @staticmethod
    def dumptofile(outputfile,lst_5):
       with open(outputfile,'w') as f:
           for line in lst_5:
               f.write(str(line))
if __name__ == '__main__':
    args=sys.argv[1:]
    arg_c=args.index('-c')
    arg_d=args.index('-d')
    arg_o=args.index('-o')
    configfile=args[arg_c+1]
    userdatafile=args[arg_d+1]
    outputfile=args[arg_o+1]
    config=Config(configfile)
    config_dict=config.get_dict
    print("wocao%s"%config_dict)
    rate = 0.00
    for value in config_dict.values():
        if float(value)< 1:
            rate += float(value)
    userdata=UserData(userdatafile)
    userdata_dict=userdata.get_dict
    for id_people,fullsalary in userdata_dict.items():
       lst_3=UserData.calculator(rate,fullsalary)
       UserData.dumptofile(outputfile,lst_3) 
