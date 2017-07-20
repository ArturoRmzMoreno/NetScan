# Twitter: @Arturo1337

import os

os.system ("clear") 

print " _   _      _    _____                 "
print "| \ | |    | |  / ____|  Twitter: Arturo1337"
print "|  \| | ___| |_| (___   ___ __ _ _ __  "
print "| . ` |/ _ \ __|\___ \ / __/ _` | '_ \ "
print "| |\  |  __/ |_ ____) | (_| (_| | | | |"
print "|_| \_|\___|\__|_____/ \___\__,_|_| |_|\n"

print "Comenzando Escaneo...\n"

for redlocal in range(0,256):
    ip = "192.168.0." + str(redlocal)
    respuesta = os.system("ping -c 1 " + ip)
    if respuesta == 0:
            print chr(27)+"[1;31m"+"[ Servidor en Linea ]\n"+chr(27)+"[0m"