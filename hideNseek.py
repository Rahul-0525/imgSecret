import tkinter as tk
from tkinter import filedialog
from PIL import Image



class img():

    def __init__(self):
        self.path = self.getImg()
        self.image = Image.open(self.path)
        self.pixels = list(self.image.getdata())

    def getImg(self) -> str:
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

    def __init__(self,msg:str):
        super().__init__()
        self.msg = msg
        self.pixel_required = ((len(self.msg)*8)//3)+1
        self.newPixel = self.store()

    
    def store(self):
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
        
i = storeMsg("hello how are you doing")
i.saveImg()





    
