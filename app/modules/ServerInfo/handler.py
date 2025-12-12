from app.helpers.response import success_response
from .service import ServerInfoService

class ServerInfoHandler:
  """
  Handler for server info requests.
  """
  
  def __init__(self):
    self.service = ServerInfoService()

  def health(self):
    """
    Handle health check request.
    """
    result = self.service.get_health()
    return success_response(message='Server is healthy', payload=result)
