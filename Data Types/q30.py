dict = {1:9, 2:10, 3:11, 4:12, 5:13, 6:14}

def is_key_present(x):
  if x in dict:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')


key = int(input('Enter the key: '))
is_key_present(key)