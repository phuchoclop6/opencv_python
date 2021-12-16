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

#




