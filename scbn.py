import sys 
import json 
def process_inbound_dict():
    RuleType = dict['RuleType']
    
    if RuleType == 'Inbound':
        Port = 443
        true = 'true'
        false = 'false'
        ProfileID = dict['ProfileID']
        Sender = dict['Sender']
        Receiver = dict['Receiver']
        Message = dict['Message']
        ProcessingFlag1 = dict['ProcessingFlag1']
        ProcessingFlag1 = dict['ProcessingFlag1']
        name1_Inbound = Receiver + '_INBOUND_' + Sender + '_SFTP_STEP1'
        name2_Inbound = Receiver + '_INBOUND_' + Sender + '_SFTP_STEP2'
        Return_Name = name1_Inbound + '& SFTP_STEP2 created successfully'
        id_name = Receiver + '_INBOUND_' + Sender
        data_inbound = {
            '_id': id_name,
            'host': 'eubpnsupporttool.sci.local',
            'port': Port,
            'outputFolder': 'P:\\RPA\\BPNST',
            'disableAll': true,
            'checkForDuplicateRules': true,
            'skipRules': [],
            'rules': [{
                'name': name1_Inbound,
                'businessAlias': 'OSC_DEMO',
                'ruleBusinessAlias': 'OSC_DEMO',
                'ruleSet': 'BPN_ReceiveSFTPEval',
                'enabled': true,
                'default': false,
                'direction': 'INBOUND',
                'conditions': [{'name': 'SourceSubject',
                               'operator': 'Contains',
                               'value': ProfileID}],
                'actions': [{
                    'name': 'TrackIt',
                    'businessProcessName': 'BPN_ReceiveSFTPTrack',
                    'enabled': true,
                    'assignments': [{'name': 'InflightDirection',
                                    'value': 'INBOUND'}],
                    }, {
                    'name': 'SendToPod',
                    'businessProcessName': 'BPN_SendPod',
                    'enabled': true,
                    'assignments': [
                        {'name': 'InflightDirection', 'value': 'INBOUND'
                         },
                        {'name': 'SourceSenderID', 'value': Sender},
                        {'name': 'Action', 'value': 'ROUTER'},
                        {'name': 'ProcessingFlag1',
                         'value': ProcessingFlag1},
                        {'name': 'MessageType', 'value': Message},
                        {'name': 'BusinessAlias', 'value': 'OSC_DEMO'},
                        {'name': 'TargetSystemID', 'value': 'TX01'},
                        {'name': 'SourceReceiverID',
                         'value': Receiver},
                        ],
                    }],
                }, {
                'name': name2_Inbound,
                'businessAlias': 'OSC_DEMO',
                'ruleBusinessAlias': 'OSC_DEMO',
                'ruleSet': 'BPN_RouterEval',
                'enabled': true,
                'default': false,
                'direction': '',
                'conditions': [{'name': 'Receiver', 'operator': '=',
                               'value': Receiver}],
                'actions': [{
                    'name': 'SendToPod',
                    'businessProcessName': 'BPN_Finish',
                    'enabled': true,
                    'assignments': [],
                    }],
                }],
            }
        message ="Rule created successfully"
        return {"rule_message:":message}

