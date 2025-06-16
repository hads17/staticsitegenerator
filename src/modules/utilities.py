import os
import shutil

def copy_static_files_to_public(filepath):
    if os.path.isdir(filepath):
        shutil.rmtree(filepath)
    os.mkdir(filepath)
    static_path = os.path.join(os.getcwd(), "static")
    folders = get_folders(static_path)
    print('folders: ', folders)
    create_folder_structure(folders)
    #print(get_files(static_path))


def create_folder_structure(folders):
    if not folders:
        raise ValueError("No Folders provided")
    for folder in folders:
        os.mkdir(folder)

def create_files(files):
    pass

def get_folders(filepath, root=None):
    if root:
        new_public_path = root
    else:
        new_public_path = os.path.join(os.getcwd(), "public")
    folders = []
    if get_foldercount(filepath) > 0:
        dir_list = os.listdir(filepath)
        for dir in dir_list:
            dir_public_path = os.path.join(new_public_path, dir)
            dir_path = os.path.join(filepath, dir)
            if os.path.isdir(dir_path):
                subfolders = []
                subfolders = get_folders(dir_path, dir_public_path)
                if subfolders:
                    folders.append(dir_public_path)
                    folders.extend(subfolders)
                else:
                    folders.append(dir_public_path)
    return folders

def get_foldercount(filepath):
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
