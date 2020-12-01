import pygame

pygame.init()  # 초기화 반드시필요하다.

##### 화면 크기 설정
screen_width = 480 # 가로 크기
screen_hight = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_hight))

##### 게임 화면 타이틀 설정
pygame.display.set_caption("Mato Game")  # 게임 이름


##### 배경이미지 불러오기 (개임 내)
#background = pygame.image.load("C:/Users/82104/Desktop/pygame_basic/background.png") # 배경이미지불러오기

##### 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get():  # 이벤트 루프라는것은 프로그램이 종료되지 않게 대기 함으로 중간에 마우스 키보드 어떤 동작이 들어오는지 확인
        if event.type == pygame.QUIT: # 프로그램 맨위에에서 X버튼을 누른다면 파이게임창이 꺼질때 이 이벤트가 발생된다.
            running = False           # 러닝이 Flase로 바뀌어서 게임 종료

    #screen.blit(background, (0.0)) # 배경이미지 불러오기 게임창왼쪽맨위가 0,0 이기때문에 알아서 들어감
    screen.fill((0,0,255)) # RGB 로 배경 채워주기

    pygame.display.update()        # 게임화면 다시 그리기

##### runninf Flase 가되면 게임종료 처리
pygame.quit()
