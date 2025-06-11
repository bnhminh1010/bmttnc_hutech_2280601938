def tao_tuple_tu_list(lst):
    return tuple(lst)
# nhập danh sách từ người dùng và xử lí chuỗi 
input_list = input("Nhập danh sách chuỗi, cách nhau bằng dấu phẩy")
numbers = list(map(int, input_list.split(',')))
               
my_tuple = tao_tuple_tu_list(numbers)
print("List", numbers)
print("Tuple từ list", my_tuple)