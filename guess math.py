import random as r;

score = 0;

while (True):
       
    x = r.randint(1, 100);
    y = r.randint(1, 100);

    answer = x + y;

    guess = int(input(f"{x} + {y} = "));

    if (answer == guess):

        score = score + 1;
        print(f"정답이에요! 점수: {score}");

    else:

        print("오답이에요... 다음번엔 잘 할수 있죠?");
        print("점수: " + f"{score}");
        break;