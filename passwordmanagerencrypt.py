import sys
from cryptography.fernet import Fernet

#for the encryption need to pip install cryptography module

#Function to decrypt
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

while True:
    master_pwd = input("Enter your master password: ").lower()
    if master_pwd == "intech.2018":
        break

    if master_pwd == "q":
        sys.exit()
    else:
        print("invalid master password! Try again or q to quit")
        continue

key = load_key() + master_pwd.encode()
fer = Fernet(key)



#Function for view
def view():
    with open("passwordsencrypt.txt", "r") as f:
        for line in f.readlines():
            #print(line.rstrip())  #code with | in the result
            #rstrip to remove the next blank line.
            data = line.rstrip()
            user, passwd = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passwd.encode()).decode())
            #This will print user and password in organize way.


def add():
    name = input("Account Name: ").lower()
    pwd = input("Account Password: ").lower()

    # Create a file whrere username and and password will be stored.
    #"a" mode to create new file and add the new in the end of the file
    #other mode is r which is read and w for
    #f.write is f is the name of the file.
    with open("passwordsencrypt.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

#Functions for encryption
""" 
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""

#need only to run once or 1 time. write_key()
#write_key()


while True:
    action_mode = input("Would you like to add or view password? (add/view), or press q to quit. ").lower()
    if action_mode == "q":
        break

    if action_mode == "add":
        add()

    elif action_mode == "view":
        view()

    else:
        print("Invalid input. Please try again.")
        continue

print("Thank you for using Password Manager!")
