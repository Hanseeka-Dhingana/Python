# Generate the qr code

import qrcode
data = "Hanseeka Dhingana"  #load your data here in any form 

qr = qrcode.make(data)

qr.save("qrcode.png")
print("Qrcode generated successfully")

