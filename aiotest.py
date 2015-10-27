#!usr/bin/env python3
import asyncio
from aiohttp import web
def index(request):
    return web.Response(body=b'<h1>Index</h1>')

def hello(request):
    yield from asyncio.sleep(0.5)
    text='<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}',hello)
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
