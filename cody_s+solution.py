import time
primes = [1, 2]  # create a list to store our prime numbers

# very large number hopefully the 10001 prime is in there
for i in range(3, 120000):
    if i % 2 != 0 and i != 2:
        # add every odd number to our list
        primes.append(i)

i = 2
# defines the starting time
start = time.time()
while(i < len(primes)):
    j = i  # define j
    while(j < len(primes)):
        # if the number at index j is divisable
        # by prime[i] then it is not prime
        # and it is removed unless it IS prime[i]
        if (primes[j] % primes[i] == 0) and (primes[j] != primes[i]):
            primes.remove(primes[j])
        j = j + 1
    i = i + 1
    print " # of primes : ",
    print i  # tells us how many prime numbers we have already found
print "the number of primes in 120,000 is : ",
print len(primes)  # prints the final number of prime numbers
print "the 10001 prime number is : ",
print primes[10001]  # prints the 10001 prime number
end = time.time()  # defines the ending time
print "total run time : ",
print (end - start)  # displays running time
