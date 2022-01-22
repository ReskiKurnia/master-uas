import csv
import os

csv_filename = 'tbl_students_0530.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI SEDERHANA ===")
    print("[1] Tampilkan Semua data")
    print("[2] Tambahkan Data")
    print("[3] Cari Data")
    print("[4] Hapus Data")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu :  ")
    
    if(selected_menu == "1"):
        show_contact()
    elif(selected_menu == "2"):
        edit_contact()
    elif(selected_menu == "3"):
        search_contact()
    elif(selected_menu == "4"):
        delete_contact()
    elif(selected_menu == "0"):
        exit()
    else:
        print(" Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input(" Tekan Enter untuk kembali...")
    show_menu()

#menampilkan data
def show_contact():
    clear_screen()
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    if (len(contacts) > 0):
        labels = contacts.pop(0)
        print('-'*100)
        print(f'{labels[0]} \t {labels[1]} \t\t {labels[2]} \t\t\t {labels[3]} \t {labels[4]} \t\t {labels[5]}')
        print("-"*100)
        for data in contacts:
            print(f'{data[0]} \t {data[1]} \t\t\t\t {data[2]} \t\t {data[3]} \t {data[4]} \t {data[5]}')
        print('-'*100)

    else:
        print("Tidak ada data!")

    back_to_menu()


#-------------------------base--------------------------->
def create_contact(): 
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ["NO", "NIM", "NAMA", 'JK', 'JURUSAN', 'ALAMAT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        no = input("No urut: ")
        nim = input("Nim: ")
        nama = input("Nama lengkap: ")
        jk = input("jenis kelamin : ")
        jurusan = input("jurusan: ")
        alamat = input("alamat: ")

        writer.writerow({'NO': no, 'NIM': nim, 'NAMA': nama, 'JK': jk, 'JURUSAN': jurusan, 'ALAMAT': alamat})    
        print("Berhasil disimpan!")
    
    back_to_menu()

#---------------------------------------------------------->


#--------------------- Belum Fix -------------------------->
#Mencari data
def search_contact():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    no = input(" Cari berdasrakan Nim :  ")

    data_found = [csv_filename]

    # mencari contact
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            data_found = contacts[indeks]
            
        indeks = indeks + 1

    if (len(contacts) > 0):
        labels = contacts.pop(0)
        print("DATA DITEMUKAN: ")
        print('-'*100)
        print(f'{labels[0]}  {labels[1]} \t\t {labels[2]} \t\t\t {labels[3]} \t {labels[4]} \t\t\t {labels[5]}')
        print("-"*100)
        for data in contacts:
            print(f'{data[0]}  {data[1]} \t   {data[2]} {data[3]} \t  {data[4]}  \t\t {data[5]}')
        print('-'*100)

    else:
        print("Tidak ada data!")

    back_to_menu()

#-------------------------------------------------->

#-------------------------- Belum Fix ------------->
# mengedit data
def edit_contact():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

   
        
   

    print("-----------------")
    print(" TAMBAHKAN DATA  ")
    print("-----------------")
    nim = input("masukan nim : ")
    nama = input("masukan nama : ")
    jk = input("jenis kelamin : ")
    jurusan = input("jurusan : ")
    alamat = input("alamat : ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            contacts[indeks]['NIM'] = nim
            contacts[indeks]['NAMA'] = nama
            contacts[indeks]['JK'] = jk
            contacts[indeks]['JURUSAN'] = jurusan
            contacts[indeks]['ALAMAT'] = alamat
        indeks = indeks + 1

    # Menulis data baru ke file CSV 
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NIM', 'NAMA', 'JK', 'JURUSAN', 'ALAMAT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NO': new_data['NO'], 'NIM': new_data['NIM'], 'NAMA': new_data['NAMA'], 'JK': new_data['JK'], 'JURUSAN': new_data['JURUSAN'], 'ALAMAT': new_data['ALAMAT'],}) 

    back_to_menu()

#----------------------------------------------------->


#menghapus data
def delete_contact():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NIM \t\t NAMA \t JK \t JURUSA, \t ALAMAT")
    print("-" * 100)

    for data in contacts:
         print(f'{data[0]}  {data[1]} \t   {data[2]} {data[3]} \t  {data[4]}  \t\t {data[5]}')
    print('-'*100)


    print("-----------------------")
    no = input("Hapus nomer> ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV 
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NIM', 'NAMA', 'JK', 'JURUSAN', 'ALAMAT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NO': new_data['NO'], 'NIM': new_data['NIM'], 'NAMA': new_data['NAMA'], 'JK': new_data['JK'], 'JURUSAN': new_data['JURUSAN'], 'ALAMAT': new_data['ALAMAT'],}) 

    print("Data sudah terhapus")
    back_to_menu()



if __name__ == "__main__":
    while True:
        show_menu()