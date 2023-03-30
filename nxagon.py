import turtle as t;

t.shape("turtle");

s = t.textinput("", "몇각형을 원하세요?");
s = int(s);

t.speed(s);

for i in range(s):

    t.left(360/s);
    t.forward(1000/s);

t.mainloop();
t.bye();