import cherrypy, json, sys

from langdetector import LangDetector

a = None

class WebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def langdetect(self):
      data = cherrypy.request.json
      print (data)
      output = {}

      if "text" in data.keys():
         output = a.detect(data["text"])

      return output


if __name__ == '__main__':

   a = LangDetector()

   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(WebService())	