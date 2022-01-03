chiper = input("Masukkan kalimat : ")
key = 123
plain= ""

for i in chiper:
    plain += chr(ord(i)^key)
print("Plaintext dari chipertextnya",chiper, "adalah : ", plain)
plain
