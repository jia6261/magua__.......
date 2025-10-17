print("hi")
import time
time.sleep (1)

print("麻瓜")
time.sleep (1)
print ("祝你一路走好🪦")
print("https://www.bilibili.com/opus/1124621325153861653?plat_id=186&share_from=dynamic&share_medium=android_i&share_plat=android&share_session_id=9d2fb83b-e24b-4c70-8a22-cb97690621a5&share_source=COPY&share_tag=s_i&spmid=dt.dt-detail.0.0&timestamp=1760687334&unique_k=XtY1HGP")
import turtle

# 设置窗口
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("祝福语")

# 创建海龟
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-100, 0)  # 调整位置
t.pendown()

# 设置字体（需要系统支持中文字体）
font = ("SimHei", 36, "bold")  # 黑体，36号，加粗

# 写文字
t.write("麻瓜祝你一路走好", font=font, align="left")

# 保持窗口打开
turtle.done()

while True:
    print("('~')")
    time.sleep(1)
    print()
