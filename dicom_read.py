import glob
import numpy as np
import matplotlib.pyplot as plt
import sklearn.preprocessing import MinMaxScalar

data_dir ='-- file dir path  --'
files = glob.glob(data_dir + '/*.dcm')

X = []


ms = MinMaxScalar()

for file_name in files:
    data = pydicom.dcmread(file_name)
    data = np.array(data.pixel_array)
    data = data.astype('float32')
    data_norm = ms.fit_transform(data)
    X.append(data_norm)


np.save('data1',X)
