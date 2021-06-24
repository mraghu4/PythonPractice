import subprocess

cmd = subprocess.run(["ls"],stdout=subprocess.PIPE)
print(cmd.stdout)


p1 = subprocess.Popen(["ls"],stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep","os"],stdin=p1.stdout,stdout=subprocess.PIPE)
p2.communicate()
print(cmd.stdout)

print(subprocess.getstatusoutput("ls |grep os"))
