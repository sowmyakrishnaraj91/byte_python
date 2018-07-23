import os
import time
import subprocess

#Adding source folder as list
source = [r'C:\Users\skrishnaraj\git_personal\byte_python']

#Adding target folder
target_dir = r'C:\Users\skrishnaraj\byte_backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
print(target)

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#Check for zip command error
zip_command = 'C:\Program Files (x86)\GnuWin32\\bin\zip -r {} {}'.format(target,' '.join(source))

print(zip_command)

print('Running')

p = subprocess.Popen(zip_command)

output, errors = p.communicate()
print(output)
#
# if os.system(zip_command) == 0:
#     print('Successful backup to', target)
# else:
#     print('Backup FAILED')