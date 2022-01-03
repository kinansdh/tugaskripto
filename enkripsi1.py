plain = input("masukkan kalimat : ")
key = 123
chiper = ""

for i in plain:
    chiper += chr(ord(i)^key)
print("Chipertext dari",plain,"yaitu : ", chiper)
chiper