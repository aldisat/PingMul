import os
import platform

with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(f" {park}  \n")

param = "-n" if platform.system().lower()=="windows" else "-c"
kumpul = ""

for ip in park:
    response = os.system("ping " + param + " 1 " + ip)

    if response == 0:
        print(response)
        kumpul += ip + " is up!\n"
    else:
        print(response)
        kumpul += ip + " is down!\n"

print(kumpul)
