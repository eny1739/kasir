print("Kasir Kelompok 10 Tugas 4")
print('''====DAFTAR MENU====
Makanan :
1.Ayam Geprek    : 16.200
2.Ayam Krispi    : 13.500
3.Ayam Kecap     : 13.800
4.Ayam Rica-rica : 18.200
Minuman :
1.es teh /hangat   : 3.500
2.es jeruk /hangat : 4.000
3.Susu Panas/Dingin : 5.000
print("=========================")
menu1=int(input("masukkan jenis menu :"))
barang1=int(input("masukan nomor barang :"))
jumlah1=int(input("masukan jumlah barang :"))
if menu1==1 :
    if barang1==1 :
      harga1=16200
    else if barang1==2 :
      harga1=13500
    else if barang1==3 :
      harga1=13800
    else if barang1==4 :
      harga1=18200
else if menu1==2 :
    if barang1==1 :
      harga1=3500
    else if barang1==2 :
      harga1=4000
    else if barang1==3 :
      harga1=5000
total1=harga1*jumlah1
p1=int(input("pilih 1 jika ada pesanan lain :"))
if p1==1 :
    menu=int(input("masukkan jenis menu :"))
barang2=int(input("masukan nomor barang :"))
jumlah2=int(input("masukan jumlah barang :"))
if menu2==1 :
    if barang2==1 :
      harga2=16200
    else if barang2==2 :
      harga2=13500
    else if barang2==3 :
      harga2=13800
    else if barang2==4 :
      harga2=18200
else if menu2==2 :
    if barang2==1 :
      harga2=3500
    else if barang2==2 :
      harga2=4000
    else if barang2==3 :
      harga2=5000
total2=harga2*jumlah2
    p2=int(input("pilih 1 jika ada pesanan lain :"))
    if p2== 1:
        menu3=int(input("masukkan jenis menu :"))
barang3=int(input("masukan nomor barang :"))
jumlah3=int(input("masukan jumlah barang :"))
if menu3==1 :
    if barang3==1 :
      harga1=16200
    else if barang3==2 :
      harga1=13500
    else if barang3==3 :
      harga1=13800
    else if barang3==4 :
      harga1=18200
else if menu3==2 :
    if barang3==1 :
      harga1=3500
    else if barang3==2 :
      harga1=4000
    else if barang3==3 :
      harga1=5000
total3=harga3*jumlah3
        else :
            total=total1+total2+total3
            print(f"total harga yang dibayar : {total}")
    else :
        total=total1+total2
        print(f"total harga yang dibayar : {total}")
        
else :
    total=total1
    print(f"Total yang harus dibayar :{total}")   

uang1  = int(100000)
uang2  = int(50000)
uang3  = int(20000)
uang4  = int(10000)
uang5  = int(5000)
uang6  = int(2000)
uang7  = int(1000)
uang8  = int(500)
uang9  = int(200)
uang10 = int(100)

uang_dibayarkan=int(input("masukan jumlah uang yang dibayarkan :"))
kembalian=uang_dibayarkan-total

pecahan1 = kembalian//uang1
pecahan2 = kembalian%uang1//uang2
pecahan3 = kembalian%uang1%uang2//uang3
pecahan4 = kembalian%uang1%uang2%uang3//uang4
pecahan5 = kembalian%uang1%uang2%uang3%uang4//uang5
pecahan6 = kembalian%uang1%uang2%uang3%uang4%uang5//uang6
pecahan7 = kembalian%uang1%uang2%uang3%uang4%uang5%uang6//uang7
pecahan8 = kembalian%uang1%uang2%uang3%uang4%uang5%uang6%uang7//uang8
pecahan9 = kembalian%uang1%uang2%uang3%uang4%uang5%uang6%uang7%uang8//uang9
pecahan10 = kembalian%uang1%uang2%uang3%uang4%uang5%uang6%uang7%uang8%uang9//uang10

voucher = 1000000

if total <= voucher :
    if pecahan1 > 0 :
        print ("lembar 100000 sebanyak :"+ str(pecahan1))
    if pecahan2 > 0 :
        print ("lembar 50000  sebanyak :"+ str(pecahan2))
    if pecahan3 > 0 :
        print ("lembar 20000  sebanyak :"+ str(pecahan3))
    if pecahan4 > 0 :
        print ("lembar 10000  sebanyak :"+ str(pecahan4))
    if pecahan5 > 0 :
        print ("lembar 5000   sebanyak :"+ str(pecahan5))
    if pecahan6 > 0 :
        print ("lembar 2000   sebanyak :"+ str(pecahan6))
    if pecahan7 > 0 :
        print ("lembar 1000   sebanyak :"+ str(pecahan7))
    if pecahan8 > 0 : 
        print ("lembar 500    sebanyak :"+ str(pecahan8))
    if pecahan9 > 0 :
        print ("lembar 200    sebanyak :"+ str(pecahan9))
    if pecahan10 > 0 :
        print ("lembar 100    sebanyak :"+ str(pecahan10))
else:
    print ("pembelian tidak dapat dilanjutkan")
    
print(f"jumlah kembalian adalah :{kembalian}")
print("TERIMAKASIH SUDAH BERBELANJA")

#KELOMPOK 10
#1.edwin wahyu triyantoro
# nim : 230535604337
#2.christian hamonangan lumbanggaol
# nim : 230535608110
