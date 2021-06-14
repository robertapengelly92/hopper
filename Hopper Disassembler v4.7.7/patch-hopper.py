import sys, hashlib, os

assert str is not bytes, "Get this shit you call python outta here!"

print("Hopper 4.7.7 for Linux - Crack")
print()

if len(sys.argv) != 2:
    print("Usage: python %s [path to binary]" % sys.argv[0])
    sys.exit(1)

os.rename(sys.argv[1], sys.argv[1] + ".old")

with open(sys.argv[1] + ".old", 'rb') as inp:
#with open(sys.argv[1], 'rb') as inp:
    data = inp.read()

if data[:4] != b'\x7fELF':
    print("Error: the input is not an ELF file. Please pass the Hopper executable as input.")
    sys.exit(1)

digest = hashlib.sha3_224(data).hexdigest()

#print (digest)
#sys.exit (1)

if digest != "cf1b2c8ef74ea420439eeabfb552c16cf9ccde3fe421591501f48c6d":
    print("Error: the input digest does not match. Either this file has already been patched, or this is not the correct version of Hopper.")
    sys.exit(1)

patch_addr = 0x1035F0
patch_data = b'\xb8\x01\x00\x00\x00\xc3'

#print (data[patch_addr:patch_addr+len(patch_data)])
#sys.exit (1)

with open(sys.argv[1], 'wb') as out:
    out.write(data[:patch_addr])
    out.write(patch_data)
    out.write(data[patch_addr+len(patch_data):])

os.chmod(sys.argv[1], 0o755)

print("%s has been patched successfully." % sys.argv[1])
