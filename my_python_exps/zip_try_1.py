
'''
import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            os.path.relpath(os.‌​path.join(root, file), os.path.join(path, '..'))
            ziph.write(os.path.join(root, file))
            

if __name__ == '__main__':
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('C:\Users\uidj7182\Documents\python_files\zip', zipf)
    zipf.close()
'''

import shutil
dir_name = 'C:\Users\uidj7182\Documents\python_files\zip'
output_filename = 'temp'
shutil.make_archive(output_filename, 'zip', dir_name)
