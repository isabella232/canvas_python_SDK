import base64
import hashlib
import hmac
import json
import os
import urllib

class OptimizelyCanvasValidationError(Exception):
  pass

class CanvasValidation(object):
  def __init__(self, signed_request, optimizely_oauth_client_secret):
    self.signed_request = signed_request
    self.optimizely_oauth_client_secret = optimizely_oauth_client_secret

  def _decode_context(self):
    return json.loads(base64.b64decode(self.signed_request.split('.')[1]))

  def _validate_context(self):
    hashed_context, unhashed_context = self.signed_request.split('.')
    hashed_context=urllib.unquote(hashed_context).decode('utf8') 

    re_hashed_context = base64.b64encode(hmac.new(self.optimizely_oauth_client_secret, unhashed_context, hashlib.sha256).hexdigest())

    if hashed_context != re_hashed_context:
      raise OptimizelyCanvasValidationError()

  def extractUserContext(self):
    try:
      self._validate_context()
      return self._decode_context()

    except OptimizelyCanvasValidationError:
      raise OptimizelyCanvasValidationError("Error: Request not properly signed")

  




