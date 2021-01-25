# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:33:48 2021

@author: 91967
"""

import pandas as pd
import cv2
import os
import matplotlib.pyplot as plt

main_path = '/content/drive/MyDrive/Personal_Projects/Waldo/Datasetv2/'

files = os.listdir('/content/drive/MyDrive/Personal_Projects/Waldo/Datasetv2')
#print(files)

orig_path = files[0]
solved_path = files[1]


total_imgs = os.listdir(main_path+orig_path)
#print(total_imgs)

soln_inter = os.listdir(main_path + solved_path)
print(soln_inter)

total_solns = os.listdir(main_path+solved_path+'/'+soln_inter[1])
print(total_solns)



#print(len(total_imgs))

train_size = round(0.7*len(total_imgs))
#print(train_size)

#print(total_imgs[:train_size])

ind = 0 #Which image is being referenced at the moment
df = pd.DataFrame(columns=['Filename','Width','Height','Class','xmin','xmax','ymin','ymax'])
for ind in range(train_size):
    img1 = cv2.imread(main_path+orig_path+'/'+total_imgs[ind])
    plt.imshow(img1)
    
    ht,wt = img1.shape[:2]
    
    
    for filename in total_solns:
        names = filename.split('_')
        '''
        print(names)
        print(names[0])
        print(str(ind))
        '''
        if names[0] == str(ind+1):
            final = filename
            #print(main_path+solved_path+'/'+soln_inter[1]+'/'+filename)
            break
        
    #print(main_path+solved_path+'/'+soln_inter[1]+'/'+final)
    
    ref = cv2.imread(main_path+solved_path+'/'+soln_inter[1]+'/'+final)
    plt.imshow(ref)    
    
    result = cv2.matchTemplate(img1,ref,cv2.TM_CCOEFF)
    (_,_,minLoc,maxLoc) = cv2.minMaxLoc(result)
    '''
    print(minLoc)
    print(maxLoc)
    '''
    topLeft = maxLoc
    botRight = (topLeft[0] + wt,topLeft[1] + ht)
    '''
    print(topLeft)
    print(botRight)
    '''
    #df = pd.DataFrame(columns=['Filename','Width','Height','Class','xmin','xmax','ymin','ymax'])
    
    df2 = {'Filename':total_imgs[ind],
           'Width':wt,'Height':ht,
           'Class':'Waldo',
           'xmin':botRight[1],
           'xmax':botRight[0],
           'ymin':topLeft[1],
           'ymax':topLeft[0]}
    df = df.append(df2,ignore_index=True)
 
df.to_csv(main_path+'annotations.csv')



