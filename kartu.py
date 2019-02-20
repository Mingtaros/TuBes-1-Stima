'''
Tugas Besar 1 [IF2211] Strategi Algoritma
Nama File : kartu.py
Deskripsi : Library kartu yang didasari pydealer terkhusus untuk dipanggil di frontend.py
Nama Kelompok    : Hmm...
Anggota Kelompok :
    Ariel Ansa Razumardi    13517040
    Leonardo                13517048
    Vincent Chuardi         13517103
'''

import pydealer
#pemakaian kartu pada tugas besar kami menggunakan library pydealer
deck = pydealer.Deck()

# rank untuk perhitungan
ranks = {
    "King": 13,
    "Queen": 12,
    "Jack": 11,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "Ace": 1
}
# dictionary card_pic merujuk ke gambar yang ada pada folder gambar_kartu
# untuk mengeluarkan gambarnya pada GUI di frontend1.py
card_pic = {
    "default" : "gambar_kartu//gray_back.png",
    "Ace of Spades" : "gambar_kartu//AS.png",
    "2 of Spades" : "gambar_kartu//2S.png",
    "3 of Spades" : "gambar_kartu//3S.png",
    "4 of Spades" : "gambar_kartu//4S.png",
    "5 of Spades" : "gambar_kartu//5S.png",
    "6 of Spades" : "gambar_kartu//6S.png",
    "7 of Spades" : "gambar_kartu//7S.png",
    "8 of Spades" : "gambar_kartu//8S.png",
    "9 of Spades" : "gambar_kartu//9S.png",
    "10 of Spades" : "gambar_kartu//10S.png",
    "Jack of Spades" : "gambar_kartu//JS.png",
    "Queen of Spades" : "gambar_kartu//QS.png",
    "King of Spades" : "gambar_kartu//KS.png",
    "Ace of Hearts" : "gambar_kartu//AH.png",
    "2 of Hearts" : "gambar_kartu//2H.png",
    "3 of Hearts" : "gambar_kartu//3H.png",
    "4 of Hearts" : "gambar_kartu//4H.png",
    "5 of Hearts" : "gambar_kartu//5H.png",
    "6 of Hearts" : "gambar_kartu//6H.png",
    "7 of Hearts" : "gambar_kartu//7H.png",
    "8 of Hearts" : "gambar_kartu//8H.png",
    "9 of Hearts" : "gambar_kartu//9H.png",
    "10 of Hearts" : "gambar_kartu//10H.png",
    "Jack of Hearts" : "gambar_kartu//JH.png",
    "Queen of Hearts" : "gambar_kartu//QH.png",
    "King of Hearts" : "gambar_kartu//KH.png",
    "Ace of Clubs" : "gambar_kartu//AC.png",
    "2 of Clubs" : "gambar_kartu//2C.png",
    "3 of Clubs" : "gambar_kartu//3C.png",
    "4 of Clubs" : "gambar_kartu//4C.png",
    "5 of Clubs" : "gambar_kartu//5C.png",
    "6 of Clubs" : "gambar_kartu//6C.png",
    "7 of Clubs" : "gambar_kartu//7C.png",
    "8 of Clubs" : "gambar_kartu//8C.png",
    "9 of Clubs" : "gambar_kartu//9C.png",
    "10 of Clubs" : "gambar_kartu//10C.png",
    "Jack of Clubs" : "gambar_kartu//JC.png",
    "Queen of Clubs" : "gambar_kartu//QC.png",
    "King of Clubs" : "gambar_kartu//KC.png",
    "Ace of Diamonds" : "gambar_kartu//AD.png",
    "2 of Diamonds" : "gambar_kartu//2D.png",
    "3 of Diamonds" : "gambar_kartu//3D.png",
    "4 of Diamonds" : "gambar_kartu//4D.png",
    "5 of Diamonds" : "gambar_kartu//5D.png",
    "6 of Diamonds" : "gambar_kartu//6D.png",
    "7 of Diamonds" : "gambar_kartu//7D.png",
    "8 of Diamonds" : "gambar_kartu//8D.png",
    "9 of Diamonds" : "gambar_kartu//9D.png",
    "10 of Diamonds" : "gambar_kartu//10D.png",
    "Jack of Diamonds" : "gambar_kartu//JD.png",
    "Queen of Diamonds" : "gambar_kartu//QD.png",
    "King of Diamonds" : "gambar_kartu//KD.png",
}
