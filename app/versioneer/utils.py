import subprocess


def subprocess_run(command):
    return subprocess.run(
        command,
        shell=True,
        check=True,
        capture_output=True,
    ).stdout.decode()
