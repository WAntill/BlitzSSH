import BlitzSSH_Utils

def main():
    try:
        BlitzSSH_Utils.make_IP_List()
    except:
        print("Failed to set IPs")
    try:
        BlitzSSH_Utils.get_Passwords()
    except:
        print("Failed to set Passwords")
    try:
        BlitzSSH_Utils.get_Users()
    except:
        print("Failed to set Users")  
    try:
        BlitzSSH_Utils.run_Attack()
    except:
        print("Failed to run attack")

if __name__ == "__main__":
    main()