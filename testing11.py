import sys,time


def typingPrint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

nama = input("nama : ")
a = "Nama kamu adalah "
gabung = a + nama
typingPrint(gabung)
