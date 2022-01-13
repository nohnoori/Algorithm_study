def solution(n, arr1, arr2):
  return [bin(a|b)[2:].zfill(n).replace('0',' ').replace('1','#') for a,b in zip(arr1,arr2)]
