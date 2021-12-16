#biến python
# nhiều giá trị đến nhiều biến 
print("nhiều giá trị đến nhiều biến")
x1, y1, z1 = 'chao', 'cac', 'ban'
print(x1)
print(y1)
print(z1)

# một giá trị thành nhiều biến
print("\nmột giá trị thành nhiều biến")
x2 = y2 = z2 = 'chao cac ban'
print(x2)
print(y2)
print(z2)

#có một dánh sách và trích xuất nó
print("\ncó một dánh sách và trích xuất nó")
tapbien = ["chao", "cac", "ban"]
x3, y3, z3 = tapbien
print(x3)
print(y3)
print(z3)

#biến đầu rai
print("\nbiến đầu ra")
name = "Dang Ho Huu Phuc"
name1 = "dang"
name2 = "phuc"
name3 = name1 + name2
print("chao " + name)
print("chao " + name1 + name2)
print("chao " + name3 )

#biến toàn cục
print("\nbiến toàn cục")
bientoancuc = "bien toan cuc"
def hambientoancuc():
    print("Day la " + bientoancuc)
hambientoancuc()

#biến toàn cục sử dụng bên trong hàm
print("\nbiến toàn cục sử dụng bên trong hàm")
bien = "ben ngoai"
def hambientoancuc():
    bien = "ben trong"
    print("Day la " + bien)
hambientoancuc()
print(bien)

#global từ khóa toàn cầu
print("\nglobal từ khóa toàn cầu")
def hamglobal():
    global _global
    _global = "global toan cau"
hamglobal()
print("day la " + _global)    

#global bên trong cùng tên với biến bên ngoài
print("\nglobal bên trong cùng tên với biến bên ngoài")
_global1 = "bien ben ngoai"
def hamglobal1():
    global _global1
    _global1 = "bien ben trong"
hamglobal1()
print("day la " + _global1)


#Dạng văn bản:	str
#Loại số:	int, float, complex
#Các loại trình tự:	list, tuple, range
#Loại ánh xạ:	dict
#Đặt các loại:	set, frozenset
#Loại Boolean:	bool
#Loại nhị phân:	bytes, bytearray, memoryview

#lấy loại dữ liệu 
print("\nlấy loại dữ liệu")
layloaidulieu = 5                                                      
print(type(layloaidulieu))

#Số python 
print("\nso python")
soint = 1
sofloat = 2.8
socomplex = 2j

print(type(soint))
print(type(sofloat))
print(type(socomplex))

#chuyen doi loai so
print("\n chuyen doi loai so")
soint_float = float(soint)
sofloat_int = int(sofloat)
soint_complex = complex(soint)
print(soint_float)
print(sofloat_int)
print(soint_complex)

print(type(soint_float))
print(type(sofloat_int))
print(type(soint_complex))

#so ngau nhien random
import random
print(random.randrange(1, 10))
print("\n")

#chi dinh gia tri cua 1 bien
chidinhx = int(2.5)
print(chidinhx)
chidinhy = float(2)
print(chidinhy)
chidinhz = complex(1)
print(chidinhz)
chidinha = str("chao1")
print(chidinha)

#String
#gan chuoi cho 1 bien
stringa = "day la chuoi a"
print("\n " + stringa)

#chuoi nhieu dong 
stringnhieudong = """chao,
cac,
ban."""
print(stringnhieudong)

#chuoi mang
stringmang = "hello, phuc"
print("\n" + stringmang[1])

#vong qua 1 chuoi 
stringvonglap = " string vong lap"
for i in stringvonglap:
    print(i)
print("\n")

#String length (len())
stringlength = "string length"
print(len(stringlength))
print("\n")

#Check String
check_string = "day la chuoi can phai kiem tra"
print("phuc" in check_string)
print("chuoioi" in check_string)
if "chuoi" in check_string:
    print("chuoi in check_string")
else:
    print("khong co")
print("\n")

#Slicing (chonj vi tri cua tu se xuat hien)
string_slicing = "chuoi can chon vi tri xuat hien cua chu"
print(string_slicing[2:9])
print(string_slicing[:9])
print(string_slicing[2:])
print(string_slicing[-2:-9])

#Upper Case
string_uppercase = "string upper case"
print(string_uppercase.upper())
#lower case
string_lowercase = "String Lower Case"
print(string_lowercase.lower())
#strip
string_remove_whitespace = " xoa khoang trang "
print(string_remove_whitespace.strip())
#Replace String
string_replace = "thay the chuoi"
print(string_replace.replace("the", "vao"))
#Split string
string_split = "split string"
print(string_split.split(" "))
#String concatenation 
string_concatenation_1 = "noi chuoi"
string_concatenation_2 = "lai voi nhau"
string_concatenation_3 = string_concatenation_1 + string_concatenation_2
string_concatenation_4 = string_concatenation_1 + " " + string_concatenation_2
print(string_concatenation_3)
print(string_concatenation_4)
