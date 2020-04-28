'''
列表大小为22 ,
在字符串前面加上r，表示 对字符串中的转义字符不转义。
'''

rule_1_list = ['ParameterBinding(Set-Content): name=\"Path\"; value=\"autoupdate.vbs\"',
               'ParameterBinding(Set-Content): name=\"Path\"; value=\"recycler.exe\"',
               'ParameterBinding(Set-Content): name=\"Path\"; value=\"ftp.txt\"'
               ]

rule_3_list = ['autoupdate.vbs', 'recycler.exe', 'ftp.txt'
               ]

tactic_list = ['Lateral Movemet', 'Defense Evasion', 'Exfiltration']

technique_id_list = ['T1105', 'T1105', 'T1048']
technique_list = ['Remote File Copy', 'Remote File Copy', 'Exfiltration Over Alternative Protocol']

eval_phase_list = ['Lateral Movemet', 'Exfiltration', 'Exfiltration']
eval_step_list= ['16.E.1', '19.A', '19.C.1']

# print(len(rule_1_list))
# print((len(rule_2_list)))
# print(len(tactic_list))
# print(len(technique_id_list))
# print(len(technique_list))
# print(len(eval_phase_list))
# print(len(eval_step_list))

