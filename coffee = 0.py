coffee = 0
i = int(input("자판기에 돈을 넣으시오\n"));

while (i >= 300):

    coffee = coffee + 1;
    i = i - 300;

print("커피 " + str(coffee) + "잔, 잔돈 " + str(i) + "원");