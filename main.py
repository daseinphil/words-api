import os, random, json
import tornado.httpserver
import tornado.ioloop
import tornado.web
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")
 
class NounHandler(MainHandler):
    def get(self):
        noun_text = open('nouns.json', 'r').read()
        noun_json = json.loads(noun_text)
        self.write(random.choice(noun_json))

class VerbHandler(MainHandler):
    def get(self):
        verb_text = open('verbs.json', 'r').read()
        verb_json = json.loads(verb_text)
        self.write(random.choice(verb_json))

class AdjectiveHandler(MainHandler):
    def get(self):
        adjective_text = open('adjectives.json', 'r').read()
        adjective_json = json.loads(adjective_text)
        self.write(random.choice(adjective_json))

# RAMMING SPEEEEED
def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/noun", NounHandler),
        (r"/verb", VerbHandler),
        (r"/adjective", AdjectiveHandler),

    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()