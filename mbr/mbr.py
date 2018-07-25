import sys
import struct
filename = sys.argv[1]
f = open(filename,"rb")
data = f.read(512)
f.close()

var = [0]*66
j = 0

for i in range(446,512):
        var[j] = format(ord(data[i]),'02x')
        j += 1


def print_mbr(var):
	print"\n"
        print "Starting CHS Address : "+var[0]
        print "Partition CHS Address : "+" ".join(var[1:4])
        print "Partition Type : "+"".join(var[4])
        print "Ending CHS Address : "+" ".join(var[5:8])
	print "Starting LBA Address : "+" ".join(var[8:12])+ "-> little endian"
        print "Size in Sector : "+" ".join(var[12:16])+"->little endian * 512"
	print "==============================================="
Partition_Table1 = print_mbr(var[0:16])
Partition_Table2 = print_mbr(var[16:32])
Partition_Table3 = print_mbr(var[32:48])
Partition_Table4 = print_mbr(var[48:64])



