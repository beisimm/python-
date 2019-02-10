import os


def FileNameOrSuffix(remove_name):

    if remove_name[0] == '.':
        return 1
    else:
        return 0

def FindFiles(path, remove_name):
    lists = []
    for dir_path, dirs_name, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[FileNameOrSuffix(remove_name)] == remove_name:  # 0 下标是文件名包含, 1下标是后缀名包含
                absolute_path = dir_path +"\\" +file
                lists.append(absolute_path)
    print("文件路径获取成功 ", lists)
    return lists


def removeFileInFirstDir(path, remove_name):
    lists = FindFiles(path, remove_name)
    for index in range(len(lists)):
        os.remove(lists[index])
    print('"文件删除成功"')


if __name__ == '__main__':
    # file_dir = input(r'请输入路径: ')
    file_dir = r'F:\LOLTaiWang\32775\Game'
    removeList = ['.txt', '.csv','.log','.json']
    try:
        for i in removeList:
            removeFileInFirstDir(file_dir, i)
    except Exception as e:
        print('执行完成,一些错误',e)