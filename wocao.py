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
                lst=line.strip().strip('\n').split(',')
                self.userdata[lst[0]]=lst[1]
    @property
    def get_dict(self):
        return self.userdata
    @staticmethod
    def calculator(JiShuL,JiShuH,rate,fullsalary):
        try:
            if float(fullsalary) < float(JiShuL):
                 getsalary=fullsalary
                 fullsalary = JiShuL
            elif float(fullsalary) > float(JiShuH):
                 print "ok"
                 getsalary=fullsalary
                 fullsalary = JiShuH
            else:
                 getsalary=fullsalary
                
            insurance =float(fullsalary)*float(rate)
            if int(getsalary) <=3500:
                salary = 0
            else:
                salary = int(getsalary) - 3500 -int(insurance)
                print(salary)
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
            realsalary = float(getsalary) - float(insurance) - float(newsurance)
            salarylst=[]
            salarylst.append(insurance) 
            salarylst.append(newsurance) 
            salarylst.append(realsalary) 
            return salarylst
        except:
            print 'error'
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

        JiShuL=config_dict['JiShuL']
        JiShuH=config_dict['JiShuH']
        rate = 0.00
        for value in config_dict.values():
            if float(value)< 1:
                rate += float(value)
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
