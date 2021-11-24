import re

# number = input()

# x = re.match(r'^(1|8|9)\d{7}\b', number)

# if x:
    # print('Valid')
# else:
    # print('Invalid')

def func(first, second=1, *args, **kwargs):
    print(kwargs)
    print(args)

func(1,2,3,4,5,6,7,therd=3, fourth=100)

# a,b,*c,d = [1,2,3,4,5,6,7]

# print(a)
# print(b)
# print(c)
# print(d)

# a=7
# b = 1 if a>=5 else 42;
# print(b)

# for i in range(10):
#     if i == 99:
#         break
# else:
#     print("unbroken 1")
# for i in range(10):
#     if i == 4:
#         break
# else:
#     print("unbroken 2")

# try:
#     print(1)
# except ZeroDivisionError:
#     print(2)
# else: 
#     print(3)

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print(2)
# else: 
#     print(3)

print(__name__)