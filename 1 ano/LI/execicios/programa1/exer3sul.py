from Cryptodome.Hash import SHA256
#cant import the above
import sys

h = SHA256.new()
if len(sys.argv) < 2:
    print("usage: python3 +++++")
    sys.exit(1)

f = open(sys.argv[1],"rb")

buffer= f.read(512)
while len(buffer) > 0:
    h.update(buffer)
    buffer =f.read(512)
f.close()
print(h.hexadigest())