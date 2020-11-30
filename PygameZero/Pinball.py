import pgzrun # 导入游戏库


HEIGHT = 600 # 设置窗口的高度
WIDTH = 800 # 设置窗口的宽度
x = WIDTH / 2 # 小球X轴坐标，初始化在窗口中间
y = HEIGHT / 2 # 小球Y轴左边，初始化在窗口中间
speed_x = 3 # 小球X方向的速度
speed_y = 3 # 小球Y方向的速度
r = 10 # 小球的半径

def draw(): # 绘制模块，每帧重复执行
    screen.fill('white') # 白色背景
    # 绘制一个填充圆，坐标为(x, y)，半径为r，颜色为红色
    screen.draw.filled_circle((x, y), r, "red")

def update(): # 更新模块， 每帧重复执行
    global x, y, speed_x, speed_y # 要重复更新的变量
    x += speed_x # 利用X方向速度更新X坐标
    y += speed_y # 利用Y方向速度更新Y坐标
    if x >= WIDTH - r or x <= r: # 当小球碰到左右边界时
        speed_x = -speed_x # X方向速度反向
    if y >= HEIGHT - r or y <= r: # 当小球碰到上下边界时
        speed_y = -speed_y # Y方向速度反向

pgzrun.go()