def process_outbound_dict():
    RuleType = dict['RuleType']
    Port = 443
    true = 'true'
    false = 'false'
    if RuleType == 'Outbound':
        ProfileID_outbound = dict['ProfileID_outbound']
        Sender_outbound = dict['Sender_outbound']
        Receiver_outbound = dict['Receiver_outbound']
        Message_outbound = dict['Message_outbound']
        ProcessingFlag1_outbound = dict['ProcessingFlag1_outbound']
        Filename_output = dict['Filename_output']
        name1_Outbound = Receiver_outbound + '_Outbound_' \
            + Sender_outbound + '_SFTP_STEP1'
        name2_Outbound = Receiver_outbound + '_Outbound_' \
            + Sender_outbound + '_SFTP_STEP1'
        id_name = Receiver_outbound + '_Outbound_' + Sender_outbound
        # data = ProfileID_outbound + Sender_outbound + Receiver_outbound + Message_outbound + ProcessingFlag1_outbound + Filename_output
        Return_Name = name1_Outbound + '& SFTP_STEP2 created successfully'
        data_outbound = {
            '_id': id_name,
            'host': 'eubpnsupporttool.sci.local',
            'port': Port,
            'outputFolder': 'P:\\RPA\\BPNST',
            'disableAll': true,
            'checkForDuplicateRules': true,
            'skipRules': [],
            'rules': [{
                'name': name1_Outbound,
                'businessAlias': 'OSC_DEMO',
                'ruleBusinessAlias': 'OSC_DEMO',
                'ruleSet': 'BPN_ReceiveSFTPEval',
                'enabled': true,
                'default': false,
                'direction': 'OUTBOUND',
                'conditions': [{'name': 'SourceFileName',
                               'operator': 'StartsWith',
                               'value': Filename_output},
                               {'name': 'SourceSubject',
                               'operator': 'Contains',
                               'value': ProfileID_outbound}],
                'actions': [{
                    'name': 'TrackIt',
                    'businessProcessName': 'BPN_ReceiveSFTPTrack',
                    'enabled': true,
                    'assignments': [{'name': 'InflightDirection',
                                    'value': 'OUTBOUND'}],
                    }, {
                    'name': 'SendToPod',
                    'businessProcessName': 'BPN_SendPod',
                    'enabled': true,
                    'assignments': [
                        {'name': 'InflightDirection',
                         'value': 'OUTBOUND'},
                        {'name': 'SourceSenderID',
                         'value': Receiver_outbound},
                        {'name': 'Action', 'value': 'ROUTER'},
                        {'name': 'ProcessingFlag1',
                         'value': ProcessingFlag1_outbound},
                        {'name': 'MessageType',
                         'value': Message_outbound},
                        {'name': 'BusinessAlias', 'value': 'OSC_DEMO'},
                        {'name': 'TargetSystemID', 'value': 'TX01'},
                        {'name': 'SourceReceiverID',
                         'value': Sender_outbound},
                        ],
                    }],
                }, {
                'name': name2_Outbound,
                'businessAlias': 'OSC_DEMO',
                'ruleBusinessAlias': 'OSC_DEMO',
                'ruleSet': 'BPN_RouterEval',
                'enabled': true,
                'default': false,
                'direction': 'OUTBOUND',
                'conditions': [{'name': 'ProcessingFlag1',
                               'operator': '=',
                               'value': ProcessingFlag1_outbound}],
                'actions': [{
                    'name': 'Action2',
                    'businessProcessName': 'BPN_Finish',
                    'enabled': false,
                    'assignments': [],
                    }, {
                    'name': 'SendToPod',
                    'businessProcessName': 'BPN_SendPod',
                    'enabled': true,
                    'assignments': [
                        {'name': 'Category', 'value': 'SFTP'},
                        {'name': 'Action', 'value': 'SEND'},
                        {'name': 'TargetSystemID', 'value': 'PRO01'},
                        {'name': 'ProtocolProfileID',
                         'value': ProfileID_outbound},
                        {'name': 'InflightDirection',
                         'value': 'OUTBOUND'},
                        {'name': 'BusinessAlias', 'value': 'OSC_DEMO'},
                        ],
                    }],
                }],
            }
        message ="Rule created successfully"
        return {"rule_message:":message}
    
