import argparse
import asyncio
from getpass import getuser
from .mxtunnel import open_tunnel


def main():
    parser = argparse.ArgumentParser(description='Live And HTTPS Localhost')
    parser.add_argument('-p', '--port', type=int, default=False, help='Port number of the local server')
    parser.add_argument('-V', '--version', action='store_true' ,help='Version number of jpmx-tunnel')
    parser.add_argument
    args = parser.parse_args()

    if args.version:
        print("0.1.5")
        return
    
    if not args.port:
        print("Please specify -p/--port argument and port.")
        return

    username = getuser()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            open_tunnel(
                ws_uri=f'wss://mx.tunnel.messengerx.io/_ws/?username=&port={args.port}',
                http_uri=f'http://127.0.0.1:{args.port}',
            )
        )
    except KeyboardInterrupt:
        print("\nmx-tunnel tunnel closed")
