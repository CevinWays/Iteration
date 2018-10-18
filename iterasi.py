print('Masukkan nilai x :')
x=int(input())

print('Masukkan nilai n :')
y=int(input())

def iteratif(n):
  if(n==1):
    hasil = x
    print(hasil)
  else:
    hasil = x*iteratif(n-1)
    print(hasil)
  return hasil
print("\n\nUlang x sebanyak n ")
print("\n\nHasil Iteratif :")
iteratif(y)