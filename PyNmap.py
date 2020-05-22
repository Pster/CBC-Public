#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Zach Prince"
__email__ = 
__date_ = "Spring 2020"
__version__ = "0.0.1"

# LIBRARIES
from datetime import date
import os
import pickle
import json
import subprocess

# SET VARIABLES
my_dir = 'C:\\Users\\Zachary\\Downloads\\123456'
my_pickle = 'C:\\Users\\Zachary\\Downloads\\tmp\\data.pickle'
my_json = 'C:\\Users\\Zachary\\Downloads\\tmp\\data.json'
port_list = ['192.168.1.1:80', '192.168.1.1:23', '192.168.1.1:22']
nmap_path = 'C:\\Program Files (x86)\\Nmap\\nmap.exe'
nmap_network = '192.168.1.15'

def create_directory():   
    if(os.path.isdir(my_dir)) == False:
        try:  
            os.mkdir(my_dir)
            print ("INFO: The directory was created:", my_dir) 
        except OSError:  
            print ("ERROR: Failed to create directory:", my_dir)
    else:
        print ("INFO: The directory already exists:", my_dir) 
        
def create_date_string():
    date_str = date.today().strftime("%m%d%y")
    os.rename(r'C:\\Users\\Zachary\\Downloads\\tmp\\data.json',r'C:\\Users\\Zachary\\Downloads\\tmp\\_'
              +str(date_str) + '.json')
    print("Date String:", date_str)

def write_files():
    # write the pickle file
    with open(my_pickle, 'wb') as fp:
        pickle.dump(port_list, fp)
    fp.close()
    
    # write the json file
    with open(my_json, 'w') as fp:  
        json.dump(port_list, fp)
    fp.close()

def read_files():
    port_list = []
    
    # read the pickle file
    with open (my_pickle, 'rb') as fp:
        port_list = pickle.load(fp)
    fp.close()
    
    print("pickle:", port_list)
    
    port_list = []
    
    # read the json file
    with open(my_json, 'r') as fp:  
        port_list = json.load(fp)
    fp.close()
    
    print("json:", port_list)

def run_nmap():
    nmap_out = subprocess.run([nmap_path, "-o -X", nmap_network], capture_output=True)
    nmap_data = nmap_out.stdout.splitlines()
    fp=open("_52120.json", 'w')
    print(nmap_data, file = fp)
    fp.close()    

create_directory()
run_nmap()
write_files()
read_files()
create_date_string()

