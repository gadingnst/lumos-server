import wakeonlan
import os
import paramiko
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

  def shutdown_ai_server(self):
    """
    Shutdown the AI server via SSH.
    
    Returns:
      True if command sent, False if connection failed.
    """
    ip = os.getenv('AI_SERVER_IP')
    user = os.getenv('AI_SERVER_USER')
    
    if not ip or not user:
      return False
      
    try:
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      
      # Connect
      # Use empty password as requested
      ssh.connect(ip, username=user, password='', timeout=10, allow_agent=False, look_for_keys=False)
      
      # Execute shutdown command
      # Assuming passwordless sudo for 'shutdown' or 'poweroff'
      stdin, stdout, stderr = ssh.exec_command('shutdown /s /f /t 0')

      # read the output and error
      output = stdout.read().decode().strip()
      error  = stderr.read().decode().strip()

      print(f"Output: {output}")
      print(f"Error: {error}")

      # Close connection
      ssh.close()
      return True
    except Exception as e:
      print(f"SSH Error: {e}")
      return False
