import csv
import re
import yaml

# Read CSV file
csv_file = r"C:\Users\showc\Documents\Workspace\warp-yxip-win\result.csv"
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    data = list(reader)

# Read YAML file
yaml_file = r"C:\Users\showc\.config\clash\profiles\1690985494786.yml"
with open(yaml_file, "r", encoding="utf-8") as f:
    yaml_data = yaml.safe_load(f)

# Update YAML data
for i, row in enumerate(data[1:5]):
    ip_port = row[0]
    server, port = ip_port.split(":")
    
    print(f"Processing row {i + 1}: IP: {server}, Port: {port}")
    
    yaml_data["proxies"][i]["server"] = server
    yaml_data["proxies"][i]["port"] = int(port)

# Write back updated YAML data
with open(yaml_file, "w", encoding="utf-8") as f:
    yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print("YAML file updated successfully.")
