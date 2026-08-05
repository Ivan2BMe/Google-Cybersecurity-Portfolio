# Script Name: update_allow_list.py
# Description: Algorithm for file updates in Python to manage server access allow lists.

# Assign the file name and the list of IP addresses that need to be removed[cite: 1]
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# 1. Open the file containing the allow list in read mode[cite: 1]
with open(import_file, "r") as file:

# 2. Read the file contents and convert it into a string stored in ip_addresses[cite: 1]
    ip_addresses = file.read()

# 3. Convert the string into a list using the .split() method[cite: 1]
ip_addresses = ip_addresses.split()

# 4. Iterate through the ip_addresses list and remove any address present in remove_list[cite: 1]
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

# 5. Convert the list back into a string separated by spaces[cite: 1]
ip_addresses = " ".join(ip_addresses)

# 6. Open the allow list file in write mode and overwrite it with the updated string[cite: 1]
with open(import_file, "w") as file:
    file.write(ip_addresses)
