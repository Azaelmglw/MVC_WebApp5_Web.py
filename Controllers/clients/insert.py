import web
import Controllers.config as config


class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render1.insert()

    def POST(self):
        input_field = web.input()
        name = input_field['name']
        gender = input_field['gender']
        phone_number = input_field['phone_number']
        occupation = input_field['occupation']
        config.model_clients.insert_client(name, gender, phone_number, occupation)
        raise web.seeother('/')