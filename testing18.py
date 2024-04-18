import os
import sys

import pyautogui as pt
import time

def typingPrint(text):
    for chat in text:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.05)
def clearScreen():
    os.system("cls")
while True:
    print("==================================================================")
    print("= 1. Text                                                        =")
    print("= 2. Emot                                                        =")
    print("= 3. Exit                                                        =")
    print("==================================================================")
    pilih = int(input("Masukkan pilihan anda 1/2 : "))
    if pilih == 1:
        limit = int(input("Enter Limit : "))
        message = input("Enter Message : ")
        i=0
        time.sleep(5)
        while True:
            i += 1
            # pt.typewrite(message +" "+ str(i),0.1)
            pt.typewrite(message,0.05)
            pt.press("enter")
            print(i)
            if i == limit:
                time.sleep(1)
                typingPrint("Selesai.....\n")
                break
    elif pilih == 2:
        elimit = int(input("Enter Limit : "))
        message = input("Enter Message : ")
        e = 0
        time.sleep(5)
        while True:
            e += 1
            # pt.typewrite(message +" "+ str(i),0.1)
            pt.typewrite(message, 0.15)
            pt.press("enter")
            print(e)
            if e == elimit:
                time.sleep(1)
                typingPrint("Selesai.....\n")
                break
    elif pilih == 3:
        typingPrint("Terima kasih telah menjalankan Program ini\n")
        time.sleep(1)
        typingPrint("Program ini akan di clear dalam 4..")
        time.sleep(1)
        typingPrint(" 3..")
        time.sleep(1)
        typingPrint(" 2..")
        time.sleep(1)
        typingPrint(" 1..")
        time.sleep(1)
        clearScreen()
        break
    else:
        typingPrint("Pilihan Anda tidak ada")
        time.sleep(1)