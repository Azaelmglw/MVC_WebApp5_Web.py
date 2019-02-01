import config as config

db = config.db

def select_clients():
    try:
        return db.select('clients', order = "c_id ASC")
    except Exception as e:
        print "Error 000: There was a problem while obtaining the clients data. {}".format(e.args)
        print "Error 000: There was a problem while obtaining the clients data. {}".format(e.message)
        return None

def select_client(id):
    try:
        return db.select('clients', where = 'c_id = $id', vars = locals())[0]
    except Exception as e:
        print "Error 000: There was a problem while obtaining the client's data. {}".format(e.args)
        print "Error 000: There was a problem while obtaining the client's data. {}".format(e.message)
        return None

def insert_client(name, gender, phone_number, occupation):
    try:
        return db.insert('clients', c_name = name, c_gender = gender, c_phone_number = phone_number, c_occupation = occupation)
    except Exception as e:
        print "Error 000: There was a problem while adding the client. {}".format(e.args)
        print "Error 000: There was a problem while adding the client. {}".format(e.message)
        return None

def update_client(id, name, gender, phone_number, occupation):
    try:
        return db.update('clients', c_name = name, c_gender = gender, c_phone_number = phone_number, c_occupation = occupation, where = 'c_id = $id', vars = locals())
    except Exception as e:
        print "Error 000: There was a problem while updating the client's data. {}".format(e.args)
        print "Error 000: There was a problem while updating the client's data. {}".format(e.message)
        return None

def delete_client(id):
    try:
        return db.delete('clients', where = 'c_id = $id', vars = locals())
    except Exception as e:
        print "Error 000: There was a problem while removing the client. {}".format(e.args)
        print "Error 000: There was a problem while removing the client. {}".format(e.message)
        return None
