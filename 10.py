# Запуск внешних приложений
# import os
# Заменяем слеши, чтобы не получилось экранирование
# os.system('C:/WINDOWS/system32/notepad.exe')
# Или используем сырую строку
# os.system(r'C:\WINDOWS\system32\notepad.exe')
# os.system(r'C:\"Program Files (x86)"\7-Zip\7zFM.exe')
# os.startfile(r'C:\Program Files (x86)\7-Zip\7zFM.exe')
# Далее не понятная хренотень, надо читать справку в Shell'e
import subprocess
"""import shlex
# Выдаёт справку по интерпритатору команд в Windows
cmd = 'cmd /?'
args = shlex.split(cmd)
p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
result = p.communicate()[0]
print(result.decode('cp866'))
"""
# Определяет время обмена данными с сервером Гугл
cmd = 'ping 8.8.8.8'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
result = p.communicate()[0]
print(result.decode('cp866'))
