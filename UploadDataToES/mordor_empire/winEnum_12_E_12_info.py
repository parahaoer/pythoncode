'''
列表大小为22 ,
在字符串前面加上r，表示 对字符串中的转义字符不转义。
'''


rule_3_list = ["$Lastupdate = Get-HotFix", "WIN32_OperATiNgSYstEm", "ServiceStatus = (Get-service | where-object { $_.DisplayName -eq $ServiceName}).status",
                "win32_share", "Antivirusproduct", "$FirewallRule", "win32_networkadapterconfiguration",
                "NetConnectionStatus"
               ]

tactic_list = ["Discovery", "Discovery", "Discovery", "Discovery", "Discovery", "Discovery", "Discovery", "Discovery"]

technique_id_list = ["T1082", "T1012", "T1007", "T1135", "T1063", "T1063", "T1016", "T1049"]
technique_list = ["System Information Discovery", "Query Registry", "System Service Discovery",
                  "Network Share Discovery", "Security Software Discovery", "Security Software Discovery",
                  "System Network Configuration Discovery", "System Network Connections Discovery"]

eval_phase_list = ["Initial Discovery", "Initial Discovery", "Initial Discovery", "Initial Discovery", "Initial Discovery",
                   "Initial Discovery", "Initial Discovery", "Initial Discovery"]

eval_step_list= ["12.E.1.6.2", "12.E.1.7", "12.E.1.8", "12.E.1.9.1", "12.E.1.10.1", "12.E.1.10.2", "12.E.1.11", "12.E.1.12"]


# print((len(rule_3_list)))
# print(len(tactic_list))
# print(len(technique_id_list))
# print(len(technique_list))
# print(len(eval_phase_list))
# print(len(eval_step_list))

