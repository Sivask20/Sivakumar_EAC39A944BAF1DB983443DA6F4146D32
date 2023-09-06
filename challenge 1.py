def fac_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fac_rec(n - 1)


number = int(input("enter the number : "))
res = fac_rec(number)
print("the factorila of {} is {} .".format(number, res)