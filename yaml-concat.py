#!/usr/bin/python 

import yaml,os

config_file_path = os.environ.get("CONFIG_FILE")
output_file_path = os.environ.get("OUTPUT_FILE")
head_dict_prefix = os.environ.get("HEAD")

output_file = open(output_file_path, 'a')

if head_dict_prefix is None:
  output_file.write("groups:\n")
else:
  output_file.write(head_dict_prefix)

with open(config_file_path, 'r') as cfg_stream:
  try:
    config = yaml.safe_load(cfg_stream)   
  except yaml.YAMLError as e:
    print(e)

for rulepath in config['rules']:
  with open(rulepath, 'r') as rule_stream:
    try:      
      lines = rule_stream.readlines()
      for line in lines:
        output_file.write(f"  {line}")
    except yaml.YAMLError as e:
      print(e)
