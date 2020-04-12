The first goal of the second part of the assignment is to find a function of r
(number of switch ports to be connected to other switches in Jellyfish) as a function of n (number of ports of a switch)
so that N (number of servers), S (number of switches) and L (number of links)
are the same for Jellyfish and Fat-tree.

Now, the Jellyfish approach is to construct a random graph a the top-of-rack (ToR) switch layer:
in a r-regular random graph we know that N = S*(n-r)
and using some algebra we have...

N = S*n - S*r
S*r = S*n - N
r = n - N/S

At this point we insert into the obtained formula the following values of Fat-tree:
N = (n^3)/4      ;      S = (5*n^2)/4      ;       L = (3/4)*n^3
(with L = 3N)

So we finally have:
r = n - [(n^3)/4]/[(5*n^2)/4]
r = n - (1/5)*n

r = (4/5)*n
