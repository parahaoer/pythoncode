import yaml

f = open("sysmon_wmi_susp_scripting.yml")

json = yaml.load(f)

messages = json['detection']['selection']['Destination']

w_str = ""

for mess in messages:

    # 三引号表示多行字符串， 
    w_str += '''{ 
              "match_phrase": { 

                "wmi_consumer_destination": ''' + "\"" + mess + '''\"
              } 
            },\n'''    


print(w_str)