def process_both_dict():
    RuleType = dict['RuleType']
    Port = 443
    true = 'true'
    false = 'false'
    if RuleType == 'Both':
        Inbound_ProfileID_both = dict['Inbound_ProfileID_both']
        Outbound_ProfileID_both = dict['Outbound_ProfileID_both']
        Sender_both = dict['Sender_both']
        Receiver_both = dict['Receiver_both']
        Message_both = dict['Message_both']
        ProcessingFlag1_both = dict['ProcessingFlag1_both']
        ProcessingFlag1_IB = ProcessingFlag1_both + "_IB"
        ProcessingFlag1_OB = ProcessingFlag1_both + "_OB"
        Filename_both = dict['Filename_both']
        name1_Inbound_both = Receiver_both + '_INBOUND_' + Sender_both \
            + '_SFTP_STEP1'
        name2_Inbound_both = Receiver_both + '_INBOUND_' + Sender_both \
            + '_SFTP_STEP2'
        name1_Outbound_both = Receiver_both + '_Outbound_' \
            + Sender_both + '_SFTP_STEP1'
        name2_Outbound_both = Receiver_both + '_Outbound_' \
            + Sender_both + '_SFTP_STEP1'
        id_name =  Receiver_both + '_Both_' + Sender_both
        Return_Name = Receiver_both + 'both' + Sender_both +  'SFTP_STEP1,SFTP_STEP2 created successfully'
        data_both = {
            '_id': id_name,
            'host': 'eubpnsupporttool.sci.local',
            'port': Port,
            'outputFolder': 'P:\\RPA\\BPNST',
            'disableAll': true,
            'checkForDuplicateRules': true,
            'skipRules': [],
            'rules': [{
                'name': name1_Inbound_both,
                'businessAlias': 'OSC_DEMO',
                'ruleBusinessAlias': 'OSC_DEMO',
                'ruleSet': 'BPN_ReceiveSFTPEval',
                'enabled': true,
                'default': false,
                'direction': 'INBOUND',
                'conditions': [{'name': 'SourceSubject',
                               'operator': 'Contains',
                               'value': Inbound_ProfileID_both}],
                'actions': [{
                    'name': 'TrackIt',
                    'businessProcessName': 'BPN_ReceiveSFTPTrack',
                    'enabled': true,
                    'assignments': [{'name': 'InflightDirection',
                                    'value': 'INBOUND'}],
                    }, {
                    'name': 'SendToPod',
                    'businessProcessName': 'BPN_SendPod',
                    'enabled': true,
                    'assignments': [
                        {'name': 'InflightDirection', 'value': 'INBOUND'
                         },
                        {'name': 'SourceSenderID',
                         'value': Sender_both},
                        {'name': 'Action', 'value': 'ROUTER'},
                        {'name': 'ProcessingFlag1',
                         'value': ProcessingFlag1_IB},
                        {'name': 'MessageType', 'value': Message_both},
                        {'name': 'BusinessAlias', 'value': 'OSC_DEMO'},
                        {'name': 'TargetSystemID', 'value': 'TX01'},
                        {'name': 'SourceReceiverID',
                         'value': Receiver_both},
                        ],
                    }],
                }, {
                'name': name2_Inbound_both,
                'businessAlias': 'OSC_DEMO',
                'ruleBusinessAlias': 'OSC_DEMO',
                'ruleSet': 'BPN_RouterEval',
                'enabled': true,
                'default': false,
                'direction': '',
                'conditions': [{'name': 'ProcessingFlag1',
                               'operator': '=',
                               'value': ProcessingFlag1_IB}],
                'actions': [{
                    'name': 'SendToPod',
                    'businessProcessName': 'BPN_Finish',
                    'enabled': true,
                    'assignments': [],
                    }],
                }, {
                'name': name1_Outbound_both,
                'businessAlias': 'OSC_DEMO',
                'ruleBusinessAlias': 'OSC_DEMO',
                'ruleSet': 'BPN_ReceiveSFTPEval',
                'enabled': true,
                'default': false,
                'direction': 'OUTBOUND',
                'conditions': [{'name': 'SourceFileName',
                               'operator': 'StartsWith',
                               'value': Filename_both},
                               {'name': 'SourceSubject',
                               'operator': 'Contains',
                               'value': Outbound_ProfileID_both}],
                'actions': [{
                    'name': 'TrackIt',
                    'businessProcessName': 'BPN_ReceiveSFTPTrack',
                    'enabled': true,
                    'assignments': [{'name': 'InflightDirection',
                                    'value': 'OUTBOUND'}],
                    }, {
                    'name': 'SendToPod',
                    'businessProcessName': 'BPN_SendPod',
                    'enabled': true,
                    'assignments': [
                        {'name': 'InflightDirection',
                         'value': 'OUTBOUND'},
                        {'name': 'SourceSenderID',
                         'value': Sender_both},
                        {'name': 'Action', 'value': 'ROUTER'},
                        {'name': 'ProcessingFlag1',
                         'value': ProcessingFlag1_OB},
                        {'name': 'MessageType', 'value': Message_both},
                        {'name': 'BusinessAlias', 'value': 'OSC_DEMO'},
                        {'name': 'TargetSystemID', 'value': 'TX01'},
                        {'name': 'SourceReceiverID',
                         'value': Receiver_both},
                        ],
                    }],
                }, {
                'name': name2_Outbound_both,
                'businessAlias': 'OSC_DEMO',
                'ruleBusinessAlias': 'OSC_DEMO',
                'ruleSet': 'BPN_RouterEval',
                'enabled': true,
                'default': false,
                'direction': 'OUTBOUND',
                'conditions': [{'name': 'ProcessingFlag1',
                               'operator': '=', 'value': 'ProcessingFlag1_both'
                               }],
                'actions': [{
                    'name': 'Action2',
                    'businessProcessName': 'BPN_Finish',
                    'enabled': false,
                    'assignments': [],
                    }, {
                    'name': 'SendToPod',
                    'businessProcessName': 'BPN_SendPod',
                    'enabled': true,
                    'assignments': [
                        {'name': 'Category', 'value': 'SFTP'},
                        {'name': 'Action', 'value': 'SEND'},
                        {'name': 'TargetSystemID', 'value': 'PRO01'},
                        {'name': 'ProtocolProfileID',
                         'value': Outbound_ProfileID_both},
                        {'name': 'InflightDirection',
                         'value': 'OUTBOUND'},
                        {'name': 'BusinessAlias', 'value': 'OSC_DEMO'},
                        ],
                    }],
                }],
            }
        message ="Rule created successfully"
        return {"rule_message:":message}

    
