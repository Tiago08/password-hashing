import argparse 
import hashlib

# parsing
parser = argparse.ArgumentParser(description="Hashing given passwords")
parser.add_argument('password', help='input pasword you want to hash')
parser.add_argument('-t', '--type', default='sha256', choices=['sha256', 'sha512', 'md5'])
args = parser.parse_args()

# hashing given passwords 
password = args.password
hashtype = args.type
m = getattr(hashlib, hashtype)()
m.update(password.encode())

# Output
print("< hash-type : " + hashtype + " >")
print(m.hexdigest())