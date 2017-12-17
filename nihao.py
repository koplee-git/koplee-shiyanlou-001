#!/usr/bin/env python3
import sys
from multiprocessing import Process, Queue

queue1=Queue()
queue2=Queue()

class Config(object):
    def __init__(self,configfile):
        print("chushihua")
        self.config={}
        self.configfile=configfile
        with open(self.configfile,'r') as f:
            for line in f:
                lst=line.strip('\n').strip().split('=')
                self.config[lst[0].strip()]=lst[1].strip()
    @property
    def get_dict(self):
        return self.config
    @property
    def get_JiShuL(self):
        return self.config['JiShuL']
    @property
    def get_JiShuH(self):
        return self.config['JiShuH']
    @property
    def get_rate(self):
        rate = float(self.config['YangLao']) + float(self.config['YiLiao']) +float(self.config['ShengYu']) +float(self.config['ShiYe']) +float(self.config['GongShang'])+float(self.config['GongJiJin'])
        return rate 
class UserData(object):
    def __init__(self,userdatafile):
        self.userdata={}
        self.userdatafile=userdatafile
        with open(self.userdatafile,'r') as f:
            for line in f:
                lst=line.strip().split(',')
                self.userdata[lst[0].strip()]=lst[1].strip()
    @property
    def get_dict(self):
        return self.userdata
 
    @staticmethod
    def calculator(JiShuL,JiShuH,rate,fullsalary):
        def calculator_shebao(fullsalary):
            if float(fullsalary) < float(JiShuL):
                insurance=float(JiShuL)*float(rate)
            elif float(fullsalary) > float(JiShuH):
                insurance=float(JiShuH)*float(rate)
            else:
                insurance =float(fullsalary)*float(rate)
            return insurance   
        insurance = calculator_shebao(fullsalary)
        def calculator_geshui(fullsalary):
            if int(fullsalary) <=3500:
                salary = 0
            else:
                salary = float(fullsalary) - 3500 -float(insurance)

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
            return newsurance
        
        newsurance=calculator_geshui(fullsalary)
        
        realsalary = float(fullsalary) - float(insurance) - float(newsurance)
            
        salarylst=[]
        salarylst.append(insurance) 
        salarylst.append(newsurance) 
        salarylst.append(realsalary) 
        return salarylst
        
    @staticmethod
    def dumptofile(outputfile,lst_5):
        with open(outputfile,'a') as f:
            n =0 
            for i in lst_5:
                if n > 1:
                    i = format(float(i),'.2f')
                    f.write(str(i))
                else:
                    f.write(str(i))
                if n < 4:
                    f.write(',')
                    n +=1
            f.write('\n')

def p1(userdata_dict):
    data=[]    
    for id_people,fullsalary in userdata_dict.items():
        data.append(id_people)
        data.append(fullsalary)
        queue1.put(data)        
def p2():
    data = queue1.get()
    fullsalary = data[1]
    newdata=UserData.calculator(JiShuL,JiShuH,rate,fullsalary)
            
    newdata = data + newdata
    queue2.get(newdata)
        
def p3(outputfile):
    newdata=queue2.get()
    UserData.dumptofile(outputfile,newdata)        
def main():
    try:
        args=sys.argv[1:]
        arg_c=args.index('-c')
        arg_d=args.index('-d')
        arg_o=args.index('-o')
        configfile=args[arg_c+1]
        userdatafile=args[arg_d+1]
        outputfile=args[arg_o+1]
        print("duwenjianwanle")      
        config=Config(configfile)
        config_dict=config.get_dict
        print(config_dict)
        JiShuL = config.get_JiShuL
        JiShuH = config.get_JiShuH
        rate = config.get_rate
        print(rate)
        userdata=UserData(userdatafile)
        userdata_dict=userdata.get_dict

        
        P1=Process(target=p1,args=userdata_dict)
        P1.start()
        P1.join() 
        P2=Process(target=p2)
        P2.start()
        P2.start()
        P3=Process(target=p3,args=outputfile)
        P3.start()
        P3.join()
              
    
    except IOError:
        print("no file")
    except ValueError:
        print("can shu bu dui")    
if __name__ == '__main__':
    print("go")