def process_basictx_inbound_dict():
    RuleType = dict['RuleType']
    Port = 443
    true = 'true'
    false = 'false'
    message= 'Rule created successfully'
    if RuleType == 'Inbound BasicTx':
        tradingpartner_Basictx = dict["tradingpartner_Basictx"]
        Profileid_Basictx = dict["Profileid_Basictx"]
        ProcessingFlag1_Basictx = dict["ProcessingFlag1_Basictx"]
        name1_BasicTx = "1.0.0_ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_Basictx + "_SFTP_TO_BASICTX"
        name2_BasicTx = "1.0.2_ELUX_GENERIC_IN_FLAT_FILE_" + ProcessingFlag1_Basictx + "_BASICTX_TO_CC_FINISH"
        Return_Name = name1_BasicTx + name2_BasicTx + "created successfully"
        id_name = "ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_Basictx
        data_inboundbasictx = {
            "_id": id_name,
            "host": "nabpnsupporttool.comm1.sci.local",
            "port": Port,
            "outputFolder": "P:\\RPA\\BPNST",
            "disableAll": true,
            "checkForDuplicateRules": true,
            "skipRules": [],
            "rules": [
                {
                    "name": name1_BasicTx,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_ReceiveSFTPEval",
                    "enabled": true,
                    "default": false,
                    "direction": "INBOUND",
                    "conditions": [
                        {
                            "name": "SourceSubject",
                            "operator": "Contains",
                            "value": Profileid_Basictx,
                        }
                    ],
                    "actions": [
                        {
                            "name": "TrackIt",
                            "businessProcessName": "BPN_ReceiveSFTPTrack",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"}
                            ],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"},
                                {"name": "Action", "value": "TX"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1_Basictx},
                                {"name": "Category", "value": "BASIC"},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                                {"name": "TargetSystemID", "value": "TX01"},
                                {
                                    "name": "MapName",
                                    "value": "ELUX_DUMMY_PASSTHRU_Fortras100_inhouse",
                                },
                            ],
                        },
                    ],
                },
                {
                    "name": name2_BasicTx,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_BasicTranslationEval",
                    "enabled": true,
                    "default": false,
                    "direction": "",
                    "conditions": [
                        {
                            "name": "ProcessingFlag1",
                            "operator": "=",
                            "value": ProcessingFlag1_Basictx,
                        }
                    ],
                    "actions": [
                        {
                            "name": "Action2",
                            "businessProcessName": "BPN_CarbonCopy",
                            "enabled": true,
                            "assignments": [
                                {"name": "CCv1Mode", "value": "TRUE"},
                                {"name": "CarbonCopyRecipient", "value": "OSC_DEMO"},
                                {"name": "CCNodesToKeep", "value": "SourceFileName"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1_Basictx},
                            ],
                        },
                        {
                            "name": "Action3",
                            "businessProcessName": "BPN_Finish",
                            "enabled": true,
                            "assignments": [],
                        },
                    ],
                },
            ],
        }
    return {'message':message}


def process_basictx_outbound_dict():
    RuleType = dict['RuleType']
    Port = 443
    true = 'true'
    false = 'false'  
    message='Rule created successfully'
    if RuleType == 'Outbound BasicTx':
        tradingpartner_Basictx = dict["tradingpartner_Basictx"]
        Profileid_Basictx = dict["Profileid_Basictx"]
        ProcessingFlag1_Basictx = dict["ProcessingFlag1_Basictx"]
        name1_BasicTx = "1.0.0_ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_Basictx + "_SFTP_TO_BASICTX"
        name2_BasicTx = "1.0.2_ELUX_GENERIC_IN_FLAT_FILE_" + ProcessingFlag1_Basictx + "_BASICTX_TO_CC_FINISH"
        Return_Name = name1_BasicTx + name2_BasicTx + "created successfully"
        id_name = "ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_Basictx
        data_outboundbasictx = {
            "_id": id_name,
            "host": "nabpnsupporttool.comm1.sci.local",
            "port": 443,
            "outputFolder": "P:\\RPA\\BPNST",
            "disableAll": true,
            "checkForDuplicateRules": true,
            "skipRules": [],
            "rules": [
                {
                    "name": name1_BasicTx,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_ReceiveSFTPEval",
                    "enabled": true,
                    "default": false,
                    "direction": "INBOUND",
                    "conditions": [
                        {
                            "name": "SourceSubject",
                            "operator": "Contains",
                            "value": Profileid_Basictx,
                        }
                    ],
                    "actions": [
                        {
                            "name": "TrackIt",
                            "businessProcessName": "BPN_ReceiveSFTPTrack",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"}
                            ],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"},
                                {"name": "Action", "value": "TX"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1_Basictx},
                                {"name": "Category", "value": "BASIC"},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                                {"name": "TargetSystemID", "value": "TX01"},
                                {
                                    "name": "MapName",
                                    "value": "ELUX_DUMMY_PASSTHRU_Fortras100_inhouse",
                                },
                            ],
                        },
                    ],
                },
                {
                    "name": name2_BasicTx,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_BasicTranslationEval",
                    "enabled": true,
                    "default": false,
                    "direction": "",
                    "conditions": [
                        {
                            "name": "ProcessingFlag1",
                            "operator": "=",
                            "value": ProcessingFlag1_Basictx,
                        }
                    ],
                    "actions": [
                        {
                            "name": "Action2",
                            "businessProcessName": "BPN_CarbonCopy",
                            "enabled": true,
                            "assignments": [
                                {"name": "CCv1Mode", "value": "TRUE"},
                                {"name": "CarbonCopyRecipient", "value": "OSC_DEMO"},
                                {"name": "CCNodesToKeep", "value": "SourceFileName"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1_Basictx},
                            ],
                        },
                        {
                            "name": "Action3",
                            "businessProcessName": "BPN_Finish",
                            "enabled": true,
                            "assignments": [],
                        },
                    ],
                },
            ],
        }
      
 
        return {"rule_message:":message}

