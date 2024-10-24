import subprocess

urls = []

with open("URLsToCheck.txt", "rt") as f:
    for x in f:
        urls.append(x)
if not f.closed:
    f.close()

for host in urls:
    try:
        ping = subprocess.getoutput(f"ping -w 2000 {host}")
        print(ping)
    except:
        print(f"{host} is unreachable")