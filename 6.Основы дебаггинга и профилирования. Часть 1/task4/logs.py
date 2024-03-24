import json
import shlex
import subprocess
from typing import Dict
from collections import Counter

with open('skillbox_json_messages.log', 'r', encoding='utf-8') as f:
    file = f.readlines()

def count_msg_each_levels() -> Dict[str, int]:
    level = {}

    for line in file:
        json_line = dict(json.loads(line))
        level.setdefault(json_line['level'], 1)
        level[json_line['level']] += 1
    return level


def most_logs_per_hour() -> int:
    time = {}
    for line in file:
        json_line = dict(json.loads(line))
        time.setdefault(json_line['time'][:2], 1)
        time[json_line['time'][:2]] += 1

    count_time = Counter(time).most_common()
    return int(count_time[0][0])


def logs_critical_per_20_min() -> int:
    pattern = '"time": "05:[0-2]0:..", "level": "CRITICAL"'
    cmd = f"grep -c '{pattern}' skillbox_json_messages.log"
    args = shlex.split(cmd)
    output = subprocess.run(args, capture_output=True)
    result = int(output.stdout.decode())
    return result


def count_logs_with_dog() -> int:
    pattern = 'dog'
    cmd = f"grep -c '{pattern}' skillbox_json_messages.log"
    args = shlex.split(cmd)
    output = subprocess.run(args, capture_output=True)
    result = int(output.stdout.decode())
    return result


def most_word_in_warning_logs() -> str:
    messages = []
    for line in file:
        json_line = dict(json.loads(line))
        if json_line['level'] == 'WARNING':
            messages.extend(json_line['message'].encode().split())

    count_word = Counter(messages)
    word = count_word.most_common(1)[0][0].decode()
    return word
