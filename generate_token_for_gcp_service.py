# In this file we will use service account credentials json file to generate access token which will be used for authorisation to connect to a service (here cloud function)

import google.oauth2.id_token
import google.auth.transport.requests
import os




def get_gcp_access_token(cred_file_path:str, target_service_url: str):
  """
  Returns the access/bearer token to access a service of gcp
  cred_file_path: path of service account credentials json file for which we want to generate the token
  target_service_url: The url of service for which we are generating the token. This url is also known as audience or target_audience.
  """
  
  # setting environment variable path, which will be used by google auth to generate token for cloud function service 
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_file_path
  request = google.auth.transport.requests.Request()
  
  # Fetching the token
  id_token = google.oauth2.id_token.fetch_id_token(request, target_service_url)
  return id_token


target_audience = "https://europe-west2-dev-applications-356712.cloudfunctions.net/hello-world-function"
cred_file_path = "/home/slim5/gcp-project/ultra-palisade-398714-514edd7f971d.json"

# get_gcp_access_token(cred_file_path, target_audience)
