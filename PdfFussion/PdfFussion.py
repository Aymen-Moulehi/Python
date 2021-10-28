import os
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()
path = '/home/aymen/Desktop'

files = os.listdir(path)
test=[]
for f in files:
	if 'pdf' in f:
		test.append(f)



test.sort()


for pdf in test:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
