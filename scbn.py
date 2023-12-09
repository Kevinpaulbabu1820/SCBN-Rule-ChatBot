from neo4j import GraphDatabase


class Neo4jConnector:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    @property
    def driver(self):
        return self._driver


def get_nodes_by_id_name(tx, id_name):
    query = (
        "MATCH (r:Rule) "
        "WHERE r.id_name = $id_name "
        "RETURN r"
    )
    result = []
    for record in tx.run(query, id_name=id_name):
        result.append(record["node"])
    return result


def create_inbound_rule(connector, profileid, sender, receiver, message, processingflag1, ruletype):
    id_name = receiver + '_inBOUND_' + sender
    name1_inbound = receiver + '_inBOUND_' + sender + '_SFTP_STEP1'
    return_name = name1_inbound + '& SFTP_STEP2 created successfully'

    query = (
        "CREATE (r:Rule {sender: $sender, receiver: $receiver, "
        "message: $message, profileid: $profileid, ruletype: $ruletype, "
        "processingflag1: $processingflag1,id_name:$id_name})"
    )

    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run(query, sender=sender, receiver=receiver,
                                                    message=message, profileid=profileid,
                                                    ruletype=ruletype, processingflag1=processingflag1,
                                                    id_name=id_name))
        return return_name


def create_outbound_rule(connector, profileid_outbound, sender_outbound, receiver_outbound,
                         message_outbound, processingflag1_outbound, filename_output):
    id_name = receiver_outbound + '_outbound_' + sender_outbound
    name1_outbound = receiver_outbound + '_Outbound_' + sender_outbound + '_SFTP_STEP1'
    return_name = name1_outbound + '& SFTP_STEP2 created successfully'
    query = (
        "CREATE (r:Rule {sender_outbound: $sender_outbound, receiver_outbound: $receiver_outbound, "
        "message_outbound: $message_outbound, profileid_outbound: $profileid_outbound, "
        "filename_output: $filename_output, "
        "processingflag1_outbound: $processingflag1_outbound,id_name:$id_name})"
    )

    with connector._driver.session() as session:
        session.write_transaction(
            lambda tx: tx.run(query, sender_outbound=sender_outbound, receiver_outbound=receiver_outbound,
                              message_outbound=message_outbound, profileid_outbound=profileid_outbound,
                              filename_output=filename_output, processingflag1_outbound=processingflag1_outbound,
                              id_name=id_name))
        return return_name


def create_both_rule(connector, inbound_profileid_both, outbound_profileid_both, sender_both, receiver_both,
                     message_both, processingflag1_both, filename_both):
    id_name = receiver_both + '_Both_' + sender_both
    return_name = receiver_both + 'both' + sender_both + 'SFTP_STEP1,SFTP_STEP2 created successfully'
    query = (
        "CREATE (r:Rule {sender_both: $sender_both, receiver_both: $receiver_both, "
        "message_both: $message_both, "
        "inbound_profileid_both: $inbound_profileid_both, outbound_profileid_both: $outbound_profileid, "
        "processingflag1_both: $processingflag1_both, filename_both: $filename_both,id_name:$id_name})"
    )

    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run(query, sender_both=sender_both, receiver_both=receiver_both,
                                                    message=message_both, inbound_profileid=inbound_profileid_both,
                                                    outbound_profileid_both=outbound_profileid_both,
                                                    processingflag1_both=processingflag1_both,
                                                    filename=filename_both, id_name=id_name))
        return return_name


def create_inbound_basictx_rule(connector, tradingpartner_basictx, profileid_basictx, processingflag1_basictx, id_name):
    name1_basictx = "1.0.0_ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_basictx + "_SFTP_TO_BASICTX"
    name2_basictx = "1.0.2_ELUX_GENERIC_IN_FLAT_FILE_" + processingflag1_basictx + "_BASICTX_TO_CC_FINISH"
    return_name = name1_basictx + name2_basictx + "created successfully"
    query = (
        "CREATE (r:Rule {TradingPartner: $tradingpartner_basictx, profileid: $profileid_basictx, "
        "processingflag1_basictx: $processingflag1_basictx,id_name:$id_name})"
    )

    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run(query, tradingpartner_basictx=tradingpartner_basictx,
                                                    profileid_basictx=profileid_basictx,
                                                    processingflag1_basictx=processingflag1_basictx, id_name=id_name))
    return return_name


