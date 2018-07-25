import sys
filename = sys.argv[1]
f = open(filename,"rb")
f.seek(1024)
data = f.read()
f.close()
j = 0

var = [0]*128

for i in range(0,128):
        var[j] = hex(ord(data[i]))
        j=j+1

Partition_Type_GUID = var[:16]
Unique_Partition_GUID = var[16:32]
First_LBA = var[32:40]
Last_LBA = var[40:48]
Attribute_Flags = var[48:56]
Partition_Name = var[56:128]

print "Partition_Type_GUID : "+" ".join(Partition_Type_GUID)
print "\n"
print "Unique_Partition_GUID : "+" ".join(Unique_Partition_GUID)
print "\n"
print "First_LBA : "+" ".join(First_LBA)
print "\n"
print "Last_LBA : "+" ".join(Last_LBA)
print "\n"
print "Attribute_Flags : "+" ".join(Attribute_Flags)
print "\n"
print "Partition_Name : "+" ".join(Partition_Name)
