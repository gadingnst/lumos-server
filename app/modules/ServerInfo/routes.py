from flask import Blueprint
from .handler import ServerInfoHandler

server_info_bp = Blueprint('server_info', __name__)
handler = ServerInfoHandler()

@server_info_bp.route('/health', methods=['GET'])
def health():
  """
  Route to verify server status.
  """
  return handler.health()
