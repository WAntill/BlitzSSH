import BlitzSSH_Improved

def main():
    try:
        BlitzSSH_Improved.make_IP_List()
    except:
        print("Failed to set IPs")
    try:
        BlitzSSH_Improved.get_Passwords()
    except:
        print("Failed to set Passwords")
    try:
        BlitzSSH_Improved.get_Users()
    except:
        print("Failed to set Users")  
    try:
        BlitzSSH_Improved.run_Attack()
    except:
        print("Failed to run attack")

if __name__ == "__main__":
    main()