import yaml
f = open('win_powershell_amsi_bypass.yml',encoding="utf-8")
x = yaml.load(f)
print(x['title'])
