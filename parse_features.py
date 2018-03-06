#!/usr/bin/python

import urllib, json, sys
import markdown
from tabulate import tabulate

targets_json_url = "https://raw.githubusercontent.com/ARMmbed/mbed-os/master/targets/targets.json"

def main():
    _targets = []
    _device_has = []
    _inherits = []
    response = urllib.urlopen(targets_json_url)
    targets_json_data = json.loads(response.read())
    # print targets_json_data

    for target_name in targets_json_data:
        target_data = targets_json_data[target_name]
        # print("The target_name is {}".format(target_name))
        _targets.append(target_name)
        if 'device_has' in target_data:
            has = target_data.get('device_has')
            for feature in has:
                # print("The feature is {}".format(feature))
                _device_has.append(feature)
        if 'inherits' in target_data:
            parents = target_data.get('inherits')
            for parent in parents:
                # print("The parent is {}".format(parent))
                _inherits.append(parent)
        # sys.exit()

    _inherits.sort()
    inherits = set(_inherits)
    
    _device_has.sort()
    device_has = set(_device_has)

    _targets.sort()
    targets = set(_targets)

    print('Sorted list targets:', targets)
    print('Sorted list device_has:', device_has)
    print('Sorted list inherits:', inherits)

    markdown_file = open('TARGETS.md','w')
    for item in inherits:
        markdown_file.write("* %s\n" % item)
    markdown_file.close()    

if __name__ == '__main__':
    main()
