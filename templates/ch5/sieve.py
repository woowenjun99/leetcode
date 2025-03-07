_sieve_size = 0
bs = []
primes = []

def sieve(upperbound):
  global _sieve_size, bs, primes

  _sieve_size = upperbound+1
  bs = [True] * 10000010
  bs[0] = bs[1] = False
  for i in range(2, _sieve_size):
    if bs[i]:
      for j in range(i * i, _sieve_size, i):
        bs[j] = False
      primes.append(i)

def isPrime(N):
  global _sieve_size, primes
  if N <= _sieve_size:
    return bs[N]
  for p in primes:
    if p * p > N:
      break
    if N % p == 0:
      return False
  return True

def main():
  global primes

  sieve(10000000)
  i = primes[-1]+1
  while True:
    if isPrime(i):
      print('The next prime beyond the last prime generated is %d' % i)
      break
    i += 1
  print(isPrime(2**31-1))
  print(isPrime(136117223861))

main()