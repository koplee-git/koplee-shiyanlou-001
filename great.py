import sys

class Config(object):
    def __init__(self,configfile):
        self.config={}
        self.configfile=configfile
        with open(self.configfile,'r') as f:
            for line in f:
                lst=line.strip('\n').strip().split('=')
                self.config[lst[0]]=lst[1]
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
        rate =self.config['YangLao'] + self.config['YiLiao'] +self.config['ShengYu'] +self.config['ShiYe'] +self.config['GongShang']+self.config['GongJiJin']
        return rate 
class UserData(object):
    def __init__(self,userdatafile):
        self.userdata={}
        self.userdatafile=userdatafile
        with open(self.userdatafile,'r') as f:
            for line in f:
                lst=line.strip().strip('\n').split(',')
                self.userdata[lst[0]]=lst[1]
    @property
    def get_dict(self):
        return self.userdata
 
    @staticmethod
    def calculator(JiShuL,JiShuH,rate,fullsalary):
        def calculator_shebao(fullsalary):
            print("ok") 
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
                    print i
                    f.write(str(i))
                if n < 4:
                    f.write(',')
                    n +=1
            f.write('\n')

if __name__ == '__main__':
    try:
        args=sys.argv[1:]
        arg_c=args.index('-c')
        arg_d=args.index('-d')
        arg_o=args.index('-o')
        configfile=args[arg_c+1]
        userdatafile=args[arg_d+1]
        outputfile=args[arg_o+1]
        
        config=Config(configfile)
        config_dict=config.get_dict

        JiShuL = config.get_JiShuL
        JiShuH = config.get_JiShuH
        rate = config.get_rate
        
        userdata=UserData(userdatafile)
        userdata_dict=userdata.get_dict
        
        for id_people,fullsalary in userdata_dict.items():
            lst_3=UserData.calculator(JiShuL,JiShuH,rate,fullsalary)
            lst_3.insert(0,fullsalary)
            lst_3.insert(0,id_people)
            UserData.dumptofile(outputfile,lst_3) 
    except IOError:
        print("no file")
    except ValueError:
        print("can shu bu dui")    
