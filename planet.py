import pygame
import random
import math


#all the necessary functions,classes and variables

#the variables
G = 6.6734*10**-11
Scale_factor = 217*10**-9/150

class heavenly_body():
    def __init__(self,mass,xpos,ypos,xvel,yvel,rad):
        self.mass = mass
        self.xpos= xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel 
        self.rad = rad

    def update_vel(self,vx,vy):

        self.xvel=vx
        self.yvel = vy  

    def update_pos(self,px,py):
        self.xpos = px 
        self.ypos = py 

def simulate(bodies:heavenly_body,dt):
    #takes in a list of bodies , updates their velocities and positions. that's all.

    for i in range(len(bodies)):
        one = bodies[i]
        rest = bodies[:i]+bodies[i+1:]


        ax = 0
        ay = 0
        
        


        for bodyj in rest:
            roj = math.sqrt((bodyj.xpos-one.xpos)**2+(bodyj.ypos-one.ypos)**2)/Scale_factor

            a = (G*bodyj.mass)/(roj**2)
            print("a",a)

            teta = math.atan((bodyj.ypos-one.ypos)/(bodyj.xpos-one.xpos))
            ax_dash = a*math.cos(teta)
            ay_dash = a*math.sin(teta)

            if bodyj.xpos>one.xpos:
                dirx = 1
                diry = 1
            else:
                dirx = -1
                diry = -1
            '''if bodyj.ypos>one.ypos:
                diry = 1
            else:
                diry = 1'''
            print("dir",dirx)
            ax+=dirx*ax_dash*10
            ay+=diry*ay_dash*10

        
        print("ax",ax*dt)  
        vx_dash = one.xvel +ax*dt
        vy_dash = one.yvel + ay*dt

        px_dash = one.xpos + vx_dash*dt
        py_dash  = one.ypos +vy_dash*dt

        one.update_vel(vx_dash,vy_dash)
        one.update_pos(px_dash,py_dash)

        print("velo",vx_dash*dt,vy_dash*dt)
        print("pos",px_dash*dt,py_dash*dt)




def stars_list():
    stars_coords = []
    for i in range(1000):
        x,y = random.randint(10,1200),random.randint(10,700)
        stars_coords.append((x,y))
    return stars_coords

    
        
stars_coords = stars_list()
def print_bg(stars_coords):
    screen.fill("black")
    for x,y in stars_coords:
        screen.set_at((x,y),"white")

def print_tracing(pos_coords,color):
    for x,y, in pos_coords:
        screen.set_at((x,y),color)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

sun_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
earth_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)
venus_pos = pygame.Vector2(2*screen.get_width() / 3, 2.5*screen.get_height() / 3)

#intialize the bodies
sun = heavenly_body(1.989*10**30,sun_pos.x,sun_pos.y,0,0,40)

earth = heavenly_body(5.972*10**24,earth_pos.x,earth_pos.y,1,3,10)

venus = heavenly_body(4.867*10**24,venus_pos.x,venus_pos.y,1,-2,8)

list_bodies = [sun,earth,venus]
earth_poses = []
venus_poses = []



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    print_bg(stars_coords=stars_coords)

    pygame.draw.circle(screen, "red", (sun.xpos,sun.ypos), 40)
    pygame.draw.circle(screen,"blue",(earth.xpos,earth.ypos),10)
    pygame.draw.circle(screen,"yellow",(venus.xpos,venus.ypos),8)
    venus_poses.append((int(venus.xpos),int(venus.ypos)))
    earth_poses.append((int(earth.xpos),int(earth.ypos)))
    print_tracing(venus_poses,"yellow")
    print_tracing(earth_poses,"blue")


    simulate(list_bodies,dt)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        sun.ypos -= 300 * dt
    if keys[pygame.K_s]:
        sun.ypos += 300 * dt
    if keys[pygame.K_a]:
        sun.xpos -= 300 * dt
    if keys[pygame.K_d]:
        sun.xpos += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60)/100
    print("dt",dt)

pygame.quit()
