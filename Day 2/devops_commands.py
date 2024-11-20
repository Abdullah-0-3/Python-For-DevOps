import subprocess

def execute_command(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return print(process.stdout.decode())

execute_command('docker images')
