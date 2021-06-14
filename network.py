#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Solucion de caracteres especiales tildes y ñ con coding: latin-1

# Aplicación para agilizar proceso de asignación de Direcciones IP en el equipo
# Nota: se necesita tener el nombre de la conexión de area local sin tildes

'''
determinar tiempo por secuencia
$ python3 -m timeit -n 3 "import time; time.sleep(3)"
3 loops, best of 5: 3 sec per loop

'''

from tkinter import *
import os, subprocess
import tkinter
import tkinter.font as tk_font
import time

#https://realpython.com/python-sleep/
import threading


#ping
import platform    # For getting the operating system name


FONT = "Consolas 10"
retval = os.getcwd()
print(retval)


def find_text_variable(variable,text):
    #print(text)
    value = variable.find(text)
    #print("value:", value)
    return value


def extract_text(file,start_char,number_of_chars):
    file = open(file, "r+")
    text=file.read()
    #print(text)
    text_extracted=text[start_char:start_char + number_of_chars]
    #print("value:", value)
    return text_extracted

def VentanaTemp(archivo):
    temp = Toplevel()
    temp.geometry("600x200")
    texto = Text(temp, width=90, height=12, wrap='none', font=FONT)
    texto.grid(row=6, column=1, columnspan=2, sticky=W)
    texto.insert(0.0, archivo)
    botonTemp = Button(temp, text="Cerrar", command=temp.destroy, takefocus=0)
    botonTemp.grid(row=15, column=1)
    botonTemp.focus_set()


def ping1():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")

    text1 = 'ping '
    text2 = ip.get()
    # print(ip)
    text3 = ' -n 1'
    textf = text1 + text2 + text3
    print(textf)
    subprocess.call(textf, shell=True, stdout=outf, stderr=errf)

    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()

    VentanaTemp(output)

    # temp=Tk()
    # text2=Text(temp, width=90,height=12,wrap='none',font="Consolas 10")
    # text2.grid(row=6,column=1,columnspan=2,sticky=W)
    # text2.insert(0.0,output)


