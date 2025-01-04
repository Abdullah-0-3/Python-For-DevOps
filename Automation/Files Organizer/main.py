# Files Organizer

'''
Folder Structure:
    - Images
    - Videos
    - Documents
    - Others
'''

import os
import shutil

def organize(path, except_files):
    files = os.listdir(path)

    # Create Folders
    folders = ['Images', 'Videos', 'Documents', 'Others']
    for folder in folders:
        if not os.path.exists(os.path.join(path, folder)):
            os.mkdir(os.path.join(path, folder))

    # Organize Files
    for file in files:
        if file in except_files:
            continue

        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.gif'):
            shutil.move(os.path.join(path, file), os.path.join(path, 'Images', file))

        elif file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv') or file.endswith('.flv'):
            shutil.move(os.path.join(path, file), os.path.join(path, 'Videos', file))

        elif file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.pptx'):
            shutil.move(os.path.join(path, file), os.path.join(path, 'Documents', file))

        else:
            shutil.move(os.path.join(path, file), os.path.join(path, 'Others', file))

    print('Files Organized Successfully!')

if __name__ == '__main__':
    path = os.getcwd()
    except_files = ['main.py']

    organize(path, except_files)