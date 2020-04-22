import yaml

f = open("powershell_malicious_commandlets.yml")

json = yaml.load(f)

messages = json['detection']['keywords']['Message']

w_str = ""

for mess in messages:

    # 三引号表示多行字符串， 
    w_str += '''{ 
              "match_phrase": { 

                "param3": ''' + "\"" + mess + '''\"
              } 
            },\n'''    


print(w_str)

