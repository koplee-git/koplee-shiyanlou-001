#!/usr/bin/env python3
import ConfigParser
import sys
class Read_Config(object):
    def __init__(self,config_file):
        self.config_file = config_file
        conf = ConfigParser.ConfigParser()
        conf.read(self.config_file)
        sections = conf.sections()
    @property
    def read_city(self,opt_city):
        options=conf.options(opt_city)
        return kvs=conf.items()
def __main__():
    try:
        opts, args = getopt.getopt(sys.argv[1:],'hCcdo',['help'])
        for opt,arg in opts:
             if opt in ('C',):
             opt=opt.strip('[').strip(']')
             config_file = opt
             read_config = Read_Config(confile_file)
             argslst = read_config.read_city
        for opt,arg in opts:


             if opt in ('h','help'):
                 print("")
             if opt in ('c',):
                 config_file = 
                 read_config(config_file)
             if opt in ('d',):
                 pass
             if opt in ('o'):
                 pass
     except getopt.GetoptError:
        print("")
