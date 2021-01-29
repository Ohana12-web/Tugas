import sys
str1 = "Nicholas"
huruf = angka = simbol = 0

for line in sys.stdin:
    str1 = line
    for i in range(len(str1)):
        if((str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z')): 
            huruf = huruf + 1 
        elif(str1[i] >= '0' and str1[i] <= '9'):
            angka = angka + 1
        else:
            simbol = simbol + 1

sys.stdout.write("Banyaknya Angka: " + str(angka))
sys.stdout.write('\n')
sys.stdout.write("Banyaknya Huruf: " + str(huruf))
sys.stdout.write('\n')
sys.stdout.write("Banyaknya Simbol: " + str(simbol))
sys.stdout.write('\n')