def process_rule_edit():
    
    RuleType = dict['RuleType']
      
    if RuleType == "Rule edit" :
        ruleName = dict["ruleName"]
        data = "Rule is there " + ruleName
        selector = {"_id": ruleName}
        
    return{"message":ruleName}
 
        
def process_edit_inbound():
    RuleType = dict['RuleType']
    Port = 443
    true = 'true'
    false = 'false'
    message = 'Rule Edited Successfully'
    if RuleType == "Edit Inbound Rule":
        ruleName = dict['ruleName']
        
        Message= dict['Message']
        ProfileID = dict['ProfileID']
        ProcessingFlag1 = dict['ProcessingFlag1']
        my_list = ruleName.split("_")
        Receiver = my_list[0]
        Sender = my_list[2]
        Return_Name = 'Rule Edit Successfully'

        name1_Inbound = Receiver + "_INBOUND_" + Sender + "_SFTP_STEP1"
        name2_Inbound = Receiver + "_INBOUND_" + Sender + "_SFTP_STEP2"
        id_name = Receiver + "_INBOUND_" + Sender
        Return_Name = 'Rule Edit Successfully'
        data_edit_inbound = {
            "_id": id_name,
            "host": "eubpnsupporttool.sci.local",
            "port": Port,
            "outputFolder": "P:\\RPA\\BPNST",
            "disableAll": true,
            "checkForDuplicateRules": true,
            "skipRules": [],
            "rules": [
                {
                    "name": name1_Inbound,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_ReceiveSFTPEval",
                    "enabled": true,
                    "default": false,
                    "direction": "INBOUND",
                    "conditions": [
                        {
                            "name": "SourceSubject",
                            "operator": "Contains",
                            "value": ProfileID,
                        }
                    ],
                    "actions": [
                        {
                            "name": "TrackIt",
                            "businessProcessName": "BPN_ReceiveSFTPTrack",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"}
                            ],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"},
                                {"name": "SourceSenderID", "value": Sender},
                                {"name": "Action", "value": "ROUTER"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1},
                                {"name": "MessageType", "value": Message},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                                {"name": "TargetSystemID", "value": "TX01"},
                                {"name": "SourceReceiverID", "value": Receiver},
                            ],
                        },
                    ],
                },
                {
                    "name": name2_Inbound,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_RouterEval",
                    "enabled": true,
                    "default": false,
                    "direction": "",
                    "conditions": [
                        {"name": "Receiver", "operator": "=", "value": Receiver}
                    ],
                    "actions": [
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_Finish",
                            "enabled": true,
                            "assignments": [],
                        }
                    ],
                },
            ],
        }
        return {"message": message}

def process_edit_outbound():
    RuleType = dict['RuleType']
    Port = 443
    true = 'true'
    false = 'false'
    message = 'Rule Edited Successfully'
    if RuleType == "Edit Outbound Rule":
        ruleName= dict['ruleName']
        Keyword = dict['Keyword']
        my_list = ruleName.split('_')
        Sender_outbound = my_list[2]
        Receiver_outbound = my_list[0]
        ProfileID_outbound = dict['ProfileID_outbound']
        Message_outbound = dict['Message_outbound']
        ProcessingFlag1_outbound = dict['ProcessingFlag1_outbound']
        Filename_output = dict['Filename_output']
        name1_Outbound = Receiver_outbound + "_Outbound_" + Sender_outbound + "_SFTP_STEP1"

        name2_Outbound = Receiver_outbound + "_Outbound_" + Sender_outbound + "_SFTP_STEP2"

        id_name = Receiver_outbound + "_Outbound_" + Sender_outbound
        data = id_name
        Return_Name = 'Rule Edit Successfully'

        data_edit_outbound  = {
            "_id": id_name,
            "host": "eubpnsupporttool.sci.local",
            "port": Port,
            "outputFolder": "P:\\RPA\\BPNST",
            "disableAll": true,
            "checkForDuplicateRules": true,
            "skipRules": [],
            "rules": [
                {
                    "name": name1_Outbound,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_ReceiveSFTPEval",
                    "enabled": true,
                    "default": false,
                    "direction": "OUTBOUND",
                    "conditions": [
                        {
                            "name": "SourceFileName",
                            "operator": "StartsWith",
                            "value": Filename_output,
                        },
                        {
                            "name": "SourceSubject",
                            "operator": "Contains",
                            "value": ProfileID_outbound,
                        },
                    ],
                    "actions": [
                        {
                            "name": "TrackIt",
                            "businessProcessName": "BPN_ReceiveSFTPTrack",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "OUTBOUND"}
                            ],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "OUTBOUND"},
                                {
                                    "name": "SourceSenderID",
                                    "value": Receiver_outbound,
                                },
                                {"name": "Action", "value": "ROUTER"},
                                {
                                    "name": "ProcessingFlag1",
                                    "value": ProcessingFlag1_outbound,
                                },
                                {"name": "MessageType", "value": Message_outbound},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                                {"name": "TargetSystemID", "value": "TX01"},
                                {
                                    "name": "SourceReceiverID",
                                    "value": Sender_outbound,
                                },
                            ],
                        },
                    ],
                },
                {
                    "name": name2_Outbound,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_RouterEval",
                    "enabled": true,
                    "default": false,
                    "direction": "OUTBOUND",
                    "conditions": [
                        {
                            "name": "ProcessingFlag1",
                            "operator": "=",
                            "value": ProcessingFlag1_outbound,
                        }
                    ],
                    "actions": [
                        {
                            "name": "Action2",
                            "businessProcessName": "BPN_Finish",
                            "enabled": false,
                            "assignments": [],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "Category", "value": "SFTP"},
                                {"name": "Action", "value": "SEND"},
                                {"name": "TargetSystemID", "value": "PRO01"},
                                {
                                    "name": "ProtocolProfileID",
                                    "value": ProfileID_outbound,
                                },
                                {"name": "InflightDirection", "value": "OUTBOUND"},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                            ],
                        },
                    ],
                },
            ],
        }

        return {"message":message}

