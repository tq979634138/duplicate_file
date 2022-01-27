import os
import difflib


def operate(file_path):
    name_list = list(os.walk(file_path))[0][2]
    compare_list = []
    for index in range(len(name_list)-1):
        name_1 = name_list[index].split(".")[0]
        ra_list = []
        for compare in range(index + 1, len(name_list)):
            name_2 = name_list[compare].split(".")[0]
            s = difflib.SequenceMatcher(None, name_1, name_2)
            ra = s.ratio()
            ra_list.append(ra)
        if max(ra_list) > 0.74:
            print(f"index:{index}")
            print(f"ra_list:{ra_list}")
            print(f"ma_index:{ra_list.index(max(ra_list))}")
            compare_list.append(name_list[ra_list.index(max(ra_list)) + index + 1])
    return compare_list


def delete_file(f_path):
    if os.path.exists(f_path):
        try:
            os.remove(f_path)
            print(f"已删除文件：{f_path}")
        except OSError:
            print("该路径可能是文件夹，请仔细检查")
    else:
        print("文件路径错误，请检查")


if __name__ == '__main__':
    li = operate(r"D:\测试文件\报表")
    print(li)
