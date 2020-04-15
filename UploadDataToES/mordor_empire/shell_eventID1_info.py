'''
列表大小为22 ,
在字符串前面加上r，表示 对字符串中的转义字符不转义。
'''


rule_3_list = ["reg.exe\" query \"hkey_local_machine\\system\\currentcontrolset\\control\\terminal server\"",
                "takeown.exe\" /f", "*\\\\icacls.exe\" *\\magnify.exe /grant SYSTEM:F"
               ]

tactic_list = ["Discovery", "Defense Evasion", "Defense Evasion"]

technique_id_list = ["T1007", "T1222", "T1222"]
technique_list = ["System Service Discovery", "File Permissions Modification", "File Permissions Modification"]

eval_phase_list = ["Persistence", "Persistence", "Persistence"]

eval_step_list= ['17.A.1', '17.B.1', '17.B.2']

# print(len(rule_1_list))
# print((len(rule_2_list)))
# print(len(tactic_list))
# print(len(technique_id_list))
# print(len(technique_list))
# print(len(eval_phase_list))
# print(len(eval_step_list))

