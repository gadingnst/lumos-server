from flask import Blueprint
from .handler import ServerControlHandler

server_control_bp = Blueprint('server_control', __name__)
handler = ServerControlHandler()

@server_control_bp.route('/wake-on-lan', methods=['POST'])
def wake_ai_server():
  """
  Route to wake the AI server via Wake-on-LAN.
  """
  return handler.wake_ai_server()
