from PIL import Image as img

hand = img.open(r"C:\Users\rahul\Downloads\Photos\hand.jpeg")
width, height = hand.size

print(width,height)
print(len(list(hand.getdata())))
