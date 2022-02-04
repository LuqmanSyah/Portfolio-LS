import os 
import math

os.system("cls")

def kalkulator():
    while True:
        print("---------------")
        print("Kalkulator")
        print("Pilihan:")
        print(" 1. Tambah")
        print(" 2. Kurang")
        print(" 3. Kali")
        print(" 4. Bagi")
        print(" 5. Pangkat")
        print(" 6. Akar")
        print(" 7. Pembulatan")
        print(" 8. Campuran")
        print("---------------")

        print(" ")
        
        a = int(input("Masukan pilihan: "))

        print(" ")

        if a == 1:
            b = int(input("Masukan angka 1: "))
            c = int(input("Masukan angka 2: "))
            print(" ")
            print(b, "+", c, "=", b + c)
        if a == 2:
            b = int(input("Masukan angka 1: "))
            c = int(input("Masukan angka 2: "))
            print(" ")
            print(b, "-", c, "=", b - c)
        if a == 3:
            b = int(input("Masukan angka 1: "))
            c = int(input("Masukan angka 2: "))
            print(" ")
            print(b, "*", c, "=", b * c)
        if a == 4:
            b = int(input("Masukan angka 1: "))
            c = int(input("Masukan angka 2: "))
            print(" ")
            print(b, "/", c, "=", b / c)
        if a == 5:
            b = int(input("Masukan angka 1: "))
            c = int(input("Masukan angka 2: "))
            print(" ")
            print(b, "**", c, "=", pow(b, c))
        if a == 6:
            b = int(input("Masukan angka: "))           
            x = math.sqrt(b)
            print("√", b, "=", x)
        if a == 7:
            b = float(input("Masukan angka: "))
            e = input("Ke Atas/Bawah: ")
            if e.upper() == "A":
                x = math.ceil(b)
                print("Hasil Pembulatan", x)
            if e.upper() == "B":
                x = math.floor(b)
                print("Hasil Pembulatan", x)
        if a == 8:
            print("Pilihan campuran:")
            
            print(" ")

            print("---------------")
            print("1. __+__+__= ")
            print("2. __+__-__= ")
            print("3. __+__*__= ")
            print("4. __+__/__= ")
            print("5. __-__-__= ")
            print("6. __-__+__= ")
            print("7. __-__*__= ")
            print("8. __-__/__= ")
            print("9. __*__*__= ")
            print("10. __*__/__= ")
            print("11. __*__+__= ")
            print("12. __*__-__= ")
            print("13. __/__/__= ")
            print("14. __/__*__= ")
            print("15. __/__+__= ")
            print("16. __/__-__= ")
            print("17. __**__*__= ")
            print("18. __**__/__= ")
            print("19. __**__+__= ")
            print("20. __**__-__= ")
            print("21. √__*__= ")
            print("22. √__/__= ")
            print("23. √__+__= ")
            print("24. √__-__= ")

            print("---------------")

            print(" ")

            h = int(input("Masukan pilihan: "))

            print(" ")

            if h == 1:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "+", kt, "+", sd, "=", tk + kt + sd)
            if h == 2:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "+", kt, "-", sd, "=", tk + kt - sd)
            if h == 3:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "+", kt, "*", sd, "=", tk + kt * sd)
            if h == 4:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "+", kt, "/", sd, "=", tk + kt / sd)
            if h == 5:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "-", kt, "-", sd, "=", tk - kt - sd)
            if h == 6:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "-", kt, "+", sd, "=", tk - kt + sd)
            if h == 7:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "-", kt, "*", sd, "=", tk - kt * sd)
            if h == 8:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "-", kt, "/", sd, "=", tk - kt / sd)
            if h == 9:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "*", kt, "*", sd, "=", tk * kt * sd)
            if h == 10:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "*", kt, "/", sd, "=", tk * kt / sd)
            if h == 11:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "*", kt, "+", sd, "=", tk * kt + sd)
            if h == 12:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "*", kt, "-", sd, "=", tk * kt - sd)
            if h == 13:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "/", kt, "/", sd, "=", tk / kt / sd)
            if h == 14:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "/", kt, "*", sd, "=", tk / kt * sd)
            if h == 15:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "/", kt, "+", sd, "=", tk / kt + sd)
            if h == 16:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "/", kt, "-", sd, "=", tk / kt - sd) 
            if h == 17:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "**", kt, "*", sd, "=", pow(tk, kt) * sd)
            if h == 18:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "**", kt, "/", sd, "=", pow(tk, kt) / sd)
            if h == 19:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "**", kt, "+", sd, "=", pow(tk, kt) + sd)
            if h == 20:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                sd = int(input("Masukan angka 3: "))
                print(tk, "**", kt, "-", sd, "=", pow(tk, kt) - sd)
            if h == 21:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                x = math.sqrt(tk)
                print("√", tk, "*", kt, "=", x * kt)
            if h == 22:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                x = math.sqrt(tk)
                print("√", tk, "/", kt, "=", x / kt)
            if h == 23:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                x = math.sqrt(tk)
                print("√", tk, "+", kt, "=", x + kt)
            if h == 24:
                tk = int(input("Masukan angka 1: "))
                kt = int(input("Masukan angka 2: "))
                x = math.sqrt(tk)
                print("√", tk, "-", kt, "=", x - kt)
            if h >= 25:
                exit()
        
        if a >= 9:
            exit()

        print(" ")

        d = input("Out [Y/N]: ")
        if d.upper() == "Y":
            exit()

        os.system("cls")

kalkulator()