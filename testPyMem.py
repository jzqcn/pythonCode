import pymem
import struct

process_name = "helloWorld.exe"
int_to_find = 4396

# 创建 Pymem 对象
pm = pymem.Pymem(process_name)

# 获取指定模块的基地址和大小
module_name = "CoreUIComponents.dll"
module_info = [m for m in pm.list_modules() if m.name == module_name][0]
base_address = module_info.lpBaseOfDll
module_size = module_info.SizeOfImage

print(f"{module_name} 的基地址为 0x{base_address:X}")

# 读取整个进程空间内的内存数据
process_all_memory = pm.read_bytes(base_address, module_size)

# 将要搜索的整数值转换为字节序列
int_to_find_bytes = struct.pack("<i", int_to_find)

# 查找字节序列的位置
offset = process_all_memory.find(int_to_find_bytes)

#只读取了一次。

if offset >= 0:
    # 计算变量在内存中的地址
    variable_address = base_address + offset
    print(f"变量值 {int_to_find} 所在内存地址：0x{variable_address:X}")
else:
    print(f"未找到值为 {int_to_find} 的变量")


# for page in pm.list_modules():
#     print(page.filename)
#     print(page.SizeOfImage)
#     print("0x{:X}".format(page.lpBaseOfDll))

# print(pm.read_int(0x0073F910))

#print("0x{:X}".format((0x740000 - 0x0073F910)))


# a_value = 4396
# test_a = 0x0073F910
# for address in range(test_a, 0x0073F920,2):
#     print("yy")
#     try:
#         value = pm.read_int(address)
#         if value == a_value:
#             print("变量 a 的地址是：0x{:X}".format(address))
#     except:
#         # 如果读取地址的值失败，则跳过该地址并继续遍历
#         continue



# 读取内存中指定地址的数据
#data = pm.read_bytes(base_address, 100)

# # 遍历内存
# for i in range(0, 100, 4):
#     # 读取地址为base_address + i的四个字节数据
#     b = pm.read_bytes(base_address + i, 4)
#     # 将读取到的四个字节数据转换为整数类型并打印
#     print(int.from_bytes(b, byteorder='little'))
 
# exe名称
# pm = Pymem('helloWorld.exe')
# print('Process id: %s' % pm.process_id)

# base = 0xCEE514F9E0
# a = pm.read_int(base)
# b = pm.read_int(base + 0x4)
# c = pm.read_int(base + 0x8)

# print(a,b,c)
# print("======new=====")
# pm.write_int(base,5999)
# a = pm.read_int(base)
# b = pm.read_int(base + 0x4)
# c = pm.read_int(base + 0x8)
# print(a,b,c)

# def Get_moduladdr(dll): # 读DLL模块基址
#     modules = list(pm.list_modules()) # 列出exe的全部DLL模块
#     for module in modules:
#         if module.name == dll:
#             print(module.name) # 模块名字
#             print(module.lpBaseOfDll) # 模块基址
#             print("找到了")
#             Moduladdr = module.lpBaseOfDll
#     return Moduladdr

# Char_Modlue = Get_moduladdr("helloWorld.exe") # 读DLL模块基址
# print('%#x'%Char_Modlue)
# #My_x = pm.read_float(My_addr + 0x308)


