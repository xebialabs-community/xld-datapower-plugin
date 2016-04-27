#
#    THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
#    FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import time
import json
import base64
from http.http_connection import HttpConnection
from http.http_request import HttpRequest
from http.http_response import HttpResponse
from http.http_entity_builder import HttpEntityBuilder

class datapowerClient( object ):
   def __init__( self, url, username, password ):
      '''
      Builds a datapowerClient

      :param url: The url of the REST inteface of the Datapower device
      :param username: The username to connect to the datapower device
      :param password: The passoword to connecto to the datapwoer device
      '''
      self.url = url
      if url.endswith('/'):
         self.url = url[:-1]
      self.http_connection = HttpConnection(url, username, password)
      self.request = HttpRequest( self.http_connection, username, password)
   # End __init__

   def uploadFile( self, domain, path, fileName, fileData ):
      '''
      Upload a file to a Datapower device

      param: domain: The domain in the Datapower device where the file will be stored
      param: path: the Datapower path
      param: fileName: the file to be stored on the datapower devide
      param: fileData: the file content to be stored on the datapower devide
      '''
      uri = '/mgmt/filestore/%s/%s/%s' % (domain,path,fileName)
      fileData64 = base64.encodestring( fileData )
      payload = '''
      {
        "file": {
                "name":"%s",
                "content":"%s"
        }
      }
      '''
      body = payload % ( fileName, fileData64 )

      
      r = self.request.put( uri, HttpEntityBuilder.create_string_entity( body ), contentType = 'application/json' )
      
      response = json.loads( r.response )
      
      return response['result']
   # End uploadFile

   def downloadFile( self, domain, path, file ):
      '''
      Download a file from a Datapower device
   
     
      param: domain: The domain in the Datapower device where the file will be stored
      param: path: the Datapower path
      param: file: the file to be stored on the datapower devide
      '''

      r = self.request.get( uri, contentType = 'application/json' )
      response = json.loads(r.response)
      
      print response['_links']['self']['href']
      return base64.decodestring(response['file'])
   # End downloadFile

# End datapowerClient
