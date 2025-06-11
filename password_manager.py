from cryptography.fernet import Fernet #module which allows to encrypt text

'''
def write_key():
     key=Fernet.generate_key()
     with open("key.key", "wb") as key_file:# it will create the file 'key.key'
          key_file.write(key)               #in 'wb' mode (write in bytes)'''


def load_key():
     file=open("key.key", "rb")
     key=file.read()
     file.close()
     return key

master_pwd=input("What is the master password? ")
key=load_key() + master_pwd.encode()
fer=Fernet(key)




def view():
    with open('passwords.txt', 'r') as f: 
        for line in f.readlines():
            data=line.rstrip() #rstrip will strip off the cariage return from our line
            user,passw=data.split("|") #the'.split' will split the content of the file (string) from where the pipe character is found
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode() + "\n")

def add():
    name=input("Account name:")
    pwd=input("Password:")

#while using "with" you dont have to manually close the opened file and
#'a' is for append mode(allows to add something to the end of the existing file and if file doesn't exists it creats a new one)
    with open('passwords.txt', 'a') as f: 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")# encode converts strings into bytes


while True:
    mode=input("Would you like to add a new password or view existing ones (view,add), press q to quit? ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode")
        continue
