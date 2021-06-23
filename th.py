from PIL import Image
from numpy import asarray


def gs(name):
    img = Image.open(name).convert('LA')
    img.save('grey.png')

def exist(a_list, index):
    return(index < len(a_list))

def th(imageArr, tInit):
    tOld = tInit

    lessT = 0
    lessC = 0
    moreT = 0
    moreC = 0
    tempArr = imageArr.copy()

    while 1 < 2:
        for i in range(0, len(imageArr)):
            for j in range(0, len(imageArr[i])):
                for k in range(0, len(imageArr[i][j])):
                    if(imageArr[i][j][k] > tOld):
                        moreT += imageArr[i][j][k]
                        moreC += 1
                    else:
                        lessT += imageArr[i][j][k]
                        lessC += 1
        tNew = ((lessT/lessC) + (moreT/moreC)) / 2

        if not(abs(tOld - tNew) > abs(tNew - tInit)):
            for i in range(0, len(imageArr)):
                for j in range(0, len(imageArr[i])):
                    if(imageArr[i][j][0] > tNew):
                        tempArr[i][j][0] = 255
                        if(exist(tempArr[i][j], 1)): tempArr[i][j][1] = 255
                        if(exist(tempArr[i][j], 2)): tempArr[i][j][2] = 255
                    else:
                        tempArr[i][j][0] = 0
                        if(exist(tempArr[i][j], 1)): tempArr[i][j][1] = 0
                        if(exist(tempArr[i][j], 2)): tempArr[i][j][2] = 0
            Image.fromarray(tempArr).save(str(tInit) + '_segmen.png')
            break

        tOld = tNew
        lessT = 0
        lessC = 0
        moreT = 0
        moreC = 0


#gs('zoro.jpg')

nImage = Image.open('grey.png')
th(asarray(nImage), 64)
