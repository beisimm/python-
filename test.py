import os

print(os.getcwd())
# folder = os.getcwd()[:-4] + 'new_folder\\test\\'
# os.mkdir('umei1')
# folder = os.path.exists('umei1')
# print(folder)
# 获取此py文件路径，在此路径选创建在new_folder文件夹中的test文件夹

# if not os.path.exists(folder):
    # os.makedirs(folder)


def create_folder(file_name):
    if os.path.exists(file_name):
        print("文件夹已存在")
    else:
        os.mkdir(file_name)
        print('文件夹%s创建成功', file_name)

create_folder('umei1')