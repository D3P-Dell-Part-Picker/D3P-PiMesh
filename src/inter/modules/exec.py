import os
import sys
import multiprocessing
import src.misc.primitives as primitives

_primitives = primitives.Primitives('Client', 'Debug')


def initiate(message, allow_command_execution):
    from src.client.client import Client
    _client = Client()

    # Assuming allow_command_execution is set, execute arbitrary UNIX commands in their own threads.
    if allow_command_execution:
        command = message[5:]
        _primitives.log(str("executing: " + command), in_log_level="Info")

        # Warning: This is about to execute some arbitrary UNIX command in it's own nice little
        # non-isolated fork of a process. That's very dangerous.
        command_process = multiprocessing.Process(target=_client.run_external_command,
                                                  args=(command,), name='Cmd_Thread')
        command_process.start()

    # allow_command_execution is not set, don't execute arbitrary UNIX commands from the network.
    else:
        _primitives.log(("Not executing command: ", message[5:]), in_log_level="Info")
