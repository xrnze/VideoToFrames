# Program untuk membaca sebuah video kemudian mengekstrak setiap framenya menjadi format foto
  
import cv2; 
  
# Fungsi yang digunakan untuk membaca video dan mengekstrak frame menjadi foto
def FrameCapture(path): 
  
    # Memanggil fungsi dari opencv untuk mengambil video dari sebuah file
    # Mengembalikan sebuah class
    vidObj = cv2.VideoCapture(path) 
  
    # Variabel untuk menyimpan jumlah frame yang sudah digenerate
    count = 1
  
    # Untuk mengambil banyaknya jumlah frame dari variabel vidObj
    success = True
    frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))

    while success: 
  
        # Memanggil fungsi untuk mengekstrak frame
        success, image = vidObj.read() 
  
        # Menyimpan frame yang diekstrak kedalam folder
        # Ganti ?Folder dengan alamat folder tujuan
        cv2.imwrite("?folder/frame%d.jpg" % count, image) 
        print("frame " + str(count) + " generated")
        print(success)
        
        # Hentikan perulangan jika semua frame telah diekstrak
        if count == frames:
            print("Total frames generated "+str(count))
            success = False
        
        # Naikan jumlah frame yang telah diekstrak menjadi gambar apabila berhasil
        count += 1
    
    
# Main code 
if __name__ == '__main__': 
    
    # Ganti ?file dengan alamat file video
    FrameCapture("?file")