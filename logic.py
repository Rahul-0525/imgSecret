


def hidemsg(msg:str,hideIN:list) -> list:
    """Take msg and nested list as argument and then store the msg secretly in the list itself """
    #this is the array to hide the data in

    rows = len(hideIN)
    cols= len(hideIN[0])


    # the below converts the msg into a list of bits where 8 bits each represents a character

    msg_bits = []
    for chr in msg:
        strbyte = (f"{ord(chr):08b}")
        for bit in strbyte:
            msg_bits.append(int(bit))
    # print(msg_bits)
    # print()



    #this convert the nested list into a single list of elements this way its easier to apply bitwise and or operation on them 
    flatlst = []
    for lst in hideIN:
        for ele in lst:
            flatlst.append((ele))
    # print(flatlst)
    # print()

    #below turns all the numbers byte's lsb to 0 and then perform or operation with the msg_bits element to hide the msg in the num

    lsbtreatedlst = []
    for ele in flatlst:
        lsbtreatedlst.append(ele&0b11111110)
    # print(lsbtreatedlst)
    # print()
    # print()

    for i in range(len(msg_bits)):
        lsbtreatedlst[i] = lsbtreatedlst[i] | (msg_bits[i])
    # print(lsbtreatedlst)
    # print()
    # print()

    # below turn the lsbtreatedlst which is flat back into the nested form as it was
    lstShaped = []
    temprow = []
    for index in range(rows*cols):

        temprow.append(int(lsbtreatedlst[index])) 

        if (index+1)%cols == 0:
            lstShaped.append(temprow)
            temprow = []
    # print(lstShaped)

    return lstShaped
        

#now i have done the work of hiding the msg now write code to retrieve the code that is hidden
#where i have stored the msg in first len(msg_bits) bits but that can change by randomly or using some different starting point for 
#storing the msg 


def retrieveMsg(mainlist:list) -> str:
    """take the list storing the secret as the input and extract and return the msg stored inside it"""



    #this convert the nested list into a single list of elements this way its easier to apply bitwise and or operation on them 
    flatlst = []
    for lst in mainlist:
        for ele in lst:
            flatlst.append((ele))
    # print(flatlst)
    # print()


    # this apply bitwise & on all the flat list to retrieved the stored msg in lsb as bits
    retrievedmsgbits = []
    for ele in flatlst:
        retrievedmsgbits.append(ele & 0b00000001)
    # print(retrievedmsgbits)


    #this group the bits in 8 to form the 1byte representing each character of the message
    chrlst = []
    chrbyte = ""
    i=1
    for ele in retrievedmsgbits:
        chrbyte += str(ele)
        if i%8 == 0:
            chrlst.append(chrbyte)
            chrbyte =''
        i+=1

    # print(chrlst)

    #converting the chrbytes back into the characters and joining them in to form the msg back
    msgExtracted =""
    for chrinbyte in chrlst:
        ch = chr(int(chrinbyte, base=2))
        msgExtracted+=ch
    
    return msgExtracted











hideIN = [
        [154, 203,  45,  87,  12,  99, 231,  64],
        [ 33, 178, 222,  56, 199,  10, 145,  77],
        [ 89,  34, 201, 167,  90, 255,  61, 142],
        [ 73,  58, 129, 244,  38,  11,  92, 200],
        [111,  62,  14, 219, 176,  88, 134,  27],
        [240,  95,  53, 168,  72, 181,  49,  66],
        [ 21, 137, 159,  80, 212, 104,  35, 190],
        [170,  44, 126,  98, 147,  69,  23, 205]]

msg = "hey my"
mainlist = hidemsg(msg,hideIN)

msgretrieved = retrieveMsg(mainlist)
print(msgretrieved)
