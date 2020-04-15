'''
列表大小为22 ,
在字符串前面加上r，表示 对字符串中的转义字符不转义。
'''

rule_1_list = [r'name=\"Command\"; value=\"route print\"', r'name=\"Command\"; value=\"ipconfig /all\"',
               r'name=\"Command\"; value=\"whoami /all /fo list\"', r'name=\"Command\"; value=\"qprocess *\"',
               r'name=\"Command\"; value=\"net start\"', r'name=\"Command\"; value=\"net group \"Domain Admins\" /domain\"',
               r'name=\"Command\"; value=\"net localgroup \"Administrators\"\"', r'name=\"Command\"; value=\"net user\"',
               r'name=\"Command\"; value=\"net user /domain\"', r'name=\"Command\"; value=\"net group \"Domain Computers\" /domain\"',
               r'name=\"Command\"; value=\"net use\"', r'name=\"Command\"; value=\"netstat -ano\"',
               r'name=\"Command\"; value=\"reg query HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ /v EnableLUA\"',
               r'name=\"Command\"; value=\"net use `\\`\\HFDC01\\ADMIN$ /user:shire\\pgustavo W1n1!19\"',
               r'name=\"Command\"; value=\"net use `\\`\\HFDC01\\ADMIN$ /user:shire\\pgustavo W1n1!19\"',
               r'name=\"Command\"; value=\"net use /delete `\\`\\HFDC01\\ADMIN$\"',
               r'name=\"Command\"; value=\"net use `\\`\\HFDC01\\C$ /user:shire\\pgustavo W1n1!19\"',
               r'name=\"Command\"; value=\"net use `\\`\\HFDC01\\C$ /user:shire\\pgustavo W1n1!19\"',
               r'name=\"Command\"; value=\"sc.exe `\\`\\HFDC01 query\"',
               r'name=\"Command\"; value=\"C:\\WINDOWS\\system32\\sc.exe `\\`\\HFDC01 create AdobeUpdater binPath= \"cmd.exe /c `\\`\"C:\\Users\\pgustavo\\AppData\\Roaming\\Adobe\\Flash Player\\autoupdate.vbs`\\`\" \" DisplayName= \"Adobe Flash Updater\" start= auto\"',
               r'name=\"Command\"; value=\"sc.exe `\\`\\HFDC01 qc AdobeUpdater\"',
               r'name=\"Command\"; value=\"sc.exe `\\`\\HFDC01 start AdobeUpdater\"'
               ]

rule_2_list = [r'route print', r'ipconfig /all', r'whoami /all /fo list', r'qprocess *',
               r'net start', r'net group \"Domain Admins\" /domain', r'net localgroup \"Administrators\"',
               r'net user', r'net user /domain', r'net group \"Domain Computers\" /domain',
               r'net use', r'netstat -ano',
               r'reg query HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ /v EnableLUA',
               r'net use `\\`\\HFDC01\\ADMIN$ /user:shire\\pgustavo W1n1!19',
               r'net use `\\`\\HFDC01\\ADMIN$ /user:shire\\pgustavo W1n1!19',
               r'net use /delete `\\`\\HFDC01\\ADMIN$',
               r'net use `\\`\\HFDC01\\C$ /user:shire\\pgustavo W1n1!19',
               r'net use `\\`\\HFDC01\\C$ /user:shire\\pgustavo W1n1!19',
               r'sc.exe `\\`\\HFDC01 query',
               r'C:\\WINDOWS\\system32\\sc.exe `\\`\\HFDC01 create AdobeUpdater binPath= \"cmd.exe /c `\\`\"C:\\Users\\pgustavo\\AppData\\Roaming\\Adobe\\Flash Player\\autoupdate.vbs`\\`\" \" DisplayName= \"Adobe Flash Updater\" start= auto',
               r'sc.exe `\\`\\HFDC01 qc AdobeUpdater',
               r'sc.exe `\\`\\HFDC01 start AdobeUpdater'
               ]

