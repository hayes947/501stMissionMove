##501st copy-paste script CR-C Pastor, CC Klein
import os
def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    print ('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            print ('%s in r[i]' %(name))
            return True
    return False
    if name == 'main':
        '''
        This code checks tasklist, and will print the status of a code
        '''
        imgName = 'dwm.exe'
        notResponding = 'Not Responding'
        r = getTasks(imgName)
        if not r:
            print('%s - No such process' % (imgName)) 
        elif 'Not Responding' in r:
            print('%s is Not responding' % (imgName))
        else:
            print('%s is Running or Unknown' % (imgName))

canMove=not(getTasks('arma3server_x64.exe'))
##pSrc=path to source pDes=path to destination
def move(pSrc, pDes):
    if canMove:
        if (os.path.isfile(pDes)==False):
            os.system('copy '+pSrc+' '+pDes)
        elif (os.path.getmtime(pSrc)!=os.path.getmtime(pDes)):
            os.system('copy '+pSrc+' '+pDes)

move('abc.txt', 'copy_abc.txt')
move('abc.txt', 'def.txt')
