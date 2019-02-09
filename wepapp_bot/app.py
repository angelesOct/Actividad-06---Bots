import web
        
urls = (
    '/', 'application.controllers.bot.index.Index',
    '/insert', 'application.controllers.bot.insert.Insert',
    '/update/(.*)', 'application.controllers.bot.update.Update',
    '/delete/(.*)', 'application.controllers.bot.delete.Delete',
    '/view/(.*)', 'application.controllers.bot.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
