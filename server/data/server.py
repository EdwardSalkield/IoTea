import cherrypy, os, json, sys

teaqueue = []

def success():
        return(json.dumps({'success': True, 'error': ''}))


def failure():
        return(json.dumps({'success': False, 'error': ''}))

class RootServer:
        @cherrypy.expose
        # Authenticates the tea brewer, and sends it a session cookie
        def authenticate(self, code=None):
                if code == "FacebookLadyWeLoveYou":
                        cherrypy.session['usertype'] = "brewer"
                        return success()
                return(json.dumps({'success': False}))


        @cherrypy.expose
        # Adds a cup of tea to the queue
        def enqueue(self, temp=None, time=None, mode='brew'):
                teaqueue.append(tuple([temp, time, mode]))
                return success()

        # Says what sort of tea is currently on top of the queue
        @cherrypy.expose
        def peek(self):
                if len(teaqueue) == 0:
                        return failure()

                tea = teaqueue[0]
                return(json.dumps({'success': True, 'temp': tea[0], 'time': tea[1], 'mode': tea[2]}))
        # Removes the current tea from the queue
        @cherrypy.expose
        def dequeue(self):
                try:
                        if cherrypy.session['usertype'] == "brewer":

                                if len(teaqueue) == 0:
                                        return failure()
                                tea = teaqueue.pop(0)
                                return(json.dumps({'success': True, 'temp': tea[0], 'time': tea[1], 'mode': tea[2]}))
                        else:
                                return(json.dumps({'success': False}))

                except Exception:
                        return(json.dumps({'success': False}))



if __name__ == '__main__':
        cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8081,
                            'tools.sessions.on' : True,
                            'tools.sessions.timeout': 10
                            })

        cherrypy.quickstart(RootServer())