def VerInterfaces():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('netsh interface show interface', shell=True, stdout=outf, stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()
    VentanaTemp(output)

    # temp=Tk()
    # temp.geometry("600x200")
    # text2=Text(temp, width=90,height=12,wrap='none',font="Consolas 10")
    # text2.grid(row=6,column=1,columnspan=2,sticky=W)
    # text2.insert(0.0,output)
    # bottemp=Button(temp, text="Cerrar", command=temp.close())
    # bottemp.grid(row=6,column=2,columnspan=2,sticky=W)


def verip():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    #subprocess.call('netsh interface ip show addresses name=\"Conexion de area local\"', shell=True, stdout=outf,
    # stderr=errf)
    subprocess.call('netsh interface ip show addresses', shell=True, stdout=outf,
                    stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()

    VentanaTemp(output)

    # temp=Tk()
    # text2=Text(temp, width=90,height=10,wrap='none',font="Consolas 10")
    # text2.grid(row=6,column=1,columnspan=2,sticky=W)
    # text2.insert(0.0,output)


def dhcp():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('netsh interface ip set address \"Conexion de area local\" dhcp', shell=True, stdout=outf,
                    stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()
    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()
    time.sleep(3)
    verip()


def ip_1():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('netsh interface ip set address \"Conexion de area local\" static 192.168.0.5 255.255.255.0',
                    shell=True, stdout=outf, stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()
    time.sleep(3)
    verip()


def ip_2():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('netsh interface ip set address \"Conexion de area local\" static 192.168.1.5 255.255.255.0',
                    shell=True, stdout=outf, stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()
    time.sleep(3)
    verip()


def ip_3():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('netsh interface ip set address \"Conexion de area local\" static 192.168.1.184 255.255.255.0',
                    shell=True, stdout=outf, stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()
    time.sleep(3)
    verip()


def ip_x():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    text1 = 'netsh interface ip set address \"Conexion de area local\" static '
    text2 = ipx0.get()
    text3 = ' 255.255.255.0'
    textf = text1 + text2 + text3
    print(textf)
    # subprocess.call(['netsh interface ip set address \"Conexion de area local\" static ',ipx0.get(),' 255.255.255.0'], shell=True, stdout=outf,stderr=errf)
    subprocess.call(textf, shell=True, stdout=outf, stderr=errf)

    outf.close()
    errf.close()

    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()
    time.sleep(3)
    verip()

def ping_online(host="8.8.8.8"):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    result = subprocess.run(command,check=True, stdout=subprocess.PIPE, universal_newlines=True)
    return result.stdout

def ping_box(x):
    #https://stackoverflow.com/questions/2953462/pinging-servers-in-python

    button_ok = Label(vent, text="ok", bg='green', width=2, height=2)
    button_nok = Label(vent, text="nok", bg='red', width=2, height=2)



    result = ping_online("8.8.8.8")
    #print(result[1:8])
    text="tiempo="

    print(result)
    print(result.find(text))

    #if result.find(text) == True:
    find_text = result.find(text)
    count_text = len(text)
    start_char = find_text + count_text
    find_final = result.find("ms ")
    time = result[ start_char : find_final]
    text = Label(vent, text= time, width=2, height=2)


    #print(result)
    #print(find_text , " " , count_text , " " , start_char , " " , time)
    #print(type(time))

    x_value = 140

    if int(time) > 0:
        button_ok.place(x=x, y=200)
        text.place(x=x,y=230)

    else:
        button_nok.place(x=x, y=200)



def ping_extendido(qty=10):
    #default initial x:140
    x_value=140

    i=0
    while i < qty:
        ping_box(x_value)
        event = threading.Event()
        event.wait(1)
        x_value=x_value+25
        vent.update()

        flag = int(ping_flag.get())
        print(flag)
        print(i)
        print(qty)

        tmp_qty = qty-1
        if flag == 1 and i == tmp_qty:
            print("igual")
            i=0
            x_value = 140
        else:
            i += 1

        print(i)


def google():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('ping 8.8.8.8 -n 1', shell=True, stdout=outf, stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()

    VentanaTemp(output)


def deactred():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('netsh interface set interface \"Conexion de area local\" disabled', shell=True, stdout=outf,
                    stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()


def actred():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('netsh interface set interface \"Conexion de area local\" enabled', shell=True, stdout=outf,
                    stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()


def CambiarNombreInterface():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    comando = 'netsh interface set interface name=\"Conexión de área local\" newname=\"Conexion de area local\"'
    subprocess.call(comando, shell=True, stdout=outf, stderr=errf)
    print(comando)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()


def centrar(ventana):
    ventana.update_idletasks()
    w = ventana.winfo_width()
    h = ventana.winfo_height()
    extraW = ventana.winfo_screenwidth() - w
    extraH = ventana.winfo_screenheight() - h
    ventana.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))


def JustAbajo(ventana):
    ventana.update_idletasks()
    w = ventana.winfo_width()
    h = ventana.winfo_height()
    extraW = ventana.winfo_screenwidth() - w
    extraH = ventana.winfo_screenheight() - h
    ventana.geometry("%dx%d%+d%+d" % (w, h, extraW - 50, extraH - 100))


def ipactual():
    labelipactual = Label(vent, text="IP Actual")
    labelipactual.place(x=250, y=50)

    entipact = Entry(vent, textvariable=ipactual, width=15)
    entipact.place(x=250, y=60)

    # ent1.insert(0,"192.168.0.1")


def arp():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('arp -a', shell=True, stdout=outf, stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()
    time.sleep(5)
    VentanaTemp(output)




vent = Tk()
vent.geometry("530x300")
vent.title("SOLES IP")
# centrar(vent)
JustAbajo(vent)

ip1 = StringVar()
ip = StringVar()
ipx0 = StringVar()
ipx1 = StringVar()
conexion = "Conexión de área local"
# vent2=Toplevel(vent)

titulo = Label(vent, text="SOLES V2", font="arial 14")
titulo.place(x=200, y=10)
# line1=C.create_line(0,12,300,12,fill="black")

# ******************CAMBIO DE NOMBRE CONEXIÓN AREA LOCAL******************
bot1 = Button(vent, text="{}", command=CambiarNombreInterface, width=1, height=1)
bot1.place(x=500, y=10)
# **************PING********************
bot1 = Button(vent, text="Ping Manual: ", command=ping1, width=15, height=1)
bot1.place(x=10, y=150)
ent1 = Entry(vent, textvariable=ip, width=15)
ent1.place(x=20, y=175)
ent1.insert(0, "192.168.0.1")
# **************PING GOOGLE********************
bot8 = Button(vent, text="Ping GOOGLE", command=google, width=15, height=2)
bot8.place(x=10, y=100)
# **************VER Interfaces********************
bot2 = Button(vent, text="Ver Interfaces", command=VerInterfaces, width=15, height=2)
bot2.place(x=10, y=50)

# **************PING ONLINE********************
bot9 = Button(vent, text="Ping Online", command=ping_extendido, width=15, height=2)
bot9.place(x=10, y=200)
ping_flag=IntVar()
check_ping = Checkbutton(vent, text="Active", variable=ping_flag)
check_ping.place(x=400, y=200)

# **************PING ONLINE********************
bot10 = Button(vent, text="Find Text", command=lambda: extract_text("open.txt",1,4), width=15, height=2)
bot10.place(x=10, y=250)

# **************VER IP********************
bot2 = Button(vent, text="Ver IP", command=verip, width=15, height=2, background="powder blue")
bot2.place(x=270, y=150)
# **************DHCP********************
bot3 = Button(vent, text="DHCP", command=dhcp, width=15, height=2, background="palegreen")
bot3.place(x=270, y=50)
# **************IP 1********************
bot4 = Button(vent, text="192.168.0.5", command=ip_1, width=15, height=2)
bot4.place(x=140, y=150)
# **************IP 2********************
bot5 = Button(vent, text="192.168.1.5", command=ip_2, width=15, height=2)
bot5.place(x=140, y=100)
# **************IP3********************
bot6 = Button(vent, text="192.168.1.184", command=ip_3, width=15, height=2, background="sky blue")
bot6.place(x=140, y=50)
# **************IP X********************
bot7 = Button(vent, text="IP Manual: ", command=ip_x, width=15, height=1)
bot7.place(x=270, y=100)

ent2 = Entry(vent, textvariable=ipx0, width=15)
ent2.insert(0, "192.168.100.1")
ent2.place(x=280, y=125)

# **************DESACTIVAR RED********************
bot9 = Button(vent, text="Desactivar Red", command=deactred, width=15, height=2, background="pink")
bot9.place(x=400, y=100)
# **************ACTIVAR RED********************
bot10 = Button(vent, text="Activar Red", command=actred, width=15, height=2, background="green")
bot10.place(x=400, y=150)

# **************ARP -A********************
bot9 = Button(vent, text="LOOP (ARP-A)", command=arp, width=15, height=2)
bot9.place(x=400, y=50)

salir = Button(vent, text="Salir", command=vent.destroy, width=15, height=1, font="arial 14", bg="gray")
salir.place(x=550, y=150)

vent.mainloop()