def process_edit_both():
    RuleType = dict['RuleType']
    
    if RuleType == "Edit Both Rule":
        ruleName = dict["ruleName"]
        Port = 443
        true = 'true'
        false = 'false'
        message = 'Rule Edited Successfully'
        my_list = ruleName.split('_')
        Sender_both = my_list[2]
        Receiver_both = my_list[0]

        Inbound_ProfileID_both = dict['Inbound_ProfileID_both']
        Outbound_ProfileID_both = dict['Outbound_ProfileID_both']

        Message_both = dict['Message_both']
        ProcessingFlag1_both = dict['ProcessingFlag1_both']
        ProcessingFlag1_IB = ProcessingFlag1_both + "_IB"
        ProcessingFlag1_OB = ProcessingFlag1_both + "_OB"
        Filename_both = dict['Filename_both']
        name1_Inbound_both = Receiver_both + "_INBOUND_" + Sender_both + "_SFTP_STEP1"
        name2_Inbound_both = Receiver_both + "_INBOUND_" + Sender_both + "_SFTP_STEP2"
        name1_Outbound_both = Receiver_both + "_Outbound_" + Sender_both + "_SFTP_STEP1"
        name2_Outbound_both = Receiver_both + "_Outbound_" + Sender_both + "_SFTP_STEP1"
        id_name = Sender_both + "_Both_" + Receiver_both
        Return_Name = 'Rule Edit Successfully'

        data_edit_both  = {
            "_id": id_name,
            "host": "eubpnsupporttool.sci.local",
            "port": Port,
            "outputFolder": "P:\\RPA\\BPNST",
            "disableAll": true,
            "checkForDuplicateRules": true,
            "skipRules": [],
            "rules": [
                {
                    "name": name1_Inbound_both,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_ReceiveSFTPEval",
                    "enabled": true,
                    "default": false,
                    "direction": "INBOUND",
                    "conditions": [
                        {
                            "name": "SourceSubject",
                            "operator": "Contains",
                            "value": Inbound_ProfileID_both,
                        }
                    ],
                    "actions": [
                        {
                            "name": "TrackIt",
                            "businessProcessName": "BPN_ReceiveSFTPTrack",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"}
                            ],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"},
                                {"name": "SourceSenderID", "value": Sender_both},
                                {"name": "Action", "value": "ROUTER"},
                                {
                                    "name": "ProcessingFlag1",
                                    "value": ProcessingFlag1_IB,
                                },
                                {"name": "MessageType", "value": Message_both},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                                {"name": "TargetSystemID", "value": "TX01"},
                                {
                                    "name": "SourceReceiverID",
                                    "value": Receiver_both,
                                },
                            ],
                        },
                    ],
                },
                {
                    "name": name2_Inbound_both,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_RouterEval",
                    "enabled": true,
                    "default": false,
                    "direction": "",
                    "conditions": [
                        {
                            "name": "ProcessingFlag1",
                            "operator": "=",
                            "value": ProcessingFlag1_IB,
                        }
                    ],
                    "actions": [
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_Finish",
                            "enabled": true,
                            "assignments": [],
                        }
                    ],
                },
                {
                    "name": name1_Outbound_both,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_ReceiveSFTPEval",
                    "enabled": true,
                    "default": false,
                    "direction": "OUTBOUND",
                    "conditions": [
                        {
                            "name": "SourceFileName",
                            "operator": "StartsWith",
                            "value": Filename_both,
                        },
                        {
                            "name": "SourceSubject",
                            "operator": "Contains",
                            "value": Outbound_ProfileID_both,
                        },
                    ],
                    "actions": [
                        {
                            "name": "TrackIt",
                            "businessProcessName": "BPN_ReceiveSFTPTrack",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "OUTBOUND"}
                            ],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "OUTBOUND"},
                                {"name": "SourceSenderID", "value": Sender_both},
                                {"name": "Action", "value": "ROUTER"},
                                {
                                    "name": "ProcessingFlag1",
                                    "value": ProcessingFlag1_OB,
                                },
                                {"name": "MessageType", "value": Message_both},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                                {"name": "TargetSystemID", "value": "TX01"},
                                {
                                    "name": "SourceReceiverID",
                                    "value": Receiver_both,
                                },
                            ],
                        },
                    ],
                },
                {
                    "name": name2_Outbound_both,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_RouterEval",
                    "enabled": true,
                    "default": false,
                    "direction": "OUTBOUND",
                    "conditions": [
                        {
                            "name": "ProcessingFlag1",
                            "operator": "=",
                            "value": "ProcessingFlag1_both",
                        }
                    ],
                    "actions": [
                        {
                            "name": "Action2",
                            "businessProcessName": "BPN_Finish",
                            "enabled": false,
                            "assignments": [],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "Category", "value": "SFTP"},
                                {"name": "Action", "value": "SEND"},
                                {"name": "TargetSystemID", "value": "PRO01"},
                                {
                                    "name": "ProtocolProfileID",
                                    "value": Outbound_ProfileID_both,
                                },
                                {"name": "InflightDirection", "value": "OUTBOUND"},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                            ],
                        },
                    ],
                },
            ],
        }
        return {"message": message}


