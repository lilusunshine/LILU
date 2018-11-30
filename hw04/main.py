import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,x):
        if x==None:
            x=9
        x =int(x)
        if x>9:
            x=9
        html = '''
        <html>
        <body>
        '''
        if  0 < x < 10:
            for i in range(1,x+1):
                for j in range (1,i+1):
                    if i*j>=10:
                        html += '<td>' + str("%d*%d=%d" % (i,j,i*j)) + '&nbsp;&nbsp;' + '</td>'              
                    else:
                        html += '<td>' + str("%d*%d=%d" % (i,j,i*j)) + '&nbsp;&nbsp;&nbsp;&nbsp;' + '</td>'
                html += '</br>'
        html += '''      
        </body>
        <ml>'''
    
        self.write(html)

application = tornado.web.Application([
    (r"/([0-9])?", MainHandler)
    ], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
