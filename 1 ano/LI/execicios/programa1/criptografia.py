import hashlib
import os.path
import sys

cases = int(input("what hush test do you want to test: "))
if cases == 1:
    h = hashlib.md5()
    h.update("batata frita".encode("utf-8")) #adicionar dados
    h.update("sebola".encode("utf-8"))
    print(h.hexdigest())
elif cases == 2:
    h = hashlib.md5()
    h.update("A long sentence broken in two halves".encode("utf-8"))
    print(h.hexdigest())
elif cases == 3:
    import os.path
    if len(sys.argv) < 2:
        print ("Usage: python3 %s filename" % (sys.argv[0]))#does not print argv[0]?
        sys.exit (1)

    fname = sys.argv[1] # verify if it is a file
    if not os.path.exists(fname) or os.path.isdir(fname) or not os.path.isfile(fname):
        print(fname + " is not a file", file=sys.stderr)
        sys.exit (2)

from Cryptodome.Hash import MD5 
#h = MD5.new()
#h.update("A long sentence ".encode("utf-8"))
#h.update("broken in two halves".encode("utf-8"))
#print(h.hexdigest())
#------------------------------------




from Cryptodome.Cipher import ARC4
cipher = ARC4.new("chave".encode("utf-8"))
cryptogram = cipher.encrypt("Text".encode("utf-8"))
print(cryptogram)

os.write(1, cryptogram)
print("std")
print(f"std: {os.write(1, cryptogram)}")

# o 1 representa o descritor do stdout
print()
decipher = ARC4.new("chave".encode("utf-8"))
decrypted = decipher.decrypt(cryptogram)
print(decrypted.decode("utf-8"))