import os
import platform
import fileinput

park = []
for line in fileinput.input():
    park.append(line.rstrip())

print(park + "\n")

param = "-n" if platform.system().lower()=="windows" else "-c"
kumpul = "\n"

for ip in park:
    response = os.system("ping " + param + " 1 " + ip)

    if response == 0:
        print(response)
        kumpul += ip + " is up!\n"
    else:
        print(response)
        kumpul += ip + " is down!\n"

print(kumpul)

#Copyright © 2022 Aldi Satria. All rights reserved.
