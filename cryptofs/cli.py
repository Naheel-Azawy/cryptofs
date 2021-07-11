import sys
import os
import getpass

from cryptofs.core import CryptoFSBase
from Crypto.Hash   import SHA256

class CryptoFS(CryptoFSBase):
    def __init__(self, root, mount, password):
        super(CryptoFS, self).__init__(root, mount)
        h = SHA256.new()
        h.update(password.encode())
        self.key = h.digest()

    def key_gen(self, path, iv):
        return self.key

def usage():
    print("usage: cryptofs <ROOT> <MOUNT>")

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        usage()
        return 1
    root  = args[0]
    mount = args[1]
    for d in [root, mount]:
        if not os.path.isdir(d):
            print(f"'{d}' is not a directory")
            return 1

    password = getpass.getpass("Password: ")
    fs = CryptoFS(root, mount, password)
    fs.start(foreground=False, allow_other=False)
    return 0
