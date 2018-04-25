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

    device_data_json = {}
    
    device_has_template = { 
        'FLASH': 'x', 'RTC': 'x', 'SPI': 'x', 'I2C': 'x', 'TRNG': 'x', 'SLEEP': 'x'
    }
    
    set_targets_json_location("C://Users//maclob01//Documents//Projects//TARGET_PARSING//mbed-target-parsing//example_targets.json")

    device_data_json["DATE"] = "2018/04/25 21:22"
    device_data_json["MBED-OS-VER"] = "3.8.2"
    
    for target in TARGETS:        
        for feature in target.device_has:
            for template_feature in device_has_template:
                if feature == template_feature:
                    device_has_template[feature] = 'YES' 

        device_data_json[target.name] = json.dumps(device_has_template)     

    s = json.dumps(device_data_json)    
    with open (".//device_data_output.json", "w") as f:
        f.write(s)
        f.close()
        
if __name__ == '__main__':
    main()
