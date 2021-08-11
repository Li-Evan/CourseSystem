from conf import settings
import os
import pickle

def save(obj):

    # 如果没有属于该类的文件夹则进行创建
    class_name = obj.__class__.__name__
    class_dir_path = os.path.join(
        settings.DB_PATH,class_name
    )

    if not os.path.exists(class_dir_path):
        os.mkdir(class_dir_path)


    # 以对象名作为文件名进行保存
    file_name = obj.username
    file_path = os.path.join(
        class_dir_path,file_name
    )

    with open(file_path,'wb') as f:
        pickle.dump(obj,f)


def select(cls,username):

    # 如果没有属于该类的文件夹则进行创建
    class_name = cls.__name__
    class_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )

    if not os.path.exists(class_dir_path):
        os.mkdir(class_dir_path)

    # 如果文件存在则读取并返回对象，不存在则默认返回None
    file_name = username
    file_path = os.path.join(
        class_dir_path, file_name
    )
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)

            return obj