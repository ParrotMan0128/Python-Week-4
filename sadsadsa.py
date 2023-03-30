import random as r;

for i in range(5):

    lotto_n = r.sample(range(1, 46), 6);
    lotto_n.sort();
    
    for j in lotto_n:

        print(f"{j}", end=" ");

    print("");