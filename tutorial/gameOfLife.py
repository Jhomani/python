treats = input()

queue = []

for i in range(int(treats)):
  lenth_loop = input()
  [size, iteration] = lenth_loop.split() 
  data = input()

  queue.append([int(iteration), data, int(size)])

for i in queue:
  for j in  range(i[0]):
    aux = i[1]
    for k in range(i[2]): 
      if k != 0 & k+1 != i[2]:
        if aux[k] == '0' and bool(aux[k+1] == '1') != bool(aux[k-1] == '1'):
          i[1] = i[1][:k] + '1' + i[1][k+1:]
      elif k == 0:
        if aux[k] == '0' and aux[k+1] == '1':
          i[1] = i[1][:k] + '1' + i[1][k+1:]
      else:
        if aux[k] == '0' and aux[k-1] == '1':
          i[1] = i[1][:k] + '1' + i[1][k+1:]
  print(i[1])