rule_3_list = [r'*\\\\ROUTE.EXE\" print', r'*\\\\ipconfig.exe\" /all',
               r'*\\\\whoami.exe\" /all /fo list', r'*\\\\qprocess.exe\" *',
               r'*\\\\net.exe\" start', r'net.exe\" group \"Domain Admins\" /domain',
               r'net.exe\" localgroup Administrators', r'*\\\\net.exe\" user',
               r'*\\\\net.exe\" user /domain', r'*\\\\net.exe\" group \"Domain Computers\" /domain',
               r'*\\\\net.exe\" use', r'*\\\\NETSTAT.EXE\" -ano',
               r'*\\\\reg.exe\" query', r'*\\\\net.exe\" use \\\\HFDC01\\ADMIN$ /user:shire\\pgustavo W1n1!19',
               r'*\\\\net.exe\" use \\\\HFDC01\\ADMIN$ /user:shire\\pgustavo W1n1!19',
               r'*\\\\net.exe\" use /delete \\\\HFDC01\\ADMIN$',
               r'*\\\\net.exe\" use \\\\HFDC01\\C$ /user:shire\\pgustavo W1n1!19',
               r'*\\\\net.exe\" use \\\\HFDC01\\C$ /user:shire\\pgustavo W1n1!19',
               r'*\\\\sc.exe\" \\\\HFDC01 query', r'*\\\\sc.exe\" \\\\HFDC01 create',
               r'*\\\\sc.exe\" \\\\HFDC01 qc', r'*\\\\sc.exe\" \\\\HFDC01 start'
               ]

tactic_list = ['Discovery', 'Discovery', 'Discovery', 'Discovery', 'Discovery', 'Discovery', 'Discovery', 'Discovery',
               'Discovery', 'Discovery', 'Discovery', 'Discovery',  'Discovery', 'Lateral Movement', 'Lateral Movement',
               'Defense Evasion', 'Lateral Movement', 'Lateral Movement',  'Discovery', 'Privilege Escalation',
               'Discovery', 'Execution']

technique_id_list = ['T1016', 'T1016', 'T1033', 'T1057', 'T1007', 'T1069', 'T1069', 'T1087', 'T1087', 'T1018', 'T1049', 'T1049',
                'T1012', 'T1078', 'T1077', 'T1126', 'T1078', 'T1077', 'T1007', 'T1050', 'T1007', 'T1035']
technique_list = ['System Network Configuration Discovery', 'System Network Configuration Discovery',
                  'System Owner/User Discovery', 'Process Discovery', 'System Service Discovery', 'Permission Groups Discovery',
                  'Permission Groups Discovery', 'Account Discovery', 'Account Discovery', 'Remote System Discovery',
                  'System Network Connections Discovery','System Network Connections Discovery', 'Query Registry', 'Valid Accounts',
                  'Windows Admin Shares', 'Network Share Connection Removal','Valid Accounts', 'Windows Admin Shares',
                  'System Service Discovery', 'New Service', 'System Service Discovery','Service Execution']

eval_phase_list = ['Initial Discovery', 'Initial Discovery', 'Initial Discovery', 'Initial Discovery', 'Initial Discovery',
                   'Initial Discovery', 'Initial Discovery', 'Initial Discovery', 'Initial Discovery',
                   'Discovery for Lateral Movement', 'Discovery for Lateral Movement', 'Discovery for Lateral Movement', 'Discovery for Lateral Movement',
                   'Lateral Movement', 'Lateral Movement', 'Lateral Movement', 'Lateral Movement', 'Lateral Movement',
                   'Lateral Movement', 'Lateral Movement', 'Lateral Movement', 'Lateral Movement']
eval_step_list= ['12.A.1', '12.A.2', '12.B.1', '12.C.1', '12.D.1', '12.F.1', '12.F.2', '12.G.1', '12.G.2', '13.A.1',
                 '13.B.1', '13.B.2', '13.C.1', '16.B.1', '16.B.1', '16.C.1', '16.D.1', '16.D.1', '16.H.1', '16.I.1', '16.J.1', '16.L.1']

# print(len(rule_1_list))
# print((len(rule_2_list)))
# print(len(tactic_list))
# print(len(technique_id_list))
# print(len(technique_list))
# print(len(eval_phase_list))
# print(len(eval_step_list))

