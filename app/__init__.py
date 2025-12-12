from flask import Flask
from .modules.ServerInfo.routes import server_info_bp
from .modules.ServerControl.routes import server_control_bp

def create_app():
  """
  Factory function to create and configure the Flask application.
  
  Returns:
    The configured Flask application instance.
  """
  app = Flask(__name__)
  
  # Register modules
  app.register_blueprint(server_info_bp, url_prefix='/api')
  app.register_blueprint(server_control_bp, url_prefix='/api')
  
  return app
