import sys
import json
from os.path import join, abspath, dirname
from json import load, dump

# Be sure that the tools directory is in the search path
ROOT = "C://Users//maclob01//Documents//mbed-os-5//mbed-os"
sys.path.insert(0, ROOT)

from tools.targets import TARGETS
from tools.targets import set_targets_json_location  #for changing location of targets.json

def main():

    device_data_array = []
    device_has_template = { 
        'FLASH': 'x', 'RTC': 'x', 'SPI': 'x', 'I2C': 'x', 'TRNG': 'x', 'SLEEP': 'x'
    }
    
    set_targets_json_location("C://Users//maclob01//Documents//Projects//TARGET_PARSING//mbed-target-parsing//example_targets.json")


    
    for target in TARGETS:  
        
        #construct an array of targets here
        device_data_entry = {}
               
        device_data_entry["name"] = target.name
        
        device_data_description_array = []
        device_data_description = {}
        
        device_data_description["ver"] = "5.9.1"
        device_data_description["name"] = target.name
        device_data_description["date"] = "May 25, 2018" 
                             
        for feature in target.device_has:
            for template_feature in device_has_template:
                if feature == template_feature:
                    device_has_template[feature] = 'YES' 

        device_data_description["target_data"] = device_has_template
    
           #I'm realizing that it is not practical for there to be an array of 'description' data 
           #   that includes data from multiple versions of mbed os, but that is the way it is now, so going with it.
        device_data_description_array.append(device_data_description)
        
        device_data_entry["description"] = device_data_description_array

        device_data_array.append(device_data_entry)

    s = json.dumps(device_data_array)    
    with open (".//device_data_output.json", "w") as f:
        f.write(s)
        f.close()
        
if __name__ == '__main__':
    main()
