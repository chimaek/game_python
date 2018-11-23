import pygame
import random
from time import sleep

# 배경색,게임화면크기,객체 사이즈 설정
BGcolor = (255, 255, 255)
width = 600
height = 840
BG_height = -840
unit_width = 67
unit_height = 67
enemy_width = 108
enemy_height = 67


# 게임에 집어넣을 객체를 만드는 함수
def into_Game(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))


def runGame():
    global gamepad, clock, unit, BG, BG1
    global enemy, fires, bullet, boom
    # 총알 명중 플래그 선언
    is_enemy_dead = False
    boom_count = 0

    bullet_xy = []
    # 비행기 좌표설정
    x = width * 0.05
    y = height * 0.85
    # 비행기 좌표를 변경할 변수 선언
    changeX = 0
    # 배경화면 설정
    BG_X = 0
    BG_X2 = BG_height
    # 적, 방해물 위치 지정
    enemy_x = random.randrange(0, width)
    enemy_y = -67
    fire_x = random.randrange(0, width)
    fire_y = -140
    random.shuffle(fires)
    fire = fires[0]

    # 플래그 설정
    crashe = False
    while not crashe:
        # event.get()은 게임에서 발생하는 이벤트 반환하는 함수입니다.
        for event in pygame.event.get():
            # 마우스로 창을 닫을경우 플래그를 설정하여 while문을 빠져나옵니다.
            if event.type == pygame.QUIT:
                crashe = True
            # 키입력시 x좌표를 업데이트함
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    changeX = -5
                elif (event.key == pygame.K_RIGHT):
                    changeX = 5
                # Z키를 누르면 총알 위치 설정
                elif (event.key == pygame.K_z):
                    bulletX = x
                    bulletY = y - 50
                    bullet_xy.append([bulletX, bulletY])
                # 일시 정지 5초
                elif (event.key == pygame.K_SPACE):
                    sleep(5)
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    changeX = 0
        x += changeX
        # 비행기가 배경화면을 넘어가지 않게 하는 if문
        if (x < 0 or x > width - 67):
            x -= changeX

        # 게임판을 흰색으로 채우기
        gamepad.fill(BGcolor)
        BG_X += 2
        BG_X2 += 2

        if BG_X == -BG_height:
            BG_X = BG_height
        if BG_X2 == -BG_height:
            BG_X2 = BG_height

        # 배경화면 호출함.
        into_Game(BG, 0, BG_X)
        into_Game(BG1, 0, BG_X2)

        # 적이 화면을 넘어가면 재생성하는 if문
        enemy_y += 7
        if enemy_y >= height:
            enemy_x = random.randrange(0, width - 108)
            enemy_y = -67

        # 방해물이 없다면 방해물이 나오는 속도를 조절하는 함수
        if fire == None:
            fire_y += 30
        else:
            fire_y += 15
        if fire_y >= height:
            fire_x = random.randrange(0, width - 61)
            fire_y = -140
            random.shuffle(fires)
            fire = fires[0]

        # enumerate는 튜플형태로 반환한다 [인덱스,값]
        if len(bullet_xy) != 0:
            for index, positon in enumerate(bullet_xy):
                positon[1] -= 15
                bullet_xy[index][1] = positon[1]
                # 총알이 적에 명중
                # 왜?
                if positon[1] > enemy_y and positon[1] < enemy_y + enemy_height:
                    if positon[0] > enemy_x and positon[0] < enemy_x + enemy_width:
                        bullet_xy.remove(positon)
                        is_enemy_dead = True
                if positon[0] <= -50:

                    bullet_xy.remove(positon)


        if not is_enemy_dead:
            into_Game(enemy, enemy_x, enemy_y)
        else:
            into_Game(boom, enemy_x, enemy_y)
            boom_count += 1
            if boom_count > 5:
                boom_count = 0
                enemy_x = width
                enemy_y = random.randrange(0, height - enemy_height)
                is_enemy_dead = False

        # 적과 방해물 호출
        into_Game(enemy, enemy_x, enemy_y)
        if fire != None:
            into_Game(fire, fire_x, fire_y)

        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                into_Game(bullet, bx, by)
        # 비행기 호출함.
        into_Game(unit, x, y)

        # 게임판을 그림
        pygame.display.update()
        # fps 60으로 설정합니다,
        clock.tick(60)
    # 초기화한 pygame종료합니다.
    pygame.quit()
    quit()


# 게임을 초기화 하고 시작하는 함수입니다.
def initGame():
    # 전역 변수로 설정합니다.
    global gamepad, clock, unit, BG, BG1
    global enemy, fires, bullet, boom
    fires = []
    # 파이게임 라이브러리를 초기화함 꼭 호출해줘야 합니다.
    pygame.init()
    # 게임 판 화면 설정
    gamepad = pygame.display.set_mode((width, height))
    # 게임 제목 설정
    pygame.display.set_caption("떴다 떴다 비행기")
    # 비행기 이미지 로딩
    unit = pygame.image.load('images/aircraft.png')
    # 배경화면 로딩
    BG = pygame.image.load('images/background.png')
    BG1 = BG.copy()
    # 적 이미지 및 방해물 추가
    enemy = pygame.image.load('images/bat.png')
    fires.append(pygame.image.load('images/fireball.png'))
    fires.append(pygame.image.load('images/fireball2.png'))
    # 불덩어리 2개와 None객체 5개 넣을 리스트
    for i in range(5):
        fires.append(None)
    # 총알이미지 추가
    bullet = pygame.image.load('images/bullet.png')
    # 폭발이미지 추가
    boom = pygame.image.load('images/boom.png')
    # 초당 프레임을 위한 변수 생성
    clock = pygame.time.Clock()
    # runGame 함수 호출
    runGame()


initGame()
