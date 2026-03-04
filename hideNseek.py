import tkinter as tk
from tkinter import filedialog
from PIL import Image



class img():
    """define methods for child classes storeMsg and retrieveMsg"""

    def __init__(self):
        """
        argument: nothing
        get the path, image object and pixel of the image using a file explorer interface"""
        self.path = self.getImg()
        self.image = Image.open(self.path)
        self.pixels = list(self.image.getdata())

    def getImg(self) -> str:
        """return the path of the file selected in file explorer interface"""
        root = tk.Tk()
        root.withdraw()

        filepath = filedialog.askopenfilename(
            title="Select an image",
            filetypes= [("Image files","*.png *.jpg *.jpeg")])

        if filepath:
            print("File selected successfully.")

        else:
            print("File selection cancelled.")
        
        return filepath

class storeMsg(img):
    """take msg from the user and store it in the selcted image"""

    def __init__(self,msg:str):
        """argumert: encrypted message to store in the image
        
        input the msg and select the image to store the message in"""
        super().__init__()
        self.msg = msg
        self.pixel_required = ((len(self.msg)*8)//3)+1
        self.newPixel = self.store()

    
    def store(self) -> list:
        """argument: nothing
        store the message in the image"""
        hideIn = self.pixels[:self.pixel_required]
        rows = len(hideIn)
        cols= len(hideIn[0])
        
        #converting each char in 8bits
        msg_bits = []
        for chr in self.msg:
            strbyte = (f"{ord(chr):08b}") #converting each char in 8bits
            for bit in strbyte:
                msg_bits.append(int(bit))

        #flatting the list from 2d to 1d
        flatlst = []
        for tup in hideIn:
            for ele in tup:
                flatlst.append((ele))     

        #treating the lsb of the pixels
        lsbtreatedlst = flatlst  
        for i in range(len(msg_bits)):
            lsbtreatedlst[i] = (lsbtreatedlst[i] & 0b11111110) | msg_bits[i] 

        #reshaping list to 2d from 1d
        lstShaped = []
        temprow = []
        for index in range(rows*cols):

            temprow.append(int(lsbtreatedlst[index])) 

            if (index+1)%cols == 0:
                lstShaped.append(tuple(temprow))
                temprow = []

        newpixel = self.pixels
        newpixel[:self.pixel_required] = lstShaped

        print("Message successfully stored.")
        return newpixel
        

    
    def saveImg(self):

        """argument: nothing
        rename and save the image in the selected folder"""
        root = tk.Tk()
        root.withdraw()
        folderpath = filedialog.askdirectory(title="Select a folder to save the image")
        imageName = input("Rename the image as: ")

        if folderpath:
            print("Folder selected successfully.")
            self.image.putdata(self.newPixel)
            self.image.save(folderpath +"\\" +imageName+".png")
            print("Image successfully saved.")

        else:
            print("Folder Selection cancelled.")
        
class retrieveMsg(img):
    """argument: nothing 
    retrieve the encoded message from the selected image"""
    def __init__(self):
        """argument: nothing
        retrieve the encoded message from the selected image"""
        super().__init__()
        self.encmsg = self.retrieveMsg()


    
    def retrieveMsg(self) -> str:
        """
        argument: nothing
        retrieve the encoded message from the selected image"""
        #flatting the list from 2d to 1d
        flatlst = []
        for tup in self.pixels:
            for ele in tup:
                flatlst.append((ele))

        #retrieving the lsb of each pixel
        retrievedmsgbits = []
        for ele in flatlst:
            retrievedmsgbits.append(ele & 0b00000001)


        #grouping bits in group of 8 to from a byte
        chrbytelst = []
        chrbyte = ""
        i=1
        for ele in retrievedmsgbits:
            chrbyte += str(ele)
            if i%8 == 0:
                chrbytelst.append(chrbyte)
                chrbyte =''
            i+=1


        #converting the bytes into the msg
        msgExtracted =""
        for chrinbyte in chrbytelst:
            ch = chr(int(chrinbyte, base=2)) #base 2 convert binary to integer
            msgExtracted+=ch
    
        return msgExtracted


    def getEncMsg(self):
        """argument: nothing
        returns the encoded message retrieved from the image"""
        return self.encmsg
