import pycurl
import certifi
from tkinter import *
from io import BytesIO
import webview
# Creating a buffer as the cURL is not allocating a buffer for the network response
buffer = BytesIO()
c = pycurl.Curl()
#initializing the request URL
c.setopt(c.URL, 'https://example.com/')
#setting options for cURL transfer  
c.setopt(c.WRITEDATA, buffer)
#setting the file name holding the certificates
c.setopt(c.CAINFO, certifi.where())
# perform file transfer
c.perform()
#Ending the session and freeing the resources
c.close()
#retrieve the content BytesIO
body = buffer.getvalue()
#decoding the buffer 
# print(body.decode('iso-8859-1'))

# f = open('holamundo.html','w')
# f.write(body.decode('iso-8859-1'))
# f.close()

# body.decode('iso-8859-1')
a = body.decode('iso-8859-1')

raiz = Tk()
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana
raiz.mainloop()