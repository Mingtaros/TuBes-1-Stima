'''
Tugas Besar 1 [IF2211] Strategi Algoritma
Nama File : backend.py
Deskripsi : Engine back-end untuk memproses bilangan input (array of integer) menjadi output (string)
Nama Kelompok    : Hmm...
Anggota Kelompok :
    Ariel Ansa Razumardi    13517040
    Leonardo                13517048
    Vincent Chuardi         13517103
'''
def Greedy24Solver(B): #Menghasilkan solusi permainan 24 dari 4 buah angka di list B dengan strategi greedy
    BTaken = [False, False, False, False] # Tanda bilangan sudah diambil atau belum
    NextCandidate = 0 # set kandidat yang dipilih menjadi bilangan pertama
    # Bilangan pertama yang dipilih adalah yang paling besar (makin besar makin dekat ke 24)
    for i in range (1,4): 
        if B[i] > B[NextCandidate]:
            NextCandidate = i
    BTaken[NextCandidate] = True # Memberi tanda bilangan sudah dipilih agar tidak dipilih lagi
    SolutionString = str(B[NextCandidate]) # Solusi akan disimpan sebegai sebuah string
    SolutionValue = B[NextCandidate] # Hasil dari persamaan solusi juga disimpan
    PreviousOperator = '' # Operator yang sebelumnya dipakai disimpan untuk menentukan memakai tanda kurung atau tidak
    while not (BTaken[0] and BTaken[1] and BTaken[2] and BTaken[3]):
        # Set value dan point awal untuk mencari pilihan selanjutnya
        #-9999 sudah dipastikan lebih kecil dari semua kemungkinan lain sehingga pasti tergantikan
        NextValue = -9999
        NextPoint = -9999
        for i in range(4):
            if not BTaken[i]: #Jika True maka bilangan sudah terpilih sebelumnya dan tidak bisa dipilih lagi

                # Penjumlahan 
                CandidateValue = SolutionValue + B[i] #Menghitung hasil operasi value sebelumnya dengan bilangan
                if abs(24-CandidateValue) <= abs(24-NextValue): # Jika kandidat lebih atau sama dekat ke 24, maka akan dilanjutkan proses 
                    CandidatePoint = 5 #Poin dari operator, digunakan sebagai tiebreaker
                    if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)): 
                    # Jika kandidat lebih dekat le 24 atau sama dekat tapi poin operator nya lebih besar,
                    # Kandidat akan disimpan sebagai bilangan dan operator yang dipilih selanjutnya (juga hasil,string, dan poin operator nya)
                    # sampai ketemu kandidat yang lebih baik 
                        NextPrevOperator = PreviousOperator + '+'
                        NextValue = CandidateValue
                        NextPoint = CandidatePoint
                        NextString = SolutionString + ' + ' + str(B[i])
                        NextCandidate = i
                #Proses diatas akan dilakukan untuk setiap operator

                # Pengurangan ver 1 (Prev - New)
                CandidateValue = SolutionValue - B[i]
                if abs(24-CandidateValue) <= abs(24-NextValue):
                    CandidatePoint = 4
                    if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                        NextPrevOperator = PreviousOperator + '-'
                        NextValue = CandidateValue
                        NextPoint = CandidatePoint
                        NextString = SolutionString + ' - ' + str(B[i])
                        NextCandidate = i

                # Pengurangan ver 2 (New - Prev)
                CandidateValue = B[i] - SolutionValue
                if abs(24-CandidateValue) <= abs(24-NextValue):
                    if not ((PreviousOperator == '') or (PreviousOperator == '*') or (PreviousOperator == '/') or (PreviousOperator == '**') or (PreviousOperator == '//') or (PreviousOperator == '*/') or (PreviousOperator == '/*')):
                    # Solusi sebelumnya perlu diberi kurung untuk menjaga urutan operasi
                        CandidatePoint = 3    
                        if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                            NextPrevOperator = '-'
                            NextValue = CandidateValue
                            NextPoint = CandidatePoint
                            NextString = str(B[i]) + ' - (' + SolutionString + ')'
                            NextCandidate = i  
                    else:
                    #Solusi sebelumnya tidak perlu diberi tanda kurung
                        CandidatePoint = 4    
                        if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                            NextPrevOperator = '-' + PreviousOperator
                            NextValue = CandidateValue
                            NextPoint = CandidatePoint
                            NextString = str(B[i]) + ' - ' + SolutionString
                            NextCandidate = i

                # Perkalian
                CandidateValue = SolutionValue * B[i]
                if abs(24-CandidateValue) <= abs(24-NextValue):
                    if not ((PreviousOperator == '') or (PreviousOperator == '*') or (PreviousOperator == '/') or (PreviousOperator == '**') or (PreviousOperator == '//') or (PreviousOperator == '*/') or (PreviousOperator == '/*')):
                    # Solusi sebelumnya perlu diberi kurung untuk menjaga urutan operasi    
                        CandidatePoint = 2    
                        if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                            NextPrevOperator = '*'
                            NextValue = CandidateValue
                            NextPoint = CandidatePoint
                            NextString = '(' + SolutionString + ') * ' + str(B[i])
                            NextCandidate = i  
                    else:
                    #Solusi sebelumnya tidak perlu diberi tanda kurung
                        CandidatePoint = 3    
                        if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                            NextPrevOperator = PreviousOperator + '*'
                            NextValue = CandidateValue
                            NextPoint = CandidatePoint
                            NextString = SolutionString + ' * ' + str(B[i])
                            NextCandidate = i    
    
                # Pembagian ver 1 (Prev/New)
                CandidateValue = SolutionValue / B[i]
                if abs(24-CandidateValue) <= abs(24-NextValue):
                    if not ((PreviousOperator == '') or (PreviousOperator == '*') or (PreviousOperator == '/') or (PreviousOperator == '**') or (PreviousOperator == '//') or (PreviousOperator == '*/') or (PreviousOperator == '/*')):
                    # Solusi sebelumnya perlu diberi kurung untuk menjaga urutan operasi
                        CandidatePoint = 1    
                        if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                            NextPrevOperator = '/'
                            NextValue = CandidateValue
                            NextPoint = CandidatePoint
                            NextString = '(' + SolutionString + ') / ' + str(B[i])
                            NextCandidate = i  
                    else:
                    #Solusi sebelumnya tidak perlu diberi tanda kurung
                        CandidatePoint = 2    
                        if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                            NextPrevOperator = PreviousOperator + '/'
                            NextValue = CandidateValue
                            NextPoint = CandidatePoint
                            NextString = SolutionString + ' / ' + str(B[i])
                            NextCandidate = i 

                # Pembagian ver 2 (New/Prev)
                CandidateValue = B[i] / SolutionValue
                if abs(24-CandidateValue) <= abs(24-NextValue):
                    if PreviousOperator != '':
                    # Solusi sebelumnya perlu diberi kurung untuk menjaga urutan operasi
                        CandidatePoint = 1    
                        if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                            NextPrevOperator = '/'
                            NextValue = CandidateValue
                            NextPoint = CandidatePoint
                            NextString = str(B[i]) + ' / (' + SolutionString + ')'
                            NextCandidate = i  
                    else:
                    #Solusi sebelumnya tidak perlu diberi tanda kurung
                        CandidatePoint = 2    
                        if not((abs(24-CandidateValue) == abs(24-NextValue)) and (CandidatePoint <= NextPoint)):
                            NextPrevOperator = '/' + PreviousOperator
                            NextValue = CandidateValue
                            NextPoint = CandidatePoint
                            NextString = str(B[i]) + ' / ' + SolutionString
                            NextCandidate = i

        #Setelah terpilih bilangan dan operator selanjutnya, akan dimasukkan ke dalam solusi (dalam bentuk string, value, dan operator sebelumnya)
        #BTaken nya juga akan di set true agar tidak dapat dipilih lagi
        BTaken[NextCandidate] = True
        SolutionString = NextString
        SolutionValue = NextValue
        PreviousOperator = NextPrevOperator
    return SolutionString + ' = ' + str(SolutionValue) #+ '\n' + "Operator Point : " + str(PoinOperator(SolutionString))

def PoinOperator(Str): #Menghasilkan poin operator dari sebuah string persamaan
    Poin = 0
    for char in Str:
        if char == '+':
            Poin = Poin + 5
        elif char == '-':
            Poin = Poin + 4
        elif char == '*':
            Poin = Poin + 3
        elif char == '/':
            Poin = Poin + 2
        elif char == '(':
            Poin = Poin - 1
    return Poin

if __name__ == '__main__':
    B = [0,0,0,0]
    B[0] = int(input('B1 : '))
    B[1] = int(input('B2 : '))
    B[2] = int(input('B3 : '))
    B[3] = int(input('B4 : '))

    print(Greedy24Solver(B))