def create_outbound_basictx_rule(connector, tradingpartner_basictx, profileid_basictx, processingflag1_basictx,
                                 id_name):
    name1_basictx = "1.0.0_ELUX_OUTBOUND_RECEIVE_FROM_" + tradingpartner_basictx + "_SFTP_TO_BASICTX"
    name2_basictx = "1.0.2_ELUX_GENERIC_IN_FLAT_FILE_" + processingflag1_basictx + "_BASICTX_TO_CC_FINISH"
    return_name = name1_basictx + name2_basictx + "created successfully"
    query = (
        "CREATE (r:Rule {TradingPartner: $tradingpartner_basictx, profileid: $profileid_basictx, "
        "processingflag1: $processingflag1_basictx,id_name:$id_name})"
    )
    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run(query, tradingpartner_basictx=tradingpartner_basictx,
                                                    profileid_basictx=profileid_basictx,
                                                    processingflag1_basictx=processingflag1_basictx, id_name=id_name))
        return return_name


def edit_inbound_rule(connector, new_profile_id, new_message, new_processingflag1):
    s_id = dict["s_id"]
    return_name = 'Rule Edit Successfully'
    query = (
        "MATCH (r:Rule) WHERE r.id_name = $s_id "
        "SET r.profileid = $new_profile_id, "
        "    r.message = $new_message, "
        "    r.processingflag1 = $new_processingflag1 "
    )
    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run(query, new_profile_id=new_profile_id,
                                                    new_message=new_message, new_processingflag1=new_processingflag1,
                                                    s_id=s_id))
    return return_name


def edit_outbound_rule(connector, new_profile_id, new_message, new_processing_flag, new_filename):
    s_id = dict["s_id"]
    return_name = 'Rule Edit Successfully'
    query = (
        "MATCH (r:Rule) WHERE r.id_name = $id_name "
        "SET r.profileid_outbound = $new_profile_id, "
        "    r.message_outbound = $new_message, "
        "    r.processingflag1_outbound = $new_processing_flag, "
        "    r.filename_output = $new_filename"
    )
    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run(query, return_name=return_name, new_profile_id=new_profile_id,
                                                    new_message=new_message, new_processing_flag=new_processing_flag,
                                                    new_filename=new_filename, s_id_name=s_id))
    return return_name


def edit_both_rule(connector, new_inbound_profile_id, new_outbound_profile_id, new_message,
                   new_processing_flag,
                   new_filename):
    s_id = dict["s_id"]
    return_name = 'Rule Edit Successfully'
    query = (
        "MATCH (r:Rule) WHERE r.id_name = $s_id "
        "SET r.inbound_profileid_both = $new_inbound_profile_id, "
        "    r.outbound_profileid_both = $new_outbound_profile_id, "
        "    r.message_both = $new_message, "
        "    r.processingflag1_both= $new_processing_flag, "
        "    r.filename_both = $new_filename"
    )
    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run(query, new_inbound_profile_id=new_inbound_profile_id,
                                                    new_outbound_profile_id=new_outbound_profile_id,
                                                    new_message=new_message,
                                                    new_processing_flag=new_processing_flag, new_filename=new_filename,
                                                    s_id_=s_id))

    return return_name


def edit_inbound_basictx_rule(connector, new_tradingpartner, new_profile_id, new_processing_flag):
    s_id = dict["s_id"]
    return_name = 'Rule Edit Successfully'
    query = (
        "MATCH (r:Rule) WHERE r.id_name = $s_id "
        "SET r.tradingpartner = $new_tradingpartner, "
        "    r.profile_id = $new_profile_id, "
        "    r.processing_flag = $new_processing_flag"
    )
    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run
                                  .run(query, new_tradingpartner=new_tradingpartner, new_profile_id=new_profile_id,
                                       new_processing_flag=new_processing_flag, s_id=s_id))

    return return_name


def edit_outbound_basictx_rule(connector, new_tradingpartner, new_profile_id, new_processing_flag):
    s_id = dict["s_id"]
    return_name = 'Rule Edit Successfully'
    query = (
        "MATCH (r:Rule) WHERE r.id_name = $s_id "
        "SET r.tradingpartner_basictx = $new_tradingpartner, "
        "    r.profileid_basictx = $new_profile_id, "
        "    r.processingflag1_basictx = $new_processing_flag"
    )

    with connector._driver.session() as session:
        session.write_transaction(lambda tx: tx.run
                                  .run(query, return_name=return_name, new_tradingpartner=new_tradingpartner,
                                       new_profile_id=new_profile_id, new_processing_flag=new_processing_flag,
                                       s_id=s_id))

    return return_name


