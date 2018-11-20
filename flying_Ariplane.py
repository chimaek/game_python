import pygame
import random

# 배경색과 창크기 설정
BGcolor_white=(255,255,255)
width=500
height=700
BG_height= -700

#게임에 집어넣을 객체를 만드는 함수
def into_Game(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

def runGame():
    global gamepad,clock,unit,background,background1
    global bat,fires
    x=width*0.05
    y=height*0.8
    changeX=0
    backgroundX=0
    backgroundX2=BG_height

    bat_x = random.randrange(0,width)
    bat_y = height
    fire_x=random.randrange(0,width)
    fire_y=height
    random.shuffle(fires)
    fire=fires[0]

    #플래그 설정
    crashe=False

    while not crashe:
        # event.get()은 게임에서 발생하는 이벤트 반환하는 함수입니다.
        for event in pygame.event.get():
            # 마우스로 창을 닫을경우 플래그를 설정하여 while문을 빠져나옵니다.
            if event.type==pygame.QUIT:
                crashe=True
            # 키입력시 x좌표를 업데이트함
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_LEFT):
                    changeX = -5
                elif(event.key==pygame.K_RIGHT):
                    changeX = 5
            if(event.type==pygame.KEYUP):
                if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                    changeX = 0
        x += changeX

        # 게임판을 흰색으로 채우기
        gamepad.fill(BGcolor_white)
        backgroundX += 2
        backgroundX2 += 2
        bat_y-=7
        if bat_y<=0:
            bat_x = random.randrange(0,width)
            bat_y = height
        if fire==None:
            fire_y -= 30
        else:
            fire_y -= 15

        if fire_y <=0:
            fire_x = random.randrange(0,width)
            fire_y = height
            random.shuffle(fires)
            fire=fires[0]

        if backgroundX == -BG_height:
            backgroundX = BG_height
        if backgroundX2 == -BG_height:
            backgroundX2 = BG_height
        # 배경화면 호출함.
        into_Game(background,0,backgroundX)
        into_Game(background1,0,backgroundX2)
        # 적과 방해물 호출
        into_Game(bat,bat_x,bat_y)
        if fire != None:
            into_Game(fire,fire_x,fire_y)
        # 비행기 호출함.
        into_Game(unit,x,y)

        # 게임판을 그림
        pygame.display.update()
        #fps 60으로 설정합니다,
        clock.tick(60)
    # 초기화한 pygame종료합니다.
    pygame.quit()
    quit()

#게임을 초기화 하고 시작하는 함수입니다.
def initGame():
    #전역 변수로 설정합니다.
    global gamepad,clock,unit,background,background1
    global bat,fires
    fires=[]
    #파이게임 라이브러리를 초기화함 꼭 호출해줘야 합니다.
    pygame.init()
    #게임 판 화면 설정
    gamepad=pygame.display.set_mode((width,height))
    # 게임 제목 설정
    pygame.display.set_caption("떴다 떴다 비행기")
    #비행기 이미지 로딩
    unit=pygame.image.load('images/aircraft.png')
    # 배경화면 로딩
    background = pygame.image.load('images/background.png')
    background1 = background.copy()
    #적 이미지 추가
    bat=pygame.image.load('images/bat.png')
    # 방해물 추가
    fires.append(pygame.image.load('images/fireball.png'))
    fires.append(pygame.image.load('images/fireball2.png'))
    #불덩어리 2개와 None객체 5개 넣을 리스트
    for i in range(5):
        fires.append(None)
    # 초당 프레임을 위한 변수 생성
    clock = pygame.time.Clock()
    #runGame 함수 호출
    runGame()

initGame()