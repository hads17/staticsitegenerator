import os
import shutil

def copy_static_files_to_public(filepath):
    if os.path.isdir(filepath):
        shutil.rmtree(filepath)
    os.mkdir(filepath)
    static_path = os.path.join(os.getcwd(), "static")
    static_files = get_files(static_path)
    static_folders = get_folders(static_path)
    #print('files: ', static_files)
    print('folders: ', static_folders)

def get_folders(filepath):
    result = []
    print("current FilePath: ", filepath)
    if get_filecount(filepath) == 0:
        result.append(filepath)
        print("zero count: ", result)
        return result
    subfolders = []
    #List out Directories and Files in provided filepath
    dir_list = os.listdir(filepath)
    print(dir_list)
    if dir_list:
        for dir in dir_list:
            path = os.path.join(filepath, dir)
            if os.path.isdir(path):
                result.append(path)
                subfolders.extend(get_folders(path))
    if subfolders:
        result.extend(subfolders)
    return result

def get_filecount(filepath):
    count = 0
    dir_list = os.listdir(filepath)
    if not dir_list:
        return 0
    for dir in dir_list:
        path = os.path.join(filepath, dir)
        if os.path.isdir(path):
            count += 1
    return count

def get_files(filepath):
    result = []
    file_list = os.listdir(filepath)
    #print(file_list)
    for file in file_list:
        path = os.path.join(filepath, file)
        if os.path.isdir(path):
            result.extend(get_files(path))
        result.extend(path)

    return result
