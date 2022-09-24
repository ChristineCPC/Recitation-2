# ***************************************************
# Delaware State University
# Division of Physics, Engineering, Mathematics, and
# Computer Science
# CSCI-121 Elements of Computer Programming II
# Recitation 2 - Input/Output and Crypto
# ***************************************************

def crypto(filename, cypher):
    fh = open(filename)
    file_content = fh.readlines()
    print(file_content)
    with open(filename, 'r') as fh, open(filename + '.enc', 'w') as fhenc:
        for line in fh:
            eLine = ''
            for ch in line:
                eLine += cypher(ch)
            fhenc.write(eLine)
            #print(eLine)
            with open (filename, 'w') as fh:
                fh.write(eLine)
            with open (filename) as fh:
                fh.readlines()




# DO NOT touch the lines below


if __name__ == "__main__":
    crypto('hello.txt', lambda x: chr((ord(x) + 5) % 256))