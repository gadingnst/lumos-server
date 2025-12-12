from flask import jsonify

def api_response(success, message, payload=None, status_code=200):
  """
  Generate a standardized API response.
  
  Args:
    success (bool): Whether the request was successful.
    message (str): A message describing the result.
    payload (any, optional): The data to return. Defaults to None.
    status_code (int, optional): The HTTP status code. Defaults to 200.
    
  Returns:
    tuple: A tuple containing the JSON response and the status code.
  """
  response = {
    'success': success,
    'message': message,
    'payload': payload
  }
  return jsonify(response), status_code

def success_response(message='Success', payload=None, status_code=200):
  """
  Generate a success API response.
  """
  return api_response(True, message, payload, status_code)

def error_response(message='Error', payload=None, status_code=500):
  """
  Generate an error API response.
  """
  return api_response(False, message, payload, status_code)
