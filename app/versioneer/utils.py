import subprocess


def subprocess_run(command):
    return subprocess.run(
        command,
        shell=True,
        check=True,
        capture_output=True,
    ).stdout.decode()


def powershell_subprocess_run(command):
    command = ['powershell', command]
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        shell=True,
        creationflags=0x08000000
    )
    proc.wait()
    return proc.stdout.read().decode()
