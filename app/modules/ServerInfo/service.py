class ServerInfoService:
  """
  Service to handle server info operations.
  """
  
  def get_health(self):
    """
    Get the current health status of the server.
    
    Returns:
      A dictionary containing the status and message.
    """
    return {
      'status': 'ok',
      'message': 'Lumos server is running'
    }
