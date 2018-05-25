# mbed-target-parsing
Parse targets.json from mbed-os to generate markdown and unique lists

A new script has been added to get 'device_has' data (describes what features are enabled) in Mbed OS targets.json file, and create a json structure.

The format is intended to be kept compatible with the platform scorecard server project https://github.com/maclobdell/platform_scorecard_server.


# Install requirements
```
pip install -r requirements.txt
```

# Generate Markdown
```
python parse_features.py
```

#Generate JSON

```
python mbed_target_info.py
```

#TO DO

Migrate everything over to using built in features of the Mbed tools for getting target data.


 
