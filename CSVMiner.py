import csv
import urllib.request
import shutil
import requests
import os

#probably needs to pip some stuff to work for either urllib and requests

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)  

#updates train and test folders in image folder

#clean train folder
if os.path.isdir('Images/Train'):
    shutil.rmtree('Images/Train')
if not os.path.isdir('Images/Train'):
    os.makedirs('Images/Train',755)

#clean test folder
if os.path.isdir('Images/Test'):
    shutil.rmtree('Images/Test')
if not os.path.isdir('Images/Test'):
    os.makedirs('Images/Test',755)

with open('Hack@WPI - Sheet1.csv','r') as f1:
    reader = csv.reader(f1)
    next(reader)
    trustLevel = 10 # Absolute value of trust level to consider trusted
    trustedURLs = []
    testURLs = []
    count = 2
    for line in reader:
        if (int(line[1]) == trustLevel) or (int(line[1]) == -trustLevel):
            trustedURLs.append({'url':line[0], 'val':line[1], 'line':count})
##            print ("found trusted img")
        if (count-2)%5 == 0:
            testURLs.append({'url':line[0], 'val':line[1], 'line':count})
        count+=1

    for t in trustedURLs:
        imgName = ""
        if int(t['val']) > 0:
            imgName = "choc"+str(t['line'])
        else:
            imgName = "oat"+str(t['line'])
        try:            
            urllib.request.urlretrieve(t['url'], imgName+".jpg")
##            print("downloaded trusted img")
            shutil.move(imgName+".jpg", "Images/Train")
        except Exception as e:
            print ('img number: '+str(t['line']))
            print(e)
        else:
            continue

    for t in testURLs:
        imgName = ""
        if int(t['val']) >= 0:
            imgName = 'choc'+str(t['line'])
        else:
            imgName = 'oat'+str(t['line'])
        try:    
            urllib.request.urlretrieve(t['url'], imgName+".jpg")
##            print("downloaded test img")
            shutil.move(imgName+".jpg", "Images/Test")
        except Exception as e:
            print ('img number: '+str(t['line']))
            print(e)
        else:
            continue

    print ("done")
