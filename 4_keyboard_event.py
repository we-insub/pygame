import pygame

pygame.init()  # 초기화 반드시필요하다.

##### 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

##### 게임 화면 타이틀 설정
pygame.display.set_caption("Mato Game")  # 게임 이름


##### 배경이미지 불러오기 (개임 내)
#background = pygame.image.load("C:/Users/82104/Desktop/pygame_basic/background.png") # 배경이미지불러오기

##### 스프라이트 / 캐릭터 불러오기
character = pygame.image.load("C:/Users/82104/Desktop/pygame_basic/2.png")
character_size = character.get_rect().size # 이미지 크기를 구하기
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = screen_width / 2 - 35# 화면 가로의 절반크기에 해당위치하도록
character_y_pos = screen_height - character_height # 화면 세로의 가장아래에 해당위치


##### 캐릭터 이동할 좌표
to_x = 0
to_y = 0


##### 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get():  # 이벤트 루프라는것은 프로그램이 종료되지 않게 대기 함으로 중간에 마우스 키보드 어떤 동작이 들어오는지 확인
        if event.type == pygame.QUIT: # 프로그램 맨위에에서 X버튼을 누른다면 파이게임창이 꺼질때 이 이벤트가 발생된다.
            running = False           # 러닝이 Flase로 바뀌어서 게임 종료


        if event.type == pygame.KEYDOWN: # 키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 1 # to_x = to_x - 3
            elif event.key == pygame.K_RIGHT:
                to_x += 1  # to_x = to_x - 3
            elif event.key == pygame.K_UP:
                to_y -= 1  # to_x = to_x - 3
            elif event.key == pygame.K_DOWN:
                to_y += 1  # to_x = to_x - 3


        if event.type == pygame.KEYUP:
            # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y


    ##### 가로 화면 밖으로 벗어나는 캐릭터를 밖으로 못나가게.
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ##### 세로 화면 밖으로 벗어나는 캐릭터를 밖으로 못나가게.
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #screen.blit(background, (0.0)) # 배경이미지 불러오기 게임창왼쪽맨위가 0,0 이기때문에 알아서 들어감
    screen.fill((0,0,255)) # RGB 로 배경 채워주기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()        # 게임화면 다시 그리기

##### runninf Flase 가되면 게임종료 처리
pygame.quit()
