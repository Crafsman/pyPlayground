import urllib.request
import os


def findandMkFolder(folder):
    isexist = os.path.exists(folder)  # judge the spicific folder is exist
    if isexist == False:  # if not exist
        # print(isexist)
        os.makedirs(folder)  # then make the corresponding folder
    os.chdir(folder_name)


folder_name = 'cat_home'
findandMkFolder(folder_name)  # find or make a folder
print(os.path.abspath('.'))

width = 300
height = 300
for ii in range(1, 6):
    width += 100
    height = 300
    for jj in range(1, 6):
        height += 100
        # print(width, height)

        url = 'http://placekitten.com/g'
        url += '/' + str(width)
        url += '/' + str(height)
        # print(url)
        response = urllib.request.urlopen(url)
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        cat_img = response.read()

        file_name = 'cat'
        file_name += str(ii * jj)
        file_name += '.jpg'
        with open(file_name, 'wb') as f:
            if f.write(cat_img):
                print('find cat' + file_name)

# for i in range(0, 10):
#    file_name = 'cat'
#    file_name += str(i)
#    file_name += '.jpg'
#    with open(file_name, 'wb') as f:
#        if f.write(cat_img):
#            print('find cat' + file_name)






