import os

path = "G:\codes\H73\design_tool"
path.replace('\\', "\\\\")
print(1, path)
path = os.path.abspath(os.path.dirname(path)) + '\\editor_data\\game_common\\dialog\\editor_data'
print(2, path)

print(os.listdir(path))
print(os.path.abspath(os.pardir))
p = 'abc'
print(os.path.join(p, 'hhh'))

for a,b,c in os.walk(os.curdir):
    print(a,b,c)

print(os.curdir, os.getcwd())
a = os.path.realpath(__file__)
b = os.path.dirname(a)
c = os.path.join(b, '../../')
d = os.path.abspath(c)
print(a, b, c, d)

