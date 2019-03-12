import os
asim = input('''Здравствуйте! что вы
хотите?
[1] - Установка python
[2] - Установка python2
[3] - Установка nmap
[4] - Установка гит
[5] - Установка wget
[6] - Установка метасплоит
[7] - Выход
''')
if asim == '1':
       os.system("pkg install python")
elif asim == '2':
         os.system("pkg install python2")
elif asim == '3':
         os.system("pkg install nmap")
elif asim == '4':
         os.system("pkg install git")
elif asim == '5':
         os.system("pkg install wget")
elif asim == '6':
         os.system("pkg install unstable-repo")
         os.system("pkg install metasploit")
elif asim == '7':
         exit("Желаю удачи!")
else:
    print ("Я с таким ещё не знаком(")

