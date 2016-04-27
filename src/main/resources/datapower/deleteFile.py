#
#    THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
#    FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from datapower.datapower import datapowerClient


domain   = deployed.container.domain
host     = deployed.container.host
port     = deployed.container.RestPort

username = deployed.container.username
password = deployed.container.password

filePath = deployed.filePath
fileName = deployed.fileName

url = 'https://%s:%s' % (  host, port )
uri = '/mgmt/filestore/%s/%s/%s' % ( domain, filePath, fileName )

wsdlFile = open( deployed.file.path )
fileData = wsdlFile.read()

print "URL = %s%s" % (url, uri)

dpClient = datapowerClient( url, username, password )

results = dpClient.deleteFile( domain, filePath, fileName )
print results


