import pygame
import random
import math

pygame.init()
pygame.mixer.init()
pygame.font.init()

WIN_W = 1600
WIN_H = 780

t1 = 0.18  # 时间流速
show_n = 0
show_frequency = 0.0015  # 烟花绽放频率，数值越大频率越高

color_list = [
    [255, 0, 0]
]

shan_min_height = 400
shan_max_height = 150
yanhua_times = 30
yanhua_size = 900
yanhua_num = 5

yanhua_map = {}
fk_list = []
a = 30
gift = 1


class Fireworks():
    is_show = False
    x, y = 0, 0
    vy = 0
    p_list = []
    color = [0, 0, 0]
    v = 0
    cnt = 0

    def __init__(self, x, y, vy, n=300, color=[0, 255, 0], v=10):
        self.x = x
        self.y = y
        self.vy = vy
        self.color = color
        self.v = v
        self.cnt = 0
        self.p_list = []
        for i in range(n):
            self.p_list.append([random.random() * 2 * math.pi, 0, v * math.pow(random.random(), 1 / 3)])

    def run(self):
        global show_n
        for p in self.p_list:
            p[1] = p[1] + (random.random() * 0.6 + 0.7) * p[2]
            p[2] = p[2] * 0.98
            # TODO 去掉的话会越变越大，打开的话会越来越淡
            # 淡或浓
            if p[2] < 1.2:
                self.color[0] *= 0.9999
                self.color[1] *= 0.9999
                self.color[2] *= 0.9999

            if max(self.color) < 10 or self.y > WIN_H + p[1]:
                show_n -= 1
                self.is_show = False
                break
        self.vy += 10 * t1
        self.y += self.vy * t1


def random_color(l, r):
    return [random.randint(l, r), random.randint(l, r), random.randint(l, r)]


def red_random(l, r):
    return [255, random.randint(l, r), random.randint(l, r)]


def green_random(l, r):
    return [random.randint(l, r), 255, random.randint(l, r)]


def init_yanhua(bg_size):
    yanhua_list = []
    for i in range(yanhua_num):
        x_site = random.randrange(175, 350)  # 雪花圆心位置
        y_site = WIN_H  # 雪花圆心位置
        X_shift = 0  # x 轴偏移量
        radius = random.randint(4, 6)  # 半径和 y 周上升降量
        xxxxx = random_color(150, 255)
        red = xxxxx[0]
        green = xxxxx[1]
        blue = xxxxx[2]
        yanhua_list.append([x_site, y_site, X_shift, radius, red, green, blue])
    return yanhua_list


def init_xue(bg_size):
    snow_list = []
    for i in range(200):
        x_site = random.randrange(0, bg_size[0])  # 雪花圆心位置
        y_site = random.randrange(0, bg_size[1])  # 雪花圆心位置
        X_shift = random.randint(-1, 1)  # x 轴偏移量
        radius = random.randint(4, 6)  # 半径和 y 周下降量
        xxxxx = random_color(150, 255)
        # red = xxxxx[0]
        # green = xxxxx[1]
        # blue = xxxxx[2]
        snow_list.append([x_site, y_site, X_shift, radius, 255, 255, 255])
    return snow_list


def init_shan(bg_size):
    shan_list = []
    # [x,y,color]
    shan_list.append([0, shan_min_height, green_random(1, 150)])
    shan_list.append([200, shan_max_height, green_random(1, 150)])
    shan_list.append([400, shan_min_height, green_random(1, 150)])
    shan_list.append([600, shan_max_height, green_random(1, 150)])
    shan_list.append([800, shan_min_height, green_random(1, 150)])
    shan_list.append([1000, shan_max_height, green_random(1, 150)])
    shan_list.append([1200, shan_min_height, green_random(1, 150)])
    shan_list.append([1400, shan_max_height, green_random(1, 150)])
    shan_list.append([1600, shan_min_height, green_random(1, 150)])
    return shan_list


def draw_shan(shan_list: [], screen):
    n = len(shan_list)
    for i in range(1, n):
        pygame.draw.line(screen, shan_list[i - 1][2], (shan_list[i - 1][0], shan_list[i - 1][1]),
                         (shan_list[i][0], shan_list[i][1]), width=3)


