f=open('word.txt','w')

for i in range(100):
    f.write('word'+str(i)+'|'+'词性'+str(i)+'|'+'释义'+str(i)+'\n')
    
f.close()
