import pygame
import array as ar
from objfileloader import *
from pygame.locals import *
from pygame import mixer
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL.Image import open
from OpenGL.GLUT import *
tx = 0
ty = 0
tz = 0

class GameObject:

    # Initializer / Instance Attributes
    def __init__(self,
                 name='default_object',
                 type='inanimate_object',
                 location=(0, 0, 0),
                 rotation=(0, 0, 0, 0)):
        self.name = name
        self.type = type
        self.location = location
        self.rotation = rotation
        self.health = 10


class Sword(GameObject):
    def __init__(self,
                 name='default_object',
                 type='inanimate_object',
                 location=(0, 0, 0),
                 rotation=(0, 0, 0, 0)
                 ):
        super(Sword, self).__init__(name, type, location, rotation)
        self.total_rotation = 1
        self.swinging = False


class Player(GameObject):
    def __init__(self,
                 name='elf_boy',
                 type='player',
                 location=(0, 0, 0),
                 rotation=(0, 0, 0, 0)
                 ):
        super(Player, self).__init__(name, type, location, rotation)
        self.flying = False
        self.movement_direction = -1

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

from particle import Particle
from random import uniform
from OpenGL.GL import *


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def load_texture(image_name):
    im = open(image_name)
    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)
    ID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, ID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(
        GL_TEXTURE_2D, 0, 3, ix, iy, 0,
        GL_RGBA, GL_UNSIGNED_BYTE, image
    )
    return ID


def setup_texture(imageID):
    """Render-time texture environment setup"""
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glBindTexture(GL_TEXTURE_2D, imageID)