def draw_xue(snow_list: [], screen, bg_size: [], grand_has: set, grand_list: []):
    # 雪花列表循环
    # todo 空中的雪
    for i in range(len(snow_list)):
        # 绘制雪花，颜色、位置、大小
        pygame.draw.circle(screen, (snow_list[i][4], snow_list[i][5], snow_list[i][6]), snow_list[i][:2],
                           snow_list[i][3] - 3)
        # 移动雪花位置（下一次循环起效）
        snow_list[i][0] += snow_list[i][2]
        snow_list[i][1] += snow_list[i][3]
        # 如果雪花落出屏幕，重设位置
        if snow_list[i][1] > bg_size[1]:
            # tmp = []
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(0, bg_size[0])
            x = snow_list[i][0]
            y = bg_size[1]
            while (grand_has.__contains__(x * 10000 + y)):
                y = y - snow_list[i][3]
            grand_has.add(x * 10000 + y)
            grand_list.append(
                [x, y, snow_list[i][2], snow_list[i][3], snow_list[i][4], snow_list[i][5],
                 snow_list[i][6]])


def show_yanhua(fk, screen, n):
    global show_n
    # if not fk.is_show:
    #     fk.is_show = False
    #     if random.random() < show_frequency * (n - show_n):
    #         show_n += 1
    #         fk.again()
    fk.run()
    for p in fk.p_list:
        x, y = fk.x + p[1] * math.cos(p[0]), fk.y + p[1] * math.sin(p[0])
        # x, y = fk.x, fk.y
        if random.random() < 0.055:
            screen.set_at((int(x), int(y)), (int(fk.color[0]), int(fk.color[1]), int(fk.color[2])))
            # screen.set_at((int(x), int(y)), (255, 255, 255))
        else:
            screen.set_at((int(x), int(y)), (int(fk.color[0]), int(fk.color[1]), int(fk.color[2])))


def draw_yanhua(yanhua_list: [], screen, bg_size: []):
    global fk_list
    for i in range(len(yanhua_list)):
        # 绘制雪花，颜色、位置、大小
        pygame.draw.circle(screen, (yanhua_list[i][4], yanhua_list[i][5], yanhua_list[i][6]), yanhua_list[i][:2],
                           yanhua_list[i][3] - 3)
        # 移动雪花位置（下一次循环起效）
        yanhua_list[i][0] += yanhua_list[i][2]
        yanhua_list[i][1] -= yanhua_list[i][3]
        # 如果雪花落出屏幕，重设位置
        if yanhua_list[i][1] <= 0:
            # tmp = []
            yanhua_list[i][1] = WIN_H
            yanhua_list[i][0] = random.randrange(175, 350)
        if yanhua_list[i][1] <= random.randint(150, 300):
            # todo 放烟花
            fk = Fireworks(yanhua_list[i][0], yanhua_list[i][1], -20, n=yanhua_size, color=red_random(1, 150), v=10)
            fk_list.append(fk)
            yanhua_list[i][1] = WIN_H
            yanhua_list[i][0] = random.randrange(175, 350)


def show_shi(a: list, n, screen):
    i = 2 * n - 1
    j = 2 * n
    if i >= len(a):
        i = len(a) - 2
        j = len(a) - 1
    if i >= 0:
        myfont = pygame.font.SysFont('simHei', 30)
        textsurface = myfont.render(a[i], False, random_color(150, 255))
        screen.blit(textsurface, (WIN_W / 2, 30))
    if j >= 0:
        myfont = pygame.font.SysFont('simHei', 100)
        textsurface = myfont.render(a[j], False, red_random(1, 1))
        screen.blit(textsurface, (WIN_W / 2 - 200, 50))


def show_gift(flag, screen, bg_size: list, a):
    if flag == 1:
        pygame.draw.rect(screen, red_random(1, 150), ((175, bg_size[1] - 105), (200, 100)))
        pygame.draw.line(screen, (255, 225, 79), (200, bg_size[1] - 105), (200, bg_size[1] - 5), width=3)
        pygame.draw.line(screen, (255, 225, 79), (350, bg_size[1] - 105), (350, bg_size[1] - 5), width=3)
        pygame.draw.line(screen, (255, 225, 79), (200, bg_size[1] - 105), (350, bg_size[1] - 5), width=3)
        pygame.draw.line(screen, (255, 225, 79), (350, bg_size[1] - 105), (200, bg_size[1] - 5), width=3)
        pygame.draw.circle(screen, (255, 225, 79), (275, bg_size[1] - 55), a / 2)


