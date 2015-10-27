#!usr/bin/env python3
import asycio
from aiohttp import web

class AcceptChosser:
    def __init__(self):
        self._accepts={}
    @asyncio.coroutine
    def do_route(self,request):
        for accept in request.headers.getall('ACCEPT',[]):
            acceptor=self._accepts.get(accept)
            if acceptor is not None:
                return (yield from acceptor(request))
        raise HTTPNotAcceptable()
    def reg_acceptor(self,accept,handler):
        self._accepts[accept]=handler

@asyncio.coroutine
def handle_json(request):
    # do xml handling

@asyncio.coroutine
def handle_xml(request):
    # do xml handling

chooser=AcceptChooser()
app=web.Application()
app.router.add_route('GET','/',chooser.do_route)
chooser.reg_acceptor('application/json',handle_json)
chooser.reg_acceptor('application/xml',handl_xml)
