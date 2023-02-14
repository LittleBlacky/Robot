"""数据集整理"""

import os, shutil


def remove(file_path: str) -> None:
    """批量删除指定路径下所有非 `.wav` 文件"""
    for root, dirs, files in os.walk(file_path):
        for item in files:
            if not item.endswith('.wav'):
                try:
                    print("Delete file: ", os.path.join(root, item))
                    os.remove(os.path.join(root, item))
                except:
                    continue


def rename(file_path: str) -> None:
    """批量按指定格式改名（不然把相同情感的音频整理到同一个文件夹时会重名）"""
    for root, dirs, files in os.walk(file_path):
        for item in files:
            if item.endswith('.wav'):
                people_name = root.split('\\')[-2]
                emotion_name = root.split('\\')[-1]
                item_name = item[:-4]  # 音频原名（去掉.wav）
                old_path = os.path.join(root, item)
                new_path = os.path.join(root, item_name + '-' + emotion_name + '-' + people_name + '.wav')  # 新音频路径
                try:
                    os.rename(old_path, new_path)
                    print('converting ', old_path, ' to ', new_path)
                except:
                    continue

def mkdirs(folder_path: str) -> None:
    """检查文件夹是否存在，如果不存在就创建一个"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move(rootpath, file_path: str) -> None:
    """把音频按情感分类，放在不同文件夹下"""
    for root, dirs, files in os.walk(file_path):
        for item in files:
            if item.endswith('.wav'):
                emotion_name = root.split('\\')[-1]
                old_path = os.path.join(root, item)
                dir = os.path.join(rootpath, emotion_name)
                mkdirs(dir)
                new_path = os.path.join(rootpath, emotion_name, item)
                try:
                    shutil.move(old_path, new_path)
                    print("Move ", old_path, " to ", new_path)
                except:
                    continue

def deal_CASIA(filepath):
    """删除非wav文件"""
    remove(filepath)

    """重新命名wav文件，为了后续分类方便"""
    people = [
        'liuchanhg',
        'wangzhe',
        'zhaoquanyin',
        'ZhaoZuoxiang'
    ]
    for name in people:
        rename(filepath+'\\'+name)

    """基于情感分类wav文件"""
    for name in people:
        filname = filepath+'\\'+name
        move(filepath, filname)

    for name in people:
        os.rmdir(os.path.join(filepath, name))

def deal_RAVDESS(filepath):
    dict = {
            '01': 'neutral',
            '02': 'neutral',
            '03': 'happy',
            '04': 'sad',
            '05': 'angry',
            '06': 'fear',
            '08': 'surprise'
            }
    rootpath = 'G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets'
    '''移动'''
    for root, dirs, files in os.walk(filepath):
        for item in files:
            if item.endswith('.wav'):
                if item.split('-')[2] != '07':
                    emotion_name = dict[item.split('-')[2]]
                    old_path = os.path.join(root, item)
                    new_path = os.path.join(rootpath, emotion_name, item)
                    try:
                        shutil.move(old_path, new_path)
                        print("Move ", old_path, " to ", new_path)
                    except:
                        continue

def deal_EMODB(filepath):
    dict = {
                'N': 'neutral',
                'F': 'happy',
                'T': 'sad',
                'W': 'angry',
                'A': 'fear',
            }
    rootpath = 'G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets'
    '''移动'''
    for root, dirs, files in os.walk(filepath):
        for item in files:
            if item.endswith('.wav'):
                if item[5] != 'E' and item[5] != 'L':
                    emotion_name = dict[item[5]]
                    old_path = os.path.join(root, item)
                    new_path = os.path.join(rootpath, emotion_name, item)
                    try:
                        shutil.move(old_path, new_path)
                        print("Move ", old_path, " to ", new_path)
                    except:
                        continue

def deal_SAVEE(filepath):
    dict = {
                'n': 'neutral',
                'h': 'happy',
                'z': 'sad',
                'a': 'angry',
                'f': 'fear',
                'v': 'surprise'
            }
    rootpath = 'G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets'
    '''移动'''
    for root, dirs, files in os.walk(filepath):
        for item in files:
            if item.endswith('.wav'):
                if item[0] != 'd':
                    people_name = root.split('\\')[-1]
                    emotion_name = item[0]
                    if emotion_name == 's':
                        if item[1] == 'a':
                            emotion_name = 'z'
                        else:
                            emotion_name = 'v'
                    emotion_name = dict[emotion_name]
                    old_path = os.path.join(root, item)
                    new_path = os.path.join(rootpath, emotion_name, people_name+item)
                    try:
                        shutil.move(old_path, new_path)
                        print("Move ", old_path, " to ", new_path)
                    except:
                        continue

deal_SAVEE('G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets\\SAVEE')
deal_EMODB('G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets\\EMO-DB')
deal_RAVDESS('G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets\\RAVDESS')
#deal_CASIA('G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets\\CASIA')
#move('G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets\\CASIA', 'G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets\\CASIA\\liuchanhg')
