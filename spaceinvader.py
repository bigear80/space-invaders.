import pgzrun,random,pyautogui

print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()

player=Actor('rocket (player)')
player.pos=WIDTH/2,HEIGHT-200
enemies=[]
def draw():
    screen.blit('space_invaders_bg.jpg',(0,0))
    player.draw()
    for i in enemies:
        i.draw()

def update():
    if keyboard.left and player.x >50:
        player.x-=10

    if keyboard.right and player.x < WIDTH-50:                                                                                                                  
        player.x+=10
    for i in enemies:
        i.y += 10

def create_enemies():
    enemy=Actor('player.png')
    enemy.pos=random.randint(50,WIDTH-50),-50
    enemies.append(enemy)


clock.schedule_interval(create_enemies,1)
pgzrun.go()