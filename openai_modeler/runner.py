"""
    openai-modeler.py
    ------------------

    Runs the project.

    :copyright: 2019 MislavJaksic
    :license: MIT License
"""
import argparse
import json
import socket
import sys
from typing import Dict, Any

import openai
from loguru import logger

from openai_modeler.package_one import module_one
from openai_modeler.package_one.module_one import raise_exception
from openai_modeler.secrets import openai_api_key

log_message = "who={username}, what={object}/{status}"


def main() -> int:
    """main() will be run if you run this script directly"""

    openai.api_key = openai_api_key



    model = 'gpt-3.5-turbo'
    messages = [
        {"role": "system", "content": "You are a AWS engineer."},
        {"role": "user", "content": "Write a Lambda function that is triggered by an upload to the S3 bucket ..."},
        #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        #{"role": "user", "content": "Where was it played?"}
    ]
    temperature = 0.2
    max_tokens = 4000

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    data = {'request': {'model': model, 'messages': messages, 'temperature': temperature,
                        'max_tokens': max_tokens},
            'response': response}
    print(response)
    with open('request_response.jsonl', 'a') as file:
        json.dump(data, file)
        file.write('\n')

    return 0


def get_models():
    response = openai.Model.list()
    structure = json.loads(str(response))

    return [x['id'] for x in structure['data']]


def other() -> int:
    args = get_cli_arguments()

    setup_loguru()
    try:
        raise_exception()
    except:
        logger.exception(log_message, username="1", object=2, status=3)

    print("Command line interface arguments:{}".format(args))
    x = args["first"]
    y = args["second"]

    print(module_one.add(x, y))
    print(module_one.multiply(x, y))

    return 0


def get_cli_arguments() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(
        description="Welcome to the command line interface!",
        epilog="Thank you for using the program!",
    )

    parser.add_argument("-x", "--first", type=int, required=True, help="First number")
    parser.add_argument("-y", "--second", type=int, required=True, help="Second number")
    parser.add_argument(
        "-o",
        "--optional",
        type=int,
        nargs="?",
        const=1,
        default=1,
        help="Optional number",
    )
    parser.add_argument(
        "-list", "--multiple", action="append", help="Can be specified many times"
    )
    parser.add_argument(
        "-tuple",
        "--triple",
        nargs=3,
        metavar=("password", "username", "secret"),
        help="(password, username, secret) tuple",
    )
    parser.add_argument(
        "-move",
        "--move",
        choices=["rock", "paper", "scissors"],
        help="Can only input a choice",
    )

    return vars(parser.parse_args())


def setup_loguru() -> None:
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    config = {
        "handlers": [
            {
                "sink": sys.stderr,
                "diagnose": False,
                "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{extra[host]}</cyan>:<cyan>{extra[ip]}</cyan> | <cyan>{process}</cyan>:<cyan>{thread}</cyan> | <cyan>{module}</cyan>:<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>",
            },
            # {"sink": "file.log", "retention": "7 days", "compression": "zip", "serialize": True},
        ],
        "extra": {"host": host, "ip": ip},
    }

    logger.configure(**config)  # type: ignore


def run() -> None:
    """Entry point for the runnable script."""
    sys.exit(main())


if __name__ == "__main__":
    """main calls run()."""
    run()
