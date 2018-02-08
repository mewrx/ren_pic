import os

class A():

    def __init__(self):
        self.cnt = 10000

    def f(self):
        self.cnt += 1
        return self.cnt
a = A() #счетчик

print('*'*40+'\n'+os.getcwd()+'\n'+'*'*40)
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".png"):
            print(os.path.join(root, file))
            os.rename(os.path.join(root, file), os.path.join(root, str(a.f()) + '.png'))
        elif file.endswith(".jpg"):
            print(os.path.join(root, file))
            os.rename(os.path.join(root, file), os.path.join(root, str(a.f()) + '.jpg'))
        elif file.endswith(".jpeg"):
            print(os.path.join(root, file))
            os.rename(os.path.join(root, file), os.path.join(root, str(a.f()) + '.jpeg'))
        elif file.endswith(".gif"):
            print(os.path.join(root, file))
            os.rename(os.path.join(root, file), os.path.join(root, str(a.f()) + '.gif'))
input('\n[*]Renamed ' + str(a.cnt - 10000) + ' pictures\n')

