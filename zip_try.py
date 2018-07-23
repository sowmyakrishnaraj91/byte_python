import os
import zipfile

#Adding source folder as list
source = r'C:\Users\skrishnaraj\git_personal\byte_python'


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

zipf = zipfile.ZipFile(r'C:\Users\skrishnaraj\\byte_backup_zip\python_zip.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir(source, zipf)
zipf.close()

