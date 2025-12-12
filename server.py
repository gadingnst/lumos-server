import os
from app import create_app

def main():
  """
  Main entry point for the application.
  """
  app = create_app()
  
  # Get port from environment variable or default to 5000
  port = int(os.environ.get('PORT', 5000))
  
  print(f"Starting server on port {port}...")
  
  # Run the application
  app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
  main()
