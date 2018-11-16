import pygame

# 배경색과 창크기 설정
BGcolor_white=(255,255,255)
width=1280
height=1024

def runGame():
    global gamepad,clock
    #플래그 설정
    crashe=False

    while not crashe:
        #event.get()은 게임에서 발생하는 이벤트 반환하는 함수입니다.
        for event in pygame.event.get():
            # 마우스로 창을 닫을경우 플래그를 설정하여 while문을 빠져나옵니다.
            if event.type==pygame.QUIT:
                crashe=True
        # 그것이 아니라면 게임판을 흰색으로 채우고
        gamepad.fill(BGcolor_white)
        # 게임판을 그리고
        pygame.display.update()
        #fps 60으로 설정합니다,
        clock.tick(60)
    # 초기화한 pygame종료합니다.
    pygame.quit()

#게임을 초기화 하고 시작하는 함수입니다.
def initGame():
    #전역 변수로 설정합니다.
    global gamepad,clock
    #파이게임 라이브러리를 초기화함 꼭 호출해줘야 합니다.
    pygame.init()
    #게임 판 화면 설정
    gamepad=pygame.display.set_mode((width,height))
    # 게임 제목 설정
    pygame.display.set_caption("떴다 떴다 비행기")
    #초당 프레임을 위한 변수 생성
    clock=pygame.time.Clock()
    #runGame 함수 호출
    runGame()

initGame()