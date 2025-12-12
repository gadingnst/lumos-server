import wakeonlan
import os
from dotenv import load_dotenv

load_dotenv()

class ServerControlService:
  """
  Service to handle server control operations.
  """
  
  def wake_ai_server(self):
    """
    Send a magic packet to the AI server MAC address defined in env.
    
    Returns:
      True if packet sent, False if MAC address not found.
    """
    mac_address = os.getenv('AI_SERVER_MAC_ADDR')
    
    if not mac_address:
      return False
      
    wakeonlan.send_magic_packet(mac_address)
    return True
