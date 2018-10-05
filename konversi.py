import rupiah

vinput = "Y"


def usdtoidr(usd):
    a = usd * 15000
    return rupiah.formatrupiah(a)


def idrtousd(idr):
    a = idr / float(15000)
    return a


print ("PROGRAM KONVERSI MATA UANG")
print ("==========================")
print ("MENU PILIHAN :")
print ("1. KONVERSI DOLLAR KE RUPIAH")
print ("2. KONVERSI RUPIAH KE DOLLAR")
print ("3. KELUAR")
print ("==========================")

while (raw_input("ketik [Y/N] untuk lanjut :") == vinput):
    jawab = int(raw_input("Pilih Menu Konversi :"))
    if (jawab == 1):
        print ("Konversi dollar ke rupiah")
        jml = int(raw_input("Masukan Jumlah Dollar : "))
        print jml, " dollar = ", usdtoidr(jml)
    elif (jawab == 2):
        print ("Konversi rupiah ke dollar")
        jml = int(raw_input("Masukan Jumlah Rupiah :"))
        print rupiah.formatrupiah(jml), " = $", idrtousd(jml)
    elif (jawab == 3):
        vinput == "N"

    else:
        vinput == "N"
print "Terimakasih"


