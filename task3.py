x = int(input())
y = int(input())
if x==0 and y==0:
    print("точка находится в начале координатной оси")
elif x>0:
    if y>0:
        print("точка находится в первей четверти координатной плоскости")
    if y<0:
        print("точка находится во второй четверти координатной плоскости")
    if y==0:
        print("точка находится на оси координат")
elif x<0:
    if y<0:
        print("точка находится в третей четверти координатной плоскости")
    if y>0:
        print("точка находится в четвертой четверти координатной плоскости")
    if y==0:
        print("точка находится на оси координат")
elif x==0 or y==0:
    print("точка находится на оси координат")
