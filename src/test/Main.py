#coding:utf-8
'''
Created on 2019/08/09

@author: 
'''

import sys
import re

timetable = {}

class StatItems(object):
    '''
    classdocs
    '''

    def __init__(self, keyStr, status, timestr):
        '''
        Constructor
        '''
        self.keyStr  = keyStr
        self.status = status
        self.timestr = timestr

def main():
    args = sys.argv
    
    filepath = args[1]
    with open( filepath,  encoding='cp932',mode ='r') as f:
        for row in f:
            getStatistics( row.strip() )
            
    for k,v in timetable.items():
        print( k ,',', v)
    
    sys.exit(0)

def getStatistics( line ):
    m = re.match( "\[(.*)\]---\[(.+)\]\[(.+)\]", line )
    if m:
        key = m.group(1)
        status = m.group(2)
        timestr = timeToSec( m.group(3))
        
        if status=="START":
            timetable[ key ] = timestr
        elif status=="END":
            starttime = timetable.get(key, -1)
            if starttime == -1:
                print( "log format error!")
                return 0,0,0
            else:
                timetable[ key ] = timestr - starttime
        
        return key, status ,timestr
         
    else:
        pass # continue
        
def timeToSec( timestr ):
    totalSec = 0
    
    m = re.match( "^(\\d\\d):(\\d\\d):(\\d\\d)\\.\\d\\d$", timestr)
    if m:
        hour = int(m.group(1))
        minute = int(m.group(2))
        second = int(m.group(3))
        totalSec = hour*3600 + minute*60 + second 
        
    else:
        print("Time format error.")
        sys.exit(1)
        
    return totalSec

if __name__ == '__main__':
    main()