def process_edit_inbound_basictx():
    RuleType = dict['RuleType']
    Port = 443
    true = 'true'
    false = 'false'
    message = 'Rule Edited Successfully'
    if RuleType == "Edit Inbound Basictx":
        ruleName = dict["ruleName"]
        Keyword = dict['Keyword']
        tradingpartner_Basictx__Inbound_Edit = dict["tradingpartner_Basictx__Inbound_Edit"]
        ProfileID_Basictx_Inbound_Edit = dict["ProfileID_Basictx_Inbound_Edit"]
        ProcessingFlag1_Basictx_Inbound_Edit = dict["ProcessingFlag1_Basictx_Inbound_Edit"]
        name1_BasicTx = "1.0.0_ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_Basictx__Inbound_Edit + "_SFTP_TO_BASICTX"
        name2_BasicTx = "1.0.2_ELUX_GENERIC_IN_FLAT_FILE_" + ProcessingFlag1_Basictx_Inbound_Edit + "_BASICTX_TO_CC_FINISH"
        Return_Name = name1_BasicTx + name2_BasicTx + "edited successfully"
        id_name = "ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_Basictx__Inbound_Edit

      
        data_edit_inbound_basictx ={
            "_id": id_name,
            "host": "nabpnsupporttool.comm1.sci.local",
            "port": 443,
            "outputFolder": "P:\\RPA\\BPNST",
            "disableAll": true,
            "checkForDuplicateRules": true,
            "skipRules": [],
            "rules": [
                {
                    "name": name1_BasicTx,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_ReceiveSFTPEval",
                    "enabled": true,
                    "default": false,
                    "direction": "INBOUND",
                    "conditions": [
                        {
                            "name": "SourceSubject",
                            "operator": "Contains",
                            "value":  ProfileID_Basictx_Inbound_Edit,
                        }
                    ],
                    "actions": [
                        {
                            "name": "TrackIt",
                            "businessProcessName": "BPN_ReceiveSFTPTrack",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"}
                            ],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"},
                                {"name": "Action", "value": "TX"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1_Basictx_Inbound_Edit},
                                {"name": "Category", "value": "BASIC"},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                                {"name": "TargetSystemID", "value": "TX01"},
                                {
                                    "name": "MapName",
                                    "value": "ELUX_DUMMY_PASSTHRU_Fortras100_inhouse",
                                },
                            ],
                        },
                    ],
                },
                {
                    "name": name2_BasicTx,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_BasicTranslationEval",
                    "enabled": true,
                    "default": false,
                    "direction": "",
                    "conditions": [
                        {
                            "name": "ProcessingFlag1",
                            "operator": "=",
                            "value": ProcessingFlag1_Basictx_Inbound_Edit,
                        }
                    ],
                    "actions": [
                        {
                            "name": "Action2",
                            "businessProcessName": "BPN_CarbonCopy",
                            "enabled": true,
                            "assignments": [
                                {"name": "CCv1Mode", "value": "TRUE"},
                                {"name": "CarbonCopyRecipient", "value": "OSC_DEMO"},
                                {"name": "CCNodesToKeep", "value": "SourceFileName"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1_Basictx_Inbound_Edit},
                            ],
                        },
                        {
                            "name": "Action3",
                            "businessProcessName": "BPN_Finish",
                            "enabled": true,
                            "assignments": [],
                        },
                    ],
                },
            ],
        }
    return {"message": message}
    
