import subprocess
process = subprocess.Popen(['python3', 'real_time_ml_script.py'], strip)

while True:
    output = process.stdout.readline()
    if output == b''and process.poll() is not None:
        break
    if output:
        print(f'Received: {output.strip().decode()}')