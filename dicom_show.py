
import pydicom
import matplotlib.pyplot as plt

data = pydicom.dcmread(' -- file name -- ')
data = data.pixel_array
plt.imshow(data)
plt.show()


