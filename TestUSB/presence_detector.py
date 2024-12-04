import subprocess
from countdownSpeak import countdownOne
# from countdownSpeak import countdownTwo

# Find Mac Addresses Function
def find_mac_addresses(target_macs, ip_range="192.168.0.177/24"):
    result = subprocess.check_output(f"sudo nmap -sn {ip_range} | grep MAC", shell=True)
    found_macs=[]
    for mac in target_macs: 
         if mac.lower() in str(result).lower():
             found_macs.append(mac)
             

    return found_macs


# Test code
if __name__ == "__main__":
    # Example list of target MAC addresses to search for on the network
    target_macs = [
        "04:E8:B9:07:9D:7E",  # Replace with actual MAC addresses you expect to find
        "11:22:33:44:55:66"
    ]

    print("Scanning network...")
    # Call the function to find the specified MAC addresses
    found_devices = find_mac_addresses(target_macs)

    # Display the result
    if found_devices:
        print(f"Found devices:{found_devices}")
        countdownOne()
        
    else:
        print("No target MAC addresses found on the network.")



# countdownTwo()