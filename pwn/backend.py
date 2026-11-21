import subprocess
r=subprocess.check_output("id;uname -a;hostname;cat /etc/passwd",shell=True)
open("/tmp/lai84277.txt","wb").write(r)
