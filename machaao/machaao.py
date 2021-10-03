import click
import sys
import os
from shutil import copytree, copy
import machaao
import asyncio
from requests import request
from json import dumps
import subprocess
import shlex
import signal
import platform

FILE_DIR = os.path.dirname(os.path.abspath(machaao.__file__))

CURR_DIR = os.path.abspath(os.getcwd())

OS = str(platform.system()).lower()


_tunnel_p = None
_chatbot_p = None


def copyany(src, dst):
    try:
        copy(src, dst)
    except OSError as exc:
        click.secho(exc, fg="red", bold=True)


@click.group()
def cli():
    """
    An easy to use module for python developers 
    looking to build and develop chatbots using 
    MACHAAO Platform. Provide the Project Name to start with the template.

    Here is an example:

    1. machaao start -n sample-chatbot

    2. machaao tunnel -p [PORT] # If chatbot token is saved on path.

    3. machaao tunnel -p [PORT] -t [TOKEN]

    You need a valid FREE API key from https://messengerx.io for the server to work. You can
    sign up for a free account at https://portal.messengerx.io.
    """
    pass


@click.command()
@click.option('-n', type=str, default='.', help="Enter the name of project.")
def start(n):

    path = os.path.join(CURR_DIR, n)

    try:
        os.mkdir(path)
    except OSError:
        raise SystemExit(0)
    click.echo(f"initiating for {OS}")
    click.secho(f'Project {n} created...', fg="blue", bold=True)
    copyany(FILE_DIR+"/chatbot.py", path+"/")
    click.secho(f'Copying files to project directory...', fg="green", bold=True)
    click.secho(f'Project Created, Keep Developing Chat Bots', fg="blue", blink=True)


@click.command()
@click.option('-p', type=str, default='5000', help="Run tunnel to expose localhost to web.")
@click.option('-t', type=str, default=None, help="Run tunnel to expose localhost to web.")
@click.option('-h', type=int, default=None, help="get host name")
def tunnel(p, t, h):
    machaao_token = None

    if t != None:
        machaao_token = t

    if t == None:
        machaao_token = os.getenv("MESSENGERX_API_TOKEN", None)
        if machaao_token is None:
            sys.exit(" * Chatbot token not set")

    # Not the right way of doing it only doing it for testing.
    _ws_uri = f'wss://mx.tunnel.messengerx.io/_ws/?username={machaao_token}&port={p}'

    host = None

    loop = asyncio.get_event_loop()
    try:
        if h:
            host = loop.run_until_complete(
                machaao.generate_host_url(ws_uri=_ws_uri))
            click.echo(str(host))
        else:
            # print(f'Incoming tunnel params: {p}....... {t}')
            loop.run_until_complete(
                machaao.open_tunnel(
                    ws_uri=_ws_uri,
                    http_uri=f'http://127.0.0.1:{p}',
                )
            )

    except KeyboardInterrupt:
        click.echo("\nMachaao tunnel closed")

    except Exception as e:
        if int(str(e)[6:11]) == 1006:
            click.echo("\nDisconnected from MX")
            signal.signal(signal.SIGINT, exit_gracefully)
        else:
            print(e)
            print("Contact: support@messengerx.io")

#
# def sigterm_handler(signal, frame):
#     # save the state here or do whatever you want
#     print('booyah! bye bye')
#     sys.exit(0)


@click.command()
def version():
    click.echo("v0.3.2")


@click.command()
@click.option('-p', type=str, default='5000', help="Run tunnel to expose localhost to web.")
@click.option('-t', type=str, default=None, help="Run tunnel to expose localhost to web.")
def run(p, t):

    # print(f'Incoming server run params: {p}, {t}')

    _isPy = False
    _isGo = False

    if os.path.exists("chatbot.py"):
        _isPy = True

    elif os.path.exists("chatbot"):
        os.environ["PORT"] = p
        _isGo = True

    else:
        sys.exit(' * Chatbot file not present in directory')

    click.echo(
        f" * Validating & initializing chatbot for {OS}, please wait... (can take a minute or so)")

    if OS and 'windows' in OS:
        _p = subprocess.check_output(
            ["machaao", "tunnel", "-p", p, "-t", t, "-h", "1"], stderr=subprocess.STDOUT, shell=True)
    else:
        _p = subprocess.check_output(
            ["machaao", "tunnel", "-p", p, "-t", t, "-h", "1"], stderr=subprocess.STDOUT)

    validated = False
    if _p:
        try:
            _p = _p.decode("utf-8").strip()
            if "messengerx.io" in _p:
                validated = True
                click.echo(f" * Validated: {_p}")
        except Exception as e:
            print(str(e))
            validated = False

    if validated:

        try:
            click.echo(f" * Initializing a chatbot for {_p}")

            # _tunnel_port = eval(p) + 1

            click.echo(f" * Initializing tunnels for chatbot for {_p}:{p}")

            _children = []
            _tunnel_p = subprocess.Popen(shlex.split(
                f"machaao tunnel -p {p} -t {t}"), stderr=subprocess.STDOUT)

            _chatbot_p = None

            if _isPy:
                print("runing chatbot cmd")
                _chatbot_p = subprocess.Popen(shlex.split(
                    f'python3 chatbot.py -p {p}'), stderr=subprocess.STDOUT)

            if _isGo:
                _chatbot_p = subprocess.Popen(shlex.split(
                    './chatbot'), stderr=subprocess.STDOUT)

            click.echo(f" * Chatbot for {_p} is starting...")

            chatbot_url = f"https://{_p}/machaao/incoming"

            headers = {
                "api_token": t,
                "Content-Type": "application/json",
            }

            payload = {
                "url": chatbot_url
            }

            click.echo(f" * Updating the new hook for call to - {chatbot_url}")

            request(
                "POST", f'https://ganglia-dev.machaao.com/v1/bots/{t}', data=dumps(payload), headers=headers)

            _bot_name = _p.replace(".tunnel.messengerx.io", "")

            click.echo(click.style(
                f" * Your bot is now accessible @ https://dev.messengerx.io/{_bot_name}", bg="black", fg="white"))

            _chatbot_p.wait()

        except Exception as e:
            print(str(e))

    else:
        click.echo(" * oops, invalid request -- you being naughty my friend...")


cli.add_command(start)
cli.add_command(tunnel)
cli.add_command(run)
cli.add_command(version)


def exit_gracefully(signal, frame):
    if _tunnel_p:
        click.echo("terminating tunnel....")
        _tunnel_p.send_signal(signal.SIGINT)

    if _chatbot_p:
        click.echo("terminating chatbot....")
        _chatbot_p.send_signal(signal.SIGINT)

    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, exit_gracefully)
    cli()
