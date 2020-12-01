# QUIZ ) 하늘에서 떨어지는 똥 피하기 게임을 만드시오
# 1. 캐릭터는 화면 가장 아래 위치, 좌우 이동가능
# 2. 똥은 화면 가장위에서 떨어짐. X 좌표는 랜덤
# 3. 캐릭터가 똥을 피하면 다음똥이 다시떨어짐.
# 4. 캐릭턱 똥과 충돌하면게임종료
# 5. FPS 30 고정

# [ 게임이미지 ]
# 1. 배경 640 840
# 2. 캐릭터 70 70
# 3. 똥 70 70


import pygame
import random

#fream per sceond # 초당프레임 나타내는것

pygame.init()  # 초기화 반드시필요하다.

##### 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

##### 게임 화면 타이틀 설정
pygame.display.set_caption("Project1")  # 게임 이름

##### FPS

clock = pygame.time.Clock()



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
##### 캐릭터 이동 속도
character_speed = 5

##### 적 캐릭터 enemy
enemy = pygame.image.load("C:/Users/82104/Desktop/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기를 구하기
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] #캐릭터 세로크기
enemy_x_pos = random.randint(0,screen_height - enemy_width)
enemy_y_pos = 0
enemy_speed = 10


##### 폰트정의
game_font = pygame.font.Font(None,40) # 폰트 객체를 생성 ( 폰트, 크기)

##### 총 시간
total_time = 10

##### 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시간 tick을 받아옴

##### 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

##### 캐릭터가 100 만큼 이동을 해야함
##### 10 fps : 1초동안 10번동작 -> 1번에 몇 만큼이동 ? 10만큼! 10* 10 = 100
##### 20 fps : 1초동안 20번동작 -> 1번에 5만큼! 5 * 20 = 100


    #print("fts : " + str (clock.get_fps()))
    for event in pygame.event.get():  # 이벤트 루프라는것은 프로그램이 종료되지 않게 대기 함으로 중간에 마우스 키보드 어떤 동작이 들어오는지 확인
        if event.type == pygame.QUIT: # 프로그램 맨위에에서 X버튼을 누른다면 파이게임창이 꺼질때 이 이벤트가 발생된다.
            running = False           # 러닝이 Flase로 바뀌어서 게임 종료


        if event.type == pygame.KEYDOWN: # 키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed # to_x = to_x - 3
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed  # to_x = to_x - 3


        if event.type == pygame.KEYUP:
            # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 캐릭터의 위치 정의
    character_x_pos += to_x

    ##### 가로 화면 밖으로 벗어나는 캐릭터를 밖으로 못나가게.
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_height - enemy_width)

##### 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


##### 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

    #screen.blit(background, (0.0)) # 배경이미지 불러오기 게임창왼쪽맨위가 0,0 이기때문에 알아서 들어감
    screen.fill((0,0,255)) # RGB 로 배경 채워주기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적그리기

    # 타이머 집어넣기.
    # 경과 시간 시간 계산
    elapsed_time=(pygame.time.get_ticks() - start_ticks) / 1000 # ms 를 초로 환산하기위해 / 1000
    #timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255)) # ms 자르고 초단위로보기위해 int- str 으로
    #screen.blit(timer,(10,10))

    # 만약 시간이 0 이하라면 게임종료
    #if total_time - elapsed_time <= 0:
     #   print("Time out")
     #   running = False

    # 잠시 대기 2초정도
    #pygame.time.delay(2000) # 2초대기

    pygame.display.update()        # 게임화면 다시 그리기

##### runninf Flase 가되면 게임종료 처리
pygame.quit()
