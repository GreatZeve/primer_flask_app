from flask import Flask

def create_app():
app=Flask(--name__)
app.config.from_object(config.Confing)

from .views import main as main_blueprint
app.register_blueprint(main_blueprint)

return app
