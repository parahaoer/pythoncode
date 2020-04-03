'''
列表大小为22 ,
在字符串前面加上r，表示 对字符串中的转义字符不转义。
'''


rule_3_list = ["AD Group Memberships", "Password Last Changed", "Last 5 Files Opened", "Interesting Files", "Clipboard Contents"
               ]

tactic_list = ["Discovery", "Discovery", "Discovery", "Discovery", "Discovery"]

technique_id_list = ["T1069", "T1201", "T1083", "T1083", "T1115"]
technique_list = ["Permission Groups Discovery", "Password Policy Discovery", "File and Directory Discovery",
                  "File and Directory Discovery", "Clipboard Data"]

eval_phase_list = ["Initial Discovery", "Initial Discovery", "Initial Discovery", "Initial Discovery", "Initial Discovery"]

eval_step_list= ["12.E.1.2", "12.E.1.3", "12.E.1.4.1", "12.E.1.4.2", "12.E.1.5"]

# print(len(rule_1_list))
# print((len(rule_2_list)))
# print(len(tactic_list))
# print(len(technique_id_list))
# print(len(technique_list))
# print(len(eval_phase_list))
# print(len(eval_step_list))