def main(dict):
    uri = "bolt://localhost:7687"
    user = "admin"
    password = "password"
    connector = Neo4jConnector(uri, user, password)
    ruletype = dict['ruletype']
    # Initialize a dictionary to store the result

    if ruletype == 'Inbound':
        profileid = dict['profile_id']
        sender = dict['sender']
        receiver = dict['receiver']
        message = dict['message']
        processingflag1 = dict['processingflag1']
        create_inbound_rule(connector, profileid, sender, receiver, message, processingflag1, ruletype)

    elif ruletype == 'Outbound':
        profileid_outbound = dict['profileid_outbound']
        sender_outbound = dict['sender_outbound']
        receiver_outbound = dict['receiver_outbound']
        message_outbound = dict['message_outbound']
        processingflag1_outbound = dict['processingflag1_outbound']
        filename_output = dict['filename_output']

        create_outbound_rule(connector, profileid_outbound, sender_outbound, receiver_outbound,
                             message_outbound, processingflag1_outbound, filename_output)
    elif ruletype == 'Both':
        inbound_profileid_both = dict['inbound_profileid_both']
        outbound_profileid_both = dict['outbound_profile_id_both']
        sender_both = dict['sender_both']
        receiver_both = dict['receiver_both']
        message_both = dict['message_both']
        processingflag1_both = dict['processingflag1_both']

        filename_both = dict['filename_both']

        create_both_rule(connector, inbound_profileid_both, outbound_profileid_both, sender_both,
                         receiver_both, message_both, processingflag1_both, filename_both)

    elif ruletype == 'Inbound BasicTx':
        tradingpartner_basictx = dict["tradingpartner_Basictx"]
        profileid_basictx = dict["profileid_Basictx"]
        processingflag1_basictx = dict["ProcessingFlag1_Basictx"]
        id_name = "ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_basictx
        create_inbound_basictx_rule(connector, tradingpartner_basictx, profileid_basictx,
                                    processingflag1_basictx, id_name)
    elif ruletype == 'Outbound BasicTx':
        tradingpartner_basictx = dict["tradingpartner_basictx"]
        profileid_basictx = dict["profile_id_basictx"]
        processingflag1_basictx = dict["processingflag1_basictx"]
        id_name = "ELUX_INBOUND_RECEIVE_FROM_" + tradingpartner_basictx
        create_outbound_basictx_rule(connector, tradingpartner_basictx, profileid_basictx,
                                     processingflag1_basictx, id_name)
    elif ruletype == 'Edit Inbound Rule':

        new_message = dict["new_message"]
        new_profile_id = dict["new_profile_id"]
        new_processing_flag = dict["new_processing_flag"]

        edit_inbound_rule(connector, new_profile_id, new_message, new_processing_flag)

    elif ruletype == 'Edit Outbound Rule':

        new_profile_id = dict["new_profile_id"]
        new_message = dict["new_message"]
        new_processing_flag = dict["new_processing_flag"]
        new_filename = dict["new_filename"]
        edit_outbound_rule(connector, new_profile_id, new_message, new_processing_flag, new_filename)

    elif ruletype == 'Edit Both Rule':

        new_inbound_profile_id = dict["new_inbound_profile_id"]
        new_outbound_profile_id = dict["new_outbound_profile_id"]
        new_filename = dict['new_filename']
        new_message = dict["Message_edit_Both"]
        new_processing_flag = dict["new_processing_flag"]
        edit_both_rule(connector, new_inbound_profile_id, new_outbound_profile_id, new_message,
                       new_processing_flag, new_filename)
    elif ruletype == 'Edit Inbound BasicTx':

        new_tradingpartner = dict["new_tradingpartner"]
        new_profile_id = dict["new_profile_id"]
        new_processing_flag = dict["new_processing_flag"]
        edit_inbound_basictx_rule(connector, new_tradingpartner, new_profile_id, new_processing_flag)

    elif ruletype == 'Edit Outbound BasicTx':
        new_tradingpartner = dict["new_tradingpartner"]
        new_profile_id = dict["new_profile_id"]
        new_processing_flag = dict["new_processing_flag"]
        edit_outbound_basictx_rule(connector, new_tradingpartner, new_profile_id, new_processing_flag)
    elif ruletype == 'Rule Search':
        s_id = dict['s_id']
        query = (
            "MATCH (r:Rule) "
            "WHERE r.id_name = $s_id "
            "RETURN r"
        )
        result = []

        with connector._driver.session() as session:
            def search_rule_transaction(tx):
                for record in tx.run(query, s_id=s_id):
                    result.append(record["node"])

            session.write_transaction(search_rule_transaction)

        return result
    else:
        print(f"Unsupported ruletype: {ruletype}")
    connector.close()