def process_edit_outbound_basictx():
    RuleType = dict['RuleType']
    
    if RuleType == "Edit Outbound Basictx":
        Port = 443
        true = 'true'
        false = 'false'
        message ='Rule Edited Successfully'
        rulename = dict["rulename"]
        Keyword = dict['Keyword']
        tradingpartner_Basictx = dict["tradingpartner_Basictx"]
        Profileid_Basictx = dict["Profileid_Basictx"]
        ProcessingFlag1_Basictx = dict["ProcessingFlag1_Basictx"]
        name1_BasicTx = "1.0.0_ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_Basictx + "_SFTP_TO_BASICTX"
        name2_BasicTx = "1.0.2_ELUX_GENERIC_IN_FLAT_FILE_" + ProcessingFlag1_Basictx + "_BASICTX_TO_CC_FINISH"
        Return_Name = name1_BasicTx + name2_BasicTx + "edited successfully"
        id_name = "ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_Basictx


        data_edit_outbound_basictx ={
            "_id": id_name,
            "host": "nabpnsupporttool.comm1.sci.local",
            "port": 443,
            "outputFolder": "P:\\RPA\\BPNST",
            "disableAll": true,
            "checkForDuplicateRules": true,
            "skipRules": [],
            "rules": [
                {
                    "name": name1_BasicTx,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_ReceiveSFTPEval",
                    "enabled": true,
                    "default": false,
                    "direction": "INBOUND",
                    "conditions": [
                        {
                            "name": "SourceSubject",
                            "operator": "Contains",
                            "value": Profileid_Basictx,
                        }
                    ],
                    "actions": [
                        {
                            "name": "TrackIt",
                            "businessProcessName": "BPN_ReceiveSFTPTrack",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"}
                            ],
                        },
                        {
                            "name": "SendToPod",
                            "businessProcessName": "BPN_SendPod",
                            "enabled": true,
                            "assignments": [
                                {"name": "InflightDirection", "value": "INBOUND"},
                                {"name": "Action", "value": "TX"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1_Basictx},
                                {"name": "Category", "value": "BASIC"},
                                {"name": "BusinessAlias", "value": "OSC_DEMO"},
                                {"name": "TargetSystemID", "value": "TX01"},
                                {
                                    "name": "MapName",
                                    "value": "ELUX_DUMMY_PASSTHRU_Fortras100_inhouse",
                                },
                            ],
                        },
                    ],
                },
                {
                    "name": name2_BasicTx,
                    "businessAlias": "OSC_DEMO",
                    "ruleBusinessAlias": "OSC_DEMO",
                    "ruleSet": "BPN_BasicTranslationEval",
                    "enabled": true,
                    "default": false,
                    "direction": "",
                    "conditions": [
                        {
                            "name": "ProcessingFlag1",
                            "operator": "=",
                            "value": ProcessingFlag1_Basictx,
                        }
                    ],
                    "actions": [
                        {
                            "name": "Action2",
                            "businessProcessName": "BPN_CarbonCopy",
                            "enabled": true,
                            "assignments": [
                                {"name": "CCv1Mode", "value": "TRUE"},
                                {"name": "CarbonCopyRecipient", "value": "OSC_DEMO"},
                                {"name": "CCNodesToKeep", "value": "SourceFileName"},
                                {"name": "ProcessingFlag1", "value": ProcessingFlag1_Basictx},
                            ],
                        },
                        {
                            "name": "Action3",
                            "businessProcessName": "BPN_Finish",
                            "enabled": true,
                            "assignments": [],
                        },
                    ],
                },
            ],
        }

    return {"message": message}
  

def process_rule_search():
    RuleType = dict['RuleType']
    
    if RuleType == "Rule search":
        ruleName = dict["ruleName"]
        selector = {"_id": ruleName}
        filename = f"{ruleName}.json"
        print(selector)
        message = 'Rule Search Successful'

        data_rule_search = {
            'RuleName': ruleName,
            'Selector': selector,
            'Filename': filename,
            'Return_Name': Return_Name
        }

        return {"message": message}
    else:
        return {"error": "Invalid RuleType"}

def main():
    RuleType = dict['RuleType']

    if RuleType == 'Inbound':
        result = process_inbound_dict()
    elif RuleType == 'Outbound':
        result = process_outbound_dict()
    elif RuleType == 'Both':
        result = process_both_dict()
    elif RuleType == 'Inbound BasicTx':
        result = process_basictx_inbound_dict()
    elif RuleType == 'Outbound BasicTx':
        result = process_basictx_outbound_dict()
    elif RuleType == 'Rule edit':
        result = process_rule_edit()
    elif RuleType == 'Edit Inbound Rule':
        result = process_edit_inbound()
    elif RuleType == 'Edit Outbound Rule':
        result = process_edit_outbound()
    elif RuleType == 'Edit Both Rule':
        result = process_edit_both()
    elif RuleType == 'Edit Inbound Basictx':
        result = process_edit_inbound_basictx()
    elif RuleType == 'Edit Outbound Basictx':
        result = process_edit_outbound_basictx()
    elif RuleType == 'Rule search':
        result = process_rule_search()
    else:
        print(f"Invalid RuleType: {RuleType}")

    if result:
        print(result)
