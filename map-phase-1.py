import re
import sys
def cleanxml(raw):
    clean = re.compile('&(g|l)t;')
    cleantext = re.sub(clean, ' ', raw)
    return cleantext


for line in sys.stdin:
    if line.find('row',0,len(line))!=-1:
        if line.find('Tags=',0,len(line)) != -1:
            a = line.index('Tags=')+6
            b = (line.find('\"',a,len(line)))
            s = cleanxml(line[a:b])
            temp = ''
            for i in range(0 , len(s)-1):
                if (s[i] != ' '):
                    temp += s[i]
                elif (s[i]== ' ' and s[i+1] == ' '):
                    print(temp,1)
                    temp = ''

