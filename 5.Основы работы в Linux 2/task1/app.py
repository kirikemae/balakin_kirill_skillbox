import os
import shlex
import signal
import subprocess
from typing import List
from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    if not isinstance(port, int):
        raise ValueError

    pids: List[int] = []
    cmd = f"lsof -i :{port}"
    args = shlex.split(cmd)
    output = subprocess.run(args, capture_output=True)
    result = str(output.stdout).split('\\n')[1:]

    for i in result:
        if len(i) > 1:
            pids.append(int(i.split()[1]))
    return pids


def get_port(port: int) -> None:
    pids: List[int] = get_pids(port)
    for pid in pids:
        if pids:
            os.kill(pid, signal.SIGINT)


def run(port: int) -> None:
    get_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)