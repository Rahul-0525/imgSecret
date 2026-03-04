


def hidemsg(msg:str,hideIN:list) -> list:
    """Take msg and nested list as argument and then store the msg secretly in the list itself """
    
    #hideIN is the array to hide the data in
    rows = len(hideIN) #finding it to be able reshape it later after flatting the list
    cols= len(hideIN[0])


    # the below converts the msg into a list of bits where 8 bits each represents a character
    msg_bits = []
    for chr in msg:
        strbyte = (f"{ord(chr):08b}") #converting each char in 8bits
        for bit in strbyte:
            msg_bits.append(int(bit)) # store whole text as bits where each 8 bit represent a char
    # print(msg_bits)
    # print()

    #this convert the nested list into a single list of elements this way its easier to apply bitwise 
    # and or operation on them 
    flatlst = []
    for tup in hideIN:
        for ele in tup:
            flatlst.append((ele))
    # print(flatlst)
    # print()

    #below turns all the numbers's lsb to 0 using bitwise and, and then perform or operation with the msg_bits element to hide the 
    # msg in the num
    lsbtreatedlst = flatlst
    # for ele in flatlst:
    #     lsbtreatedlst.append(ele&0b11111110)
    for i in range(len(msg_bits)):
        lsbtreatedlst[i] = (lsbtreatedlst[i] & 0b11111110) | msg_bits[i] # bitwise operation with binary gives
        #binary as the ans where binary is represented by 0b

    # print(lsbtreatedlst)
    # print()
    # print()

    # for i in range(len(msg_bits)):
    #     lsbtreatedlst[i] = lsbtreatedlst[i] | (msg_bits[i])
    # print(lsbtreatedlst)
    # print()
    # print()

    # below turn the lsbtreatedlst which is flat back into the nested form as it was and return it as it
    lstShaped = []
    temprow = []
    for index in range(rows*cols):

        temprow.append(int(lsbtreatedlst[index])) 

        if (index+1)%cols == 0:
            lstShaped.append(tuple(temprow))
            temprow = []
    # print(lstShaped)

    return lstShaped
        


def retrieveMsg(mainlist:list) -> str:
    """take the list storing the secret as the input and extract and return the msg stored inside it"""


    #this convert the nested list into a single list of elements this way its easier to apply bitwise and or operation on them 
    flatlst = []
    for tup in mainlist:
        for ele in tup:
            flatlst.append((ele))
    # print(flatlst)
    # print()

    # this apply bitwise & on all the flat list to retrieved the stored msg in lsb as bits by extracting the
    #lsb out only and turning all other bits to 0
    retrievedmsgbits = []
    for ele in flatlst:
        retrievedmsgbits.append(ele & 0b00000001)
    # print(retrievedmsgbits)

    #this group the bits in 8 to form the 1byte representing each character of the message
    chrbytelst = []
    chrbyte = ""
    i=1
    for ele in retrievedmsgbits:
        chrbyte += str(ele)
        if i%8 == 0:
            chrbytelst.append(chrbyte)
            chrbyte =''
        i+=1

    # print(chrlst)

    #converting the chrbytes back into the characters and joining them in to form the msg back
    msgExtracted =""
    for chrinbyte in chrbytelst:
        ch = chr(int(chrinbyte, base=2)) #base 2 convert binary to integer
        msgExtracted+=ch
    
    return msgExtracted











# hideIN = [
#         (154, 203,  45,  87,  12,  99, 231,  64),
#         ( 33, 178, 222,  56, 199,  10, 145,  77),
#         ( 89,  34, 201, 167,  90, 255,  61, 142),
#         ( 73,  58, 129, 244,  38,  11,  92, 200),
#         (111,  62,  14, 219, 176,  88, 134,  27),
#         (240,  95,  53, 168,  72, 181,  49,  66),
#         ( 21, 137, 159,  80, 212, 104,  35, 190),
#         (170,  44, 126,  98, 147,  69,  23, 205)]

# where in the real case scenario of image i will have list of lakhs or crore of tuple so i want to get only the
# number of tuple that 
# number of bits i require to store the msg in which equals to (len(msg)*8)/3 tuples simply so if pixels 
# is the lst of tuple of pixel


# msg = "hey there so this is the password: Smashing@25Power this is written to longen the message as much as i can to check the limit"

# from PIL import Image as img

# hand = img.open(r"C:\Users\rahul\Downloads\Photos\castle_palace_manor_124492_2560x1440.jpg")

# pixel = list(hand.getdata()) #getting all pixels as list of tuple of rgb

# tplchanging = ((len(msg)*8)//3)+1 #these number of tuple we want only to store the data

# hideIN = pixel[:tplchanging] #hence taking only those and storing msg in them
# mainlist = hidemsg(msg,hideIN)

# pixel[:tplchanging] = mainlist #replacing the actual typle with the tuple with hidden msg 

# hand.putdata(pixel)
# hand.save("done2.png")


# so the above code take the message and save the msg in the image and save the image as done.png

#where the code below just took the image and tried to find the msg in it which actually worked. the image
#officially now have the msg in it and can be recieved by the code below
from PIL import Image

hand = Image.open(r"C:\Users\rahul\Downloads\stored in.png")
pixel = hand.getdata()
print(retrieveMsg(pixel))



'''
TODO:
2. see a way to encrypt ande decrypt the message for more security,
where the encryption key will me made using a master password which will be used to decrypt the msg in the image 
3. see a way to store the length of the message as that allow to read, change and pass only the part of the 
tuple that have the msg not anything else
4. see a way to like not to store the msg in the starting tuple only but anywhere in the middle
for that just needed a number to put here pixel[a:tplchanging] in place of 'a' and a method to store it and 
encrypt it also
5. then at last see how to open that window that allow you to browse and open image and save in any desired location
6. convert this messy logic file into two file each for retrieving and storing the msg and keep the main
for managing it and manipulating the image
'''