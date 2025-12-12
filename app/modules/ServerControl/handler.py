from app.helpers.response import success_response, error_response
from .service import ServerControlService

class ServerControlHandler:
  """
  Handler for server control requests.
  """
  
  def __init__(self):
    self.service = ServerControlService()

  def wake_ai_server(self):
    """
    Handle request to wake the AI server.
    """
    try:
      success = self.service.wake_ai_server()
      
      if not success:
        return error_response(message='AI_SERVER_MAC_ADDR not configured', status_code=500)
        
      return success_response(message='Magic packet sent to AI Server')
      
    except Exception as e:
      return error_response(message=str(e), status_code=500)
