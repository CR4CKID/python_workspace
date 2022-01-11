import pygame 
import os


###################################################################################
# 기본 과정
pygame.init() # 초기화 작업 (pygame 임포트 시 반드시 필요)

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("CRACKID Pang")

# FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

stage2 = pygame.image.load(os.path.join(image_path, "stage2.png"))

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width, character_height = character_size[0], character_size[1]
character_xpos = (screen_width / 2) - (character_width / 2)
character_ypos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
chracter_to_x = 0

# 캐릭터 이동 속도
chracter_speed = 1

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                chracter_to_x -= chracter_speed
            elif event.key == pygame.K_d:
                chracter_to_x += chracter_speed
            elif event.key == pygame.K_SPACE:
                weapon_xpos = character_xpos + (character_width / 2) -(weapon_width / 2)
                weapon_ypos = character_ypos
                weapons.append([weapon_xpos, weapon_ypos])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                chracter_to_x = 0
            
        
    

    # 3. 게임 캐릭터 위치 정의
    character_xpos += chracter_to_x * dt
    if character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width
    elif character_xpos < 0:
        character_xpos = 0

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 4. 충돌 처리
    
    # 5. 화면에 그리기 
    screen.blit(background, (0,0))
    for weapon_xpos, weapon_ypos in weapons: # 순서대로 화면에 그려짐
        screen.blit(weapon, (weapon_xpos, weapon_ypos))
    screen.blit(stage2, (0, character_ypos))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_xpos, character_ypos))
    
    pygame.display.update()
# pygame 종료
pygame.quit()
