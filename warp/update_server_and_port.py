import csv
import re
import sys
import os

# Check if PyYAML is installed, and provide instructions if not
try:
    import yaml
except ImportError:
    print("Error: PyYAML module is not installed. You can install it by running:")
    print("pip install pyyaml")
    sys.exit(1)

# Define file paths
csv_file = r"path_to_csv_file"
yaml_file = r"path_to_yaml_file"

# Check if CSV file exists
if not os.path.exists(csv_file):
    print(f"Error: The CSV file '{csv_file}' does not exist.")
    exit(1)

# Check if YAML file exists
if not os.path.exists(yaml_file):
    print(f"Error: The YAML file '{yaml_file}' does not exist.")
    exit(1)

# Read CSV file
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    data = list(reader)

# Read YAML file
with open(yaml_file, "r", encoding="utf-8") as f:
    yaml_data = yaml.safe_load(f)

# Update YAML data
for i, row in enumerate(data[1:5]):
    ip_port = row[0]
    server, port = ip_port.split(":")
    
    print(f"Processing row {i + 1}: IP: {server}, Port: {port}")
    
    yaml_data["proxies"][i]["server"] = server
    yaml_data["proxies"][i]["port"] = int(port)

# Write back updated and formatted YAML data with emoji encoding
try:
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print("YAML file updated successfully.")
except Exception as e:
    print(f"Error: An error occurred while writing the YAML file: {e}")
