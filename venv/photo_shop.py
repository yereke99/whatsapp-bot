from PIL import Image
import numpy as np



image = Image.open('MEa41e7906bb2b5559c21e204bec8acac3.pdf.jpg')
image_data = np.array(image)
print(image_data.shape)
crop = image_data[700:2000, 200:1995, :]
image_croped = Image.fromarray(crop)
image_croped.show(image_croped)






