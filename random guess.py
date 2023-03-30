import random as r;

tries = 0;
guess = 0;

answer = r.randint(1, 100);

print("1부터 100 사이의 숫자를 맞추시오");

while (guess != answer):

    guess = int(input("숫자를 입력하시오: "));
    tries = tries + 1;

    if (guess < answer):

        print("입력값이 정답보다 낮습니다.");

    elif (guess > answer):

        print("입력값이 정답보다 높습니다.");

    else:

        print("정답입니다! | 시도 횟수: " + str(tries));
        break;

    if (tries >= 10):

        print("실패! 정답은 " + str(answer) + "입니다!");
        break; 