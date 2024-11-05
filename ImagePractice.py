from PIL import Image
mac = Image.open('my_computer_image.jpg')
print(type(mac))
#print(mac)
#mac.show()
size = mac.size
print(size)
var1 = mac.filename
#print(var1)
format1 = mac.format_description
#print(format1)
image1=mac.crop((0,0,500,500))
#image1.show()

halfway = 330/2
x: float = halfway - 200
w = halfway + 200
y = 500
z = 650
image2 = mac.crop((x,w,y,z))
image2.show()
red = Image.open('red_color.jpg')
red.show()