def show_gift2(flag, screen, bg_size: list, a):
    if flag == 1:
        pygame.draw.rect(screen, red_random(1, 150), ((1044, 793), (1241, 893)))
        pygame.draw.line(screen, (255, 225, 79), (bg_size[0] - 200, bg_size[1] - 105), (bg_size[0] - 200, bg_size[1] - 5), width=3)
        pygame.draw.line(screen, (255, 225, 79), (bg_size[0] - 350, bg_size[1] - 105), (bg_size[0] - 350, bg_size[1] - 5), width=3)
        pygame.draw.line(screen, (255, 225, 79), (bg_size[0] - 200, bg_size[1] - 105), (bg_size[0] - 350, bg_size[1] - 5), width=3)
        pygame.draw.line(screen, (255, 225, 79), (bg_size[0] - 350, bg_size[1] - 105), (bg_size[0] - 200, bg_size[1] - 5), width=3)
        pygame.draw.circle(screen, (255, 225, 79), (bg_size[0] - 275, bg_size[1] - 55), a / 2)


# def draw_yueliang(screen):
#     pygame.draw.circle(screen, (200, 200, 200), (1350, 50), 100, 100)


def main():
    global show_n
    global fk_list
    bg_size = (WIN_W, WIN_H)

    screen = pygame.display.set_mode(bg_size)
    # bg_img = "./1.png"
    pygame.display.set_caption("思瑶小朋友新年快乐!")
    # bg = pygame.image.load(bg_img)
    # pygame.mixer.music.load('D:\\CloudMusic\\祖海 - 好运来.mp3')
    grand_list = []
    font_values = ['思瑶小朋友新年快乐!']

    grand_has = set()

    clock = pygame.time.Clock()
    yanhua_list = init_yanhua(bg_size)
    snow_list = init_xue(bg_size)
    shan_list = init_shan(bg_size)
    # 游戏主循环
    while True:
        show_n = 0
        # if not pygame.mixer.music.get_busy():
        #     pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                print(event)
            if event.type == pygame.QUIT:
                exit()
        screen.fill((0, 0, 0))
        flag = 0
        min_height = 100000
        # todo 地上的积雪
        for i in range(len(grand_list)):
            if grand_list[i][0] < 375 and grand_list[i][1] < bg_size[1] - gift:
                flag = 1
            if grand_list[i][0] < 375:
                min_height = min(min_height, grand_list[i][1])
        # if len(fk_list) != 0:
        #     print(len(fk_list))
        # # 放烟花
        show_shi(font_values, 10, screen)
        # draw_yueliang(screen)
        draw_shan(shan_list, screen)
        if flag == 1:
            draw_yanhua(yanhua_list, screen, bg_size)
            for fk in fk_list:
                fk.run()
                for p in fk.p_list:
                    x, y = fk.x + p[1] * math.cos(p[0]), fk.y + p[1] * math.sin(p[0])
                    screen.set_at((int(x), int(y)), (int(fk.color[0]), int(fk.color[1]), int(fk.color[2])))
                fk.cnt = fk.cnt + 1
        tmp = []
        for fk in fk_list:
            if fk.cnt <= yanhua_times:
                tmp.append(fk)
                break
        show_gift(flag, screen, bg_size, a)
        # show_gift2(flag, screen, bg_size, a)
        fk_list = tmp
        min_height = 100000
        # todo 地上的积雪
        for i in range(len(grand_list)):
            if grand_list[i][0] < 375:
                min_height = min(min_height, grand_list[i][1])

        draw_xue(snow_list, screen, bg_size, grand_has, grand_list)

        for i in range(len(grand_list)):
            pygame.draw.circle(screen, (grand_list[i][4], grand_list[i][5], grand_list[i][6]), grand_list[i][:2],
                               grand_list[i][3] - 3)
        pygame.display.update()
        time_passed = clock.tick(50)


if __name__ == '__main__':
    main()

