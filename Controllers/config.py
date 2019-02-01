import web
import Models.model_clients as model_clients
import Models.model_products as model_products

render = web.template.render('Views/', base = 'master')
render1 = web.template.render('Views/clients/', base = 'master')
render2 = web.template.render('Views/products/', base  = 'master')