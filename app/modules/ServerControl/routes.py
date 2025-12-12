from flask import Blueprint
from .handler import ServerControlHandler

server_control_bp = Blueprint('server_control', __name__)
handler = ServerControlHandler()

@server_control_bp.route('/ai-server/start', methods=['POST'])
def start_ai_server():
  """
  Route to wake the AI server via Wake-on-LAN.
  """
  return handler.wake_ai_server()

@server_control_bp.route('/ai-server/shutdown', methods=['POST'])
def shutdown_ai_server():
  """
  Route to shutdown the AI server via SSH.
  """
  return handler.shutdown_ai_server()
