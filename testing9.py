import sys
import time


def typingprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

# a = input("")

menu = ["Silahkan pilih Menu Makanan\n","1. Nasi Goreng\n","2. Mie Goreng\n",
                "3. Es Jeruk\n","4. Jus Mangga\n","5. Pisang Goreng\n"
                ]
for m in menu:
    typingprint(m)
