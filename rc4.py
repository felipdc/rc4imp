# RC4 implementation in python made by Felipe Tiago De Carli.
# If you are going to use this code, please keep the author name on it.

SIZE = 256

i = 0

j = 0

#initialize s_box:
    
s_box = [None]*SIZE

    #fill s_box array
    
for i in range(SIZE):
        
    s_box[i] = i

# Key to use

key_string = 'Chave'

# Converting str to int

key = [None]*len(key_string)

for i in range(len(key_string)):

    key[i] = ord(key_string[i])

def KSA():

    global i

    global j
    
    #operations to get j

    for i in range(SIZE):

        j = (j + s_box[i] + key[i%len(key)])%SIZE

        s_box[i], s_box[j] = s_box[j], s_box[i]
        
KSA()


def PRGA():

    global i

    global j

    result = [None]*len(key_string)

    for k in range(len(key_string)):

        i = (i + 1) % SIZE
        
        j = (j + s_box[i]) % SIZE

        s_box[i], s_box[j] = s_box[j], s_box[i]

        
        
PRGA()
