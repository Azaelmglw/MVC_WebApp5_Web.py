import config as config

db = config.db

def select_products():
    try:
        return db.select('products', order = "p_id ASC")
    except Exception as e:
        print "Error 000: There was a problem while obtaining the products data. {}".format(e.args)
        print "Error 000: There was a problem while obtaining the products data. {}".format(e.message)
        return None

def select_product(id):
    try:
        return db.select('products', where = 'p_id = $id', vars = locals())[0]
    except Exception as e:
        print "Error 000: There was a problem while obtaining the product's data. {}".format(e.args)
        print "Error 000: There was a problem while obtaining the product's data. {}".format(e.message)
        return None

def insert_product(name, description, brand, origin):
    try:
        return db.insert('products', p_name = name, p_description = description, p_brand = brand, p_origin = origin)
    except Exception as e:
        print "Error 000: There was a problem while adding the product. {}".format(e.args)
        print "Error 000: There was a problem while adding the product. {}".format(e.message)
        return None

def update_product(id, name, description, brand, origin):
    try:
        return db.update('products', p_name = name, p_description = description, p_brand = brand, p_origin = origin, where = 'p_id = $id', vars = locals())
    except Exception as e:
        print "Error 000: There was a problem while updating the product's data. {}".format(e.args)
        print "Error 000: There was a problem while updating the product's data. {}".format(e.message)
        return None

def delete_product(id):
    try:
        return db.delete('products', where = 'p_id = $id', vars = locals())
    except Exception as e:
        print "Error 000: There was a problem while removing the product. {}".format(e.args)
        print "Error 000: There was a problem while removing the product. {}".format(e.message)
        return None