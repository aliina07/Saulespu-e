print("Sveicināti! Šī programma izveido rēķinus koka lādīšu pasūtījumiem.")

klients = input("Ievadiet klienta vārdu: ")
veltijums = input("Ievadiet veltījuma tekstu: ")

platums = int(input("Ievadiet lādītes platumu (mm): "))
garums = int(input("Ievadiet lādītes garumu (mm): "))
augstums = int(input("Ievadiet lādītes augstumu (mm): "))

materiala_cena = float(input("Ievadiet kokmateriāla cenu (EUR/m2): "))


darba_samaksa = 15
PVN = 21
veltijuma_garums = len(veltijums)

produkta_cena = (veltijuma_garums * 1.2) + ((platums * garums * augstums) / 100 * materiala_cena) / 3
PVN_summa = (produkta_cena + darba_samaksa) * PVN / 100
rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa

print(produkta_cena)
print(rekina_summa)