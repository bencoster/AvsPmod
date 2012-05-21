#----------------------------------------------------------------------
# This file was generated by img2py.py
#
from wx import ImageFromStream, BitmapFromImage
from wx import EmptyIcon
import cStringIO, zlib


def getData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\n \xcc\xc1\x06\
$\x8b\xab\xaa\xbe\x00)\x96b\'\xcf\x10\x0e \xa8\xe1H\xe9\x00\xf2K=]\x1cC"Z\
\xdf^\xdf\xcd{\xc0\x80\x83\xe5B\xc3\xe6\xff\xc7\xcc^\x06}\xb6ty\xf8\x99\xe1\
\xced\x1e\x8f\x8e\x17Uj\xf3\xfb\x96\t;00\xca5\xcc\xcd-\xdb\xd6\xcb\xb8K\xf1\
\xa1\xbe\x83\xf3%\xdb\x86\xa6)\xb37p5\xfa:\x8a1\xc9\x1f\xd6X\x92\xcb_\xa1\
\xf8\xb8\xfb\xc5[-\x9d]),\x0fx\xdb\x98\x17\x1d4p0\xdb\xc1\xb3\x82m9\xe3\x8a\
\x07\x06\x0c\xb2\x7f\xae?\x8d\x05\x1as\x9d\xd9n\x9b\x9a\x83\x14\x7f\xd4\x16\
\x0e\xa0\x03\x18<]\xfd\\\xd69%4\x01\x00\xde\x8a@x' )

def getBitmap():
    return BitmapFromImage(getImage())

def getImage():
    stream = cStringIO.StringIO(getData())
    return ImageFromStream(stream)

def getIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getBitmap())
    return icon

