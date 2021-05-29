word =['c=','c-','dz=','d-','lj','nj','s=','z=']

IN = input()

for i in word:
  IN = IN.replace(i,'*')
print(len(IN))