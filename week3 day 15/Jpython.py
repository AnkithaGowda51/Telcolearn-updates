# import json 

# with open("titanic.json") as f:
#     data = json.load(f)
        
# print(data["passengers"])  
     


# import json 

# with open("Jsonp.json") as f:
#     data = json.load(f)
       
# print(data[0]["_source"])




# import yaml

# with open("git.yaml") as f:
#     data = yaml.safe_load(f)
       
# print(data["services"]["oai-amf"]["image"])




# import yaml

# with open("git.yaml") as f:
#     data = yaml.safe_load(f)
       
# print(data["services"])

#(mcc mnc file)
# import yaml

# # 1. Load the file
# with open("git.yaml") as f:
#     data = yaml.safe_load(f)

# # 2. Extract the 'environment' list (which causes the error)
# # It currently looks like: ['MCC=208', 'MNC=93', ...]
# list = data["services"]["oai-amf"]["environment"]

# # 3. CONVERT the list to a dictionary
# # This splits "MCC=208" into Key: "MCC" and Value: "208"
# dict = {}
# for item in list:
#     # Use split to separate Key and Value
#     if "=" in item:
#         key, value = item.split("=", 1)
#         dict[key] = value

# # 4. NOW your original requested syntax works using the new 'dict' variable
# print("MCC:", dict["MCC"])
# print("MNC:", dict["MNC"])

#(network ip)
# import yaml

# with open("git.yaml") as f:
#     data = yaml.safe_load(f)

# env_list = data["services"]["oai-amf"]["environment"]

# for item in env_list:
#     if "=" in item and item.count('.') == 3:
#         print(item.replace('=', ': '))



#list all the service port and remove duplicates

import yaml

with open("git.yaml") as f:
    data = yaml.safe_load(f)

# Loop through every service
for service, config in data["services"].items():
    
    # Loop through the environment list (use [] if missing)
    for item in config.get("environment", []):
        
        # Check if line contains "PORT" and is a valid assignment
        if "PORT" in item and "=" in item:
            # Print format: [Service] Key: Value
            print(f"[{service}]", item.replace('=', ': '))