

str = '/home/atomic-threat-coverage/detection_rules/sigma/rules/windows/powershell/powershell_downgrade_attack.yml'

filename = str.split('/')[-1]

print(filename)

print(filename[:-4])