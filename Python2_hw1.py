import subprocess

print('\n----------\nЗадание 1\n----------')

s1 = 'разработка'
print('s1 = {}, type s1 = {}, len s1 = {}'.format(s1, type(s1), len(s1)))

s2 = 'сокет'
print('s2 = {}, type s2 = {}, len s2 = {}'.format(s2, type(s2), len(s2)))

s3 = 'декоратор'
print('s3 = {}, type s3 = {}, len s3 = {}'.format(s3, type(s3), len(s3)))

u_s1 = s1.encode('utf-8')
print('\nu_s1 (utf-8) = {}, type u_s1 = {}, len u_s1 = {}'.format(u_s1, type(u_s1), len(u_s1)))

u_s2 = s1.encode('utf-16')
print('u_s2 (utf-16) = {}, type u_s2 = {}, len u_s2 = {}'.format(u_s2, type(u_s2), len(u_s2)))

u_s3 = s1.encode('utf-32')
print('u_s3 (utf-32) = {}, type u_s3 = {}, len u_s3 = {}'.format(u_s3, type(u_s3), len(u_s3)))

print('\n----------\nЗадание 2\n----------')

b1 = b'class'
print('b1 = {}, type b1 = {}, len b1 = {}'.format(b1, type(b1), len(b1)))

b2 = b'function'
print('b2 = {}, type b2 = {}, len b2 = {}'.format(b2, type(b2), len(b2)))

b3 = b'method'
print('b3 = {}, type b3 = {}, len b3 = {}'.format(b3, type(b3), len(b3)))

print('\n----------\nЗадание 3\n----------')

b1 = b'attribute'
print('b1 = {}, type b1 = {}, len b1 = {}'.format(b1, type(b1), len(b1)))

# try:
#     b2 = b'класс'
#     print('b2 = {}, type b2 = {}, len b2 = {}'.format(b2, type(b2), len(b2)))
# except SyntaxError:
#     print('SyntaxError: bytes can only contain ASCII literal characters')

# try:
#     b3 = b'функция'
#     print('b3 = {}, type b3 = {}, len b3 = {}'.format(b3, type(b3), len(b3)))
# except SyntaxError:
#     print('SyntaxError: bytes can only contain ASCII literal characters')

b4 = b'type'
print('b4 = {}, type b4 = {}, len b4 = {}'.format(b4, type(b4), len(b4)))

print('\n----------\nЗадание 4\n----------')

u_s1 = str.encode('разработка', 'utf-8')
s1 = bytes.decode(u_s1, 'utf-8')
print('u_s1 (utf-8) = {}, type u_s1 = {}, len u_s1 = {}\n'
      's1 = {}, type s1 = {}, len s1 = {}'.format(u_s1, type(u_s1), len(u_s1), s1, type(s1), len(s1)))

u_s2 = str.encode('администрирование', 'utf-8')
s2 = bytes.decode(u_s2, 'utf-8')
print('\nu_s2 (utf-8) = {}, type u_s2 = {}, len u_s2 = {}\n'
      's2 = {}, type s2 = {}, len s2 = {}'.format(u_s2, type(u_s2), len(u_s2), s2, type(s2), len(s2)))

u_s3 = str.encode('protocol', 'utf-16')
s3 = bytes.decode(u_s3, 'utf-16')
print('\nu_s3 (utf-16) = {}, type u_s3 = {}, len u_s3 = {}\n'
      's3 = {}, type s3 = {}, len s3 = {}'.format(u_s3, type(u_s3), len(u_s3), s3, type(s3), len(s3)))

u_s4 = str.encode('standard', 'utf-32')
s4 = bytes.decode(u_s4, 'utf-32')
print('\nu_s4 (utf-32) = {}, type u_s4 = {}, len u_s4 = {}\n'
      's4 = {}, type s4 = {}, len s4 = {}'.format(u_s4, type(u_s4), len(u_s4), s4, type(s4), len(s4)))

print('\n----------\nЗадание 5\n----------')

class Web_ping:

    def __init__(self, resource):
        args = ['ping', resource]
        subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

        for line in subproc_ping.stdout:
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))

Web_ping('yandex.ru')
Web_ping('youtube.com')

print('\n----------\nЗадание 6\n----------')

with open('test_file.txt', 'w') as file_w:
    file_w.write('сетевое программирование\n')
    file_w.write('сокет\n')
    file_w.write('декоратор\n')

print(file_w)

with open('test_file.txt', 'r') as file_r:
# with open('test_file.txt', 'r', 'utf-8') as file_r:
    for line in file_r:
        print(line)