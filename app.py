import web

urls = (
    '/', 'Controllers.index.Index',

    '/clients/insert', 'Controllers.clients.insert.Insert',
    '/clients/update/(.*)', 'Controllers.clients.update.Update',
    '/clients/delete/(.*)', 'Controllers.clients.delete.Delete',
    '/clients/view/(.*)', 'Controllers.clients.view.View',

    '/products/insert', 'Controllers.products.insert.Insert',
    '/products/update/(.*)', 'Controllers.products.update.Update',
    '/products/delete/(.*)', 'Controllers.products.delete.Delete',
    '/products/view/(.*)', 'Controllers.products.view.View',
)


if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()