def segmentedDelay(nodes, packets):
    p = .001
    L = 10000
    C = 1000000
    h = 100

    first = p + nodes*((((L/packets)+ h)/C)+2*p)
    last = packets * ((((L/packets)+ h)/C)+2*p)

    return first + last

while(True):
    K =int(input("Enter the number of nodes: "))
    n = int(input("Enter the number of packets: "))
    if n == -1 or K == -1:
        break
    print("Total time to transmit 10000 bits in", n, "packets through", K, "nodes is:")
    print(segmentedDelay(K, n))