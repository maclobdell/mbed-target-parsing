import sys
import json
from os.path import join, abspath, dirname
from json import load, dump


###IS THERE A TEST PARSER ALREADY THAT WILL BE EASIER TO GET RESULTS?


# target       | platform_name | test suite          | test case                  | passed | failed | result 


def main():

    test_data_json_file = "C://Users//maclob01//Documents//Projects//TARGET_PARSING//mbed-target-parsing/example_test_report.json"

    with open (test_data_json_file, "r") as f:
        test_data_json_obj = json.loads(f.read()) 
        f.close()

    test_data_json = {}
    
    test_template = { 
        'tests-api-digitalio': 'x', 'tests-api-analogin': 'x', 'tests-api-i2c': 'x', 'tests-api-spi': 'x'
    }
    
    test_data_json["DATE"] = "2018/04/25 21:22"
    test_data_json["MBED-OS-VER"] = "3.8.2"
    
    for target in test_data_json_obj:        
        print target
        target_data = test_data_json_obj[target]
        for test_group in target_data:
            print test_group                    
            test_group_data = target_data[test_group]
            result = test_group_data.get("single_test_result", "none")

            for template_test_group in test_template:
                if test_group == template_test_group:
                    test_template[template_test_group] = result 
        
            #for element in test_group_data:
            #    print element
            
        
        test_data_json[target] = json.dumps(test_template)     

    s = json.dumps(test_data_json)    
    with open (".//test_data_output.json", "w") as f:
        f.write(s)
        f.close()
        
if __name__ == '__main__':
    main()
