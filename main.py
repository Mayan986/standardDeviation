
import StandardDeviation as sd

print("Enter no. of sample")
num = [int(x) for x in input().split()]
sddiv=sd.standardDeviation(num)
print(sddiv)
