import json

from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('LogAnalitic.xlsx')
wb = copy(rb)

i=0
for line in open(r'covenant_dcsync_all_2019-10-27064128.json'):
    d = json.loads(line)
    timestamp = d['@timestamp']
    computer_name = d['winlog']['computer_name']

    provider_name = d['winlog']['provider_name']
    event_id = d['winlog']['event_id']
    log_type = ''
    if(provider_name == 'Microsoft-Windows-Security-Auditing'):
        log_type = 'Security ' + str(event_id)
    elif(provider_name == 'Microsoft-Windows-Sysmon'):
        log_type = 'Sysmon ' + str(event_id)
    task = d['winlog']['task']

    source = ''
    target = ''
    application = ''
    event_data = d['winlog']['event_data']
    if(task == 'Process accessed (rule: ProcessAccess)') :
        source = event_data['SourceImage']
        target = event_data['TargetImage']
    elif(task == 'RawAccessRead detected (rule: RawAccessRead)') :
        source = event_data['Image']
        target = event_data['Device']
    elif(task == 'Filtering Platform Connection'):
        source = event_data['SourceAddress']
        target = event_data['DestAddress'] if event_id == 5156 else  ''
        application = event_data['Application']
    elif (task == 'File created (rule: FileCreate)'):
        source = event_data['Image']
        target = event_data['TargetFilename']
    elif (task == 'Network connection detected (rule: NetworkConnect)'):
        source = event_data['SourceHostname']
        target = event_data['DestinationIp']
        application =event_data['Image']
    elif (task == 'Token Right Adjusted Events'):
        source = event_data['SubjectUserName']
        target = event_data['TargetUserName']
        application = event_data['ProcessName']
    elif (task == 'Image loaded (rule: ImageLoad)'):
        source = event_data['Image']
        target = event_data['ImageLoaded']
    elif (task == 'Special Logon'):
        source = event_data['SubjectUserName']
    elif (task == 'Logon'):
        source = event_data['SubjectUserName']
        target = event_data['TargetUserName']
        application = event_data['LogonProcessName']
    elif (task == 'Group Membership'):
        source = event_data['SubjectUserName']
        target = event_data['TargetUserName']
    elif (task == 'File Share'):
        source = event_data['SubjectUserName']
    elif (task == 'Detailed File Share'):
        source = event_data['SubjectUserName']
        target = event_data['RelativeTargetName']
    elif (task == 'Directory Service Access'):
        source = event_data['SubjectUserName']
        target = event_data['ObjectName']
    elif (task == 'Pipe Connected (rule: PipeEvent)'):
        source = event_data['Image']
        target = event_data['PipeName']
    elif (task == 'File created (rule: FileCreate)'):
        source = event_data['Image']
        target = event_data['TargetFilename']
    elif (task == 'Logoff'):
        source = event_data['TargetUserName']


    wb.get_sheet(0).write(i+1, 0, i)
    wb.get_sheet(0).write(i+1, 1, timestamp)
    wb.get_sheet(0).write(i+1, 2, computer_name)
    wb.get_sheet(0).write(i + 1, 3, log_type)
    wb.get_sheet(0).write(i + 1, 4, task)
    wb.get_sheet(0).write(i + 1, 5, source)
    wb.get_sheet(0).write(i + 1, 6, target)
    wb.get_sheet(0).write(i + 1, 7, application)
    wb.save('output.xls')
    i = i + 1

print(i)