def draw_tunnel(sword, rotate = False):

    tunnel_left_boundary = -2

    glScalef(2, 2, 2)
    texture_id = load_texture("brick_gray.jpeg")
    setup_texture(texture_id)
    #glColor4f(.23, .78, .32, 0.0);

    glTranslate(-2,-.5,0)

    x, y, z = sword.location
    if x > tunnel_left_boundary:
        glTranslate(-x, -y, -z)

    for tunnel_sections in range(0,45):

        glPushMatrix();
        glBegin(GL_QUADS);

        # Floor
        glTexCoord2f(0.0, 0.0);
        glVertex3f(0,0,0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(1, 0, 0);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(1, 0, -1);
        glTexCoord2f(0, 1.0);
        glVertex3f(0, 0, -1);


        #
        # # Right Side
        glTexCoord2f(0.0, 0.0);
        glVertex3f(1,0,0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(1, 0, -1);

        glTexCoord2f(1.0, 1.0);
        glVertex3f(1, 1, -1);
        glTexCoord2f(0.0, 1.0);
        glVertex3f(1, 1, 0);


        # # Left side
        #
        glTexCoord2f(0.0, 0.0);
        glVertex3f(0,0,0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(0, 1, 0);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(0, 1, -1);
        glTexCoord2f(0, 1.0);
        glVertex3f(0, 0, -1);
        #
        # # Ceiling side
        #
        glTexCoord2f(0.0, 0.0);
        glVertex3f(0,1,0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(0, 1, -1);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(1, 1, -1);
        glTexCoord2f(0, 1.0);
        glVertex3f(1, 1, 0);

        #

        glEnd();
        glPopMatrix();

        glTranslate(0, 0, .01*tunnel_sections)
        print(str(rotate))

        #ssglRotate(0, 0, 0, 0)


def make_cylinder(height, base):
    GLUquadric = gluNewQuadric()

    glColor3f(0.36, 0.25, 0.20)
    glPushMatrix()
    glRotatef(-90.0, 0.00, 1.0, 1.0)
    gluCylinder(GLUquadric, base, base - (0.2 * base), height, 20, 20);
    glPopMatrix()
    #glutSwapBuffers()


def make_tree(height, base):
    angle = None
    glTranslate(-2, .5, 5)
    make_cylinder(height, base)
    glTranslatef(0.0, height-.5, 0.0)
    height -= height * 0.2
    base -= base * 0.3
    #
    # # ramas = random.randint(0, 32767) % 3 + 3
    # # ramas = rands.pop().pop() % 3 + 3
    # ramas = one_rand[ORI] % 3 + 3
    # ORI = ORI + 1
    #
    # for a in range(0, ramas):
    #     # print str(len(rands))
    #
    #     # angle = rands.pop().pop() % 50 + 20
    #     angle = one_rand[ORI] % 50 + 20
    #     ORI = ORI + 1
    #     # random.randint(0,32767) % 50 + 20
    #     if (angle > 48):
    #         # angle = -(rands.pop().pop() % 50 + 20)
    #         angle = -(one_rand[ORI] % 50 + 20)
    #         ORI = ORI + 1
    #     if (height > 1):
    #         glPushMatrix();
    #         randy = one_rand[ORI] % 4
    #         ORI = ORI + 1
    #         # rands.pop().pop() % 4
    #         if (randy % 2 == 0):
    #             glRotatef(angle, 1, randy, 1)
    #
    #         else:
    #             glRotatef(angle, 1, (-randy), 1)
    #
    #         make_tree(height, base, ORI)
    #         glPopMatrix();
    #
    # glColor3f(0.0, 1.0 / (one_rand[ORI] % 3 + 1), 0.0)
    # glutSolidSphere(0.2, 10, 10)

def draw_sword(sword):
    main_viewport = glViewport(0, 0, 1200, 1100);

    # glPushMatrix()

    glMatrixMode(GL_MODELVIEW);
    sword_texture_id = load_texture("chrome.jpeg")
    setup_texture(sword_texture_id)
    #glLoadIdentity()
    glTranslate(-3, 0, 0)
    x, y, z = sword.location
    if not sword.swinging:
        glRotate(90, 1, 1, 1)
    #print(str(x), str(y), str(z))
    #glTranslate(z, y, x)
    if sword.swinging and sword.total_rotation<50:
        glRotate((sword.total_rotation+( (sword.total_rotation+48)*3)), 1, 0, 1)
        sword.total_rotation = sword.total_rotation + 1
        if sword.total_rotation>48:
            sword.swinging=False
            sword.total_rotation=1

    glBegin(GL_QUADS)
    # glColor3f(0.13, 0.37, 0.31)

    # bottom of sword
    glTexCoord2f(0.0, 0.0);
    glVertex3f(0, 0, .1);  # A
    glTexCoord2f(1.0, 0.0);
    glVertex3f(0, -.2, 0);  # B
    glTexCoord2f(1.0, 1.0);
    glVertex3f(3.8, -.2, 0);  # C
    glTexCoord2f(0.0, 1.0);
    glVertex3f(4, 0, 0.1);  # D
    glTexCoord2f(0.0, 0);

    # top of sword
    glTexCoord2f(0.0, 0);
    glVertex3f(4, 0, 0.1);  # D
    glTexCoord2f(1, 0);
    glVertex3f(3.8, 0.2, 0);  # E
    glTexCoord2f(1.0, 1);
    glVertex3f(0, 0.2, 0);  # F
    glTexCoord2f(0.0, 1.0);
    glVertex3f(0, 0, .1);  # A
    glEnd()
    # sword hilt

    sword_hilt_texture_id = load_texture("gold.jpeg")
    setup_texture(sword_hilt_texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0);
    glVertex3f(0.2, -.5, .2);  # G
    glTexCoord2f(1.0, 0);
    glVertex3f(0.2, -.5, -.2);  # H
    glTexCoord2f(1.0, 1);
    glVertex3f(-0.2, -.5, -.2);  # I
    glTexCoord2f(0, 1);
    glVertex3f(-0.2, -.5, .2);  # J

    glTexCoord2f(0.0, 0);
    glVertex3f(0.2, -.5, .2);  # G
    glTexCoord2f(1.0, 0);
    glVertex3f(0.2, -.5, -.2);  # H
    glTexCoord2f(1.0, 1);
    glVertex3f(.2, .5, -.2);  # L
    glTexCoord2f(0, 1);
    glVertex3f(.20, .5, .2);  # K

    glTexCoord2f(0.0, 0);
    glVertex3f(.20, .5, .2);  # K
    glTexCoord2f(1.0, 0);
    glVertex3f(.2, .5, -.2);  # L
    glTexCoord2f(1.0, 1);
    glVertex3f(-.2, .5, -.2);  # M
    glTexCoord2f(0, 1);
    glVertex3f(-.2, .5, .2);  # N

    glTexCoord2f(0.0, 0);
    glVertex3f(-.2, .5, -.2);  # M
    glTexCoord2f(1, 0);
    glVertex3f(-.2, .5, .2);  # N
    glTexCoord2f(1.0, 1);
    glVertex3f(-0.2, -.5, .2);  # J
    glTexCoord2f(0, 1);
    glVertex3f(-0.2, -.5, -.2);  # I

    glTexCoord2f(0, 0);
    glVertex3f(-0.2, -.5, .2);  # J
    glTexCoord2f(1.0, 0);
    glVertex3f(0.2, -.5, -.2);  # H
    glTexCoord2f(1.0, 1.0);
    glVertex3f(.2, .5, -.2);  # L
    glTexCoord2f(0, 1);
    glVertex3f(-.2, .5, -.2);  # M
    glEnd()

def open_obj():
    print("trying to open obj")
    obj = OBJFile('obj_skinny_creature.OBJ')
    obj.draw()
def draw_hud(player,  enabled=True ):
    print("in draw hud")
    # Draw Health bar:

    if enabled:
       from PIL import Image, ImageDraw

       img = Image.new('RGB', (50, 10), color=(73, 109, 137))

       d = ImageDraw.Draw(img)
       d.text((5, 0), "Health:", fill=(255, 255, 0))

       img.save('pil_text.png')


       status_viewport = glViewport(0, 1100, 1200, 100);
       health_texture_id = load_texture("pil_text.png")
       setup_texture(health_texture_id)

       #glPushMatrix()
       glBegin(GL_QUADS);

       glTexCoord2f(0.0, 0.0);
       glVertex3f(-1, -1, -10);
       glTexCoord2f(1.0, 0.0);
       glVertex3f(1, -1, -10);
       glTexCoord2f(1, 1);
       glVertex3f(1, 1, -10);
       glTexCoord2f(0.0,1.0);
       glVertex3f(-1, 1, -10);
       glEnd();

       glDisable(GL_TEXTURE_2D)
       glTranslate(3, 0, -2)

       glBegin(GL_QUADS);
       glColor3d(1, 0, 0);
       print("player health: " + str(player.health))
       glVertex3f(-.1*player.health, -1, -10);
       glVertex3f(.1*player.health, -1, -10);
       glVertex3f(.1*player.health, 1, -10);
       glVertex3f(-.1*player.health, 1, -10);
       glEnd();
       #glMatrixMode(GL_MODELVIEW);

       #glPopMatrix()


def move(rot, sword, player):
    print(str(rot))
    print("sword location: " + str(sword.location[2:3][0] ))
    #glRotate(rot, 1, 0, 0)
    tunnel_left_boundary=-.75
    tunnel_right_boundary = .75
    movement_size = .1
    print("flying: " + str(player.flying))
    if player.flying:
        z = sword.location[2] + (movement_size * player.movement_direction)
        sword.location = (sword.location[0], sword.location[1], z)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # wheel rolled up
            glScaled(1.05, 1.05, 1.05)
            print('mousebutton recognized')
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # wheel rolled down
            glScaled(1.95, 1.95,1.95)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_TAB:
                player.flying = False if player.flying else True
                print(" in move hit tab: " + str(player.flying))
            if event.key == pygame.K_a:
                x = sword.location[:1][0] - movement_size
                if x-movement_size > tunnel_left_boundary:
                    sword.location = sword.location[: 0] + (x,) + sword.location[1 + 0:]
                elif x -movement_size == tunnel_left_boundary:
                    mixer.init()
                    effect = pygame.mixer.Sound('bullet.wav')
                    effect.play()
                    player.health = player.health - 1 if player.health>0 else player.health
            elif event.key == pygame.K_d:
                x = sword.location[:1][0] + movement_size
                if x + movement_size < tunnel_right_boundary:
                    sword.location = sword.location[: 0] + (x,) + sword.location[1 + 0:]
                elif x + movement_size == tunnel_right_boundary:
                    mixer.init()
                    effect = pygame.mixer.Sound('bullet.wav')
                    effect.play()
                    player.health = player.health - 1 if player.health > 0 else player.health
            elif event.key == pygame.K_e:
                ty = 1
                glTranslate(0, ty, 0)
            elif event.key == pygame.K_q:
                ty = -1
                glTranslate(0, ty, 0)
            elif event.key == pygame.K_w:
                player.movement_direction = -1
                z = sword.location[2] - movement_size
                sword.location = (sword.location[0] , sword.location[1], z)
            elif event.key == pygame.K_s:
                player.movement_direction = 1
                z = sword.location[2] + movement_size
                sword.location = (sword.location[0], sword.location[1], z)
            elif event.key == pygame.K_RIGHT:
                ry = 1.0
                glRotatef(ry * 2, 0, 1, 0)
            elif event.key == pygame.K_LEFT:
                ry = -1.0
                glRotatef(ry * 2, 0, 1, 0)
            elif event.key == pygame.K_UP:
                sword.swinging = True
            elif event.key == pygame.K_DOWN:

            elif event.type == pygame.K_SPACE:
                tx = 0
                ty = 0
                tz = 0
                ry = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and tx > 0:
                    tx = 0
                elif event.key == pygame.K_d and tx < 0:
                    tx = 0
                elif event.key == pygame.K_w and tz > 0:
                    tz = 0
                elif event.key == pygame.K_s and tz < 0:
                    tz = 0
                elif event.key == pygame.K_RIGHT and ry > 0:
                    ry = 0.0
                elif event.key == pygame.K_LEFT and ry < 0:
                    ry = 0.0
                elif event.key == pygame.K_UP and ry > 0:
                    rz = 0.0
                elif event.key == pygame.K_DOWN and ry < 0:
                    rz = 0.0

                elif event.key == pygame.H_DOWN:
                    hud_enabled = False if hud_enabled else True;
def main():
    pygame.init()
    display = (1200,1200)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
   
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    status_viewport = glViewport(0, 1100, 1200, 100);
    health_texture_id = load_texture("pil_text.png")
    setup_texture(health_texture_id)
    rot = 3
    sword = Sword('sword')
    player = Player()
    draw_hud(player)
    movement_direction = 1
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #glViewport(0, 1100, 1200, 100);

        glMatrixMode(GL_MODELVIEW);
        #glLoadIdentity();
        #gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        # gluLookAt(0, 0, 0,
        #          0, 0, 0,
        #           0,0, 0);

        glPushMatrix()
        glPushMatrix()
        glPushMatrix()
        #open_obj()
        #glTranslate(0,-4,0)
        draw_hud(player)

        glPopMatrix()

        glViewport(0, 0, 1200, 1100);
        glMatrixMode(GL_MODELVIEW);
        #glLoadIdentity();
        #gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

        #glTranslate(0,0, 0)
        #glRotatef(rot, 1, 1, 1)

        #Cube()
        #glTranslate(-4,0,0)
        glPopMatrix()
        draw_tunnel(sword)

        glPopMatrix()


        glPushMatrix()
        print("in main loop - flying: " + str(player.flying))
        move(rot, sword, player)
        #glRotatef(rot, 1, 1, 1)
        draw_sword(sword )

        glPopMatrix()
        rot = rot + 1
        glFlush()
        pygame.display.flip()
        pygame.time.wait(10)


main()
