import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


from PIL.Image import open
#import grafkom1Framework as graphics
import random

import numpy


def IdentityMat44(): return numpy.matrix(numpy.identity(4), copy=False, dtype='float32')


view_mat = IdentityMat44()
#
# rands = [[1]]
# for a in range(0, 2):
#     for b in range(0, 1200000):
#         rands[a].append(random.randint(0, 32767))

#one_rand = [random.randint(0, 32767) for i in range(5000000)]
#rands = [[random.randint(0, 32767) for i in range(3)] for j in range(5000000)]
#tree_height_rands = [random.randint(2, 3) for i in range(500)]

verticies = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)


]

edges = [
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
]

verticies2 = [
    (2, -2, -2),
    (2, 2, -2),
    (-2, 2, -2),
    (-2, -2, -2),
    (2, -2, 2),
    (2, 2, 2),
    (-2, -2, 2),
    (-2, 2, 2)
]

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

def setup_texture(imageID):
    """Render-time texture environment setup"""
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glBindTexture(GL_TEXTURE_2D, imageID)

def draw_sword():
    sword_texture_id = load_texture("chrome.jpeg")
    setup_texture(sword_texture_id)
    glBegin(GL_QUADS)
    glColor3f(0.13, 0.37, 0.31)

    # bottom of sword
    glTexCoord2f(0.0, 0.0);
    glVertex3f(0, 0, .1); #A
    glTexCoord2f(1.0, 0.0);
    glVertex3f(0, -.2, 0); #B
    glTexCoord2f(1.0, 1.0);
    glVertex3f(3.8, -.2, 0);#C
    glTexCoord2f(0.0, 1.0);
    glVertex3f(4, 0, 0.1);#D
    glTexCoord2f(0.0, 0);

    # top of sword
    glTexCoord2f(0.0, 0);
    glVertex3f(4, 0, 0.1);#D
    glTexCoord2f(1, 0);
    glVertex3f(3.8, 0.2, 0); #E
    glTexCoord2f(1.0, 1);
    glVertex3f(0, 0.2, 0); #F
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
def draw_cube():
    glBegin(GL_QUADS);

    glColor3f(0.13, 0.37, 0.31)
    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0, -1.0, 1.0);


    glTexCoord2f(1.0, 0.0);
    glVertex3f(1.0, -1.0, 1.0);

    glTexCoord2f(1.0, 1.0);
    glVertex3f(1.0, 1.0, 1.0);

    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, 1.0);

    #****
    glTexCoord2f(0.0, 0);
    glVertex3f(-1.0, 1.0, 1.0);
    glTexCoord2f(1.0, 0);
    glVertex3f(-1.0, 1.0, -1.0);
    glTexCoord2f(1.0, 1);
    glVertex3f(-1.0, -1.0, -1.0);
    glTexCoord2f(0, 1);
    glVertex3f(-1.0, -1.0, 1.0);

    glEnd()
    #
    # # #****
    # glTexCoord2f(0.0, 0);
    # glVertex3f(-1.0, 1.0, 1.0);
    # glTexCoord2f(1.0, 0);
    # glVertex3f(-1.0, 1.0, -1.0);
    # glTexCoord2f(1.0, 1);
    # glVertex3f(-1.0, -1.0, -1.0);
    # glTexCoord2f(0, 1);
    # glVertex3f(-1.0, -1.0, 1.0);

    #********

    #
    # glTexCoord2f(0.0, 0.0);
    # glVertex3f(-1.0, -1.0, -1.0);
    #
    #
    # glTexCoord2f(1.0, 0.0);
    # glVertex3f(1.0, -1.0, -1.0);
    #
    # glTexCoord2f(1.0, 1.0);
    # glVertex3f(1.0, 1.0, -1.0);
    #
    # glTexCoord2f(0.0, 1.0);
    # glVertex3f(-1.0, 1.0, -1.0);
    glEnd()

def draw_tunnel():
    #glPushMatrix();
    texture_id = load_texture("brick_gray.jpeg")
    setup_texture(texture_id)
    #glColor4f(.23, .78, .32, 0.0);
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


    # Right Side
    glTexCoord2f(0.0, 0.0);
    glVertex3f(1,0,0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(1, 0, -1);

    glTexCoord2f(1.0, 1.0);
    glVertex3f(1, 1, -1);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(1, 1, 0);


    # Left side

    glTexCoord2f(0.0, 0.0);
    glVertex3f(0,0,0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(0, 1, 0);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(0, 1, -1);
    glTexCoord2f(0, 1.0);
    glVertex3f(0, 0, -1);

    # Ceiling side

    glTexCoord2f(0.0, 0.0);
    glVertex3f(0,1,0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(0, 1, -1);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(1, 1, -1);
    glTexCoord2f(0, 1.0);
    glVertex3f(1, 1, 0);



    glEnd();
    #glPopMatrix();
    #ssglRotate(0, 0, 0, 0)


def load_texture(image_name):
    im = open(image_name)
    #try:
    #    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBA", 0, -1)
    #except SystemError:
    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)
    #print(str(ix) + " " +  str(iy))
    ID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, ID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(
        GL_TEXTURE_2D, 0, 3, ix, iy, 0,
        GL_RGBA, GL_UNSIGNED_BYTE, image
    )
    return ID

def make_tunnel():
    glTranslate(-.5, -.5, 0)
    for tunnel_sections in range(0, 14):
        draw_tunnel()
        glTranslate(0, 0, 1)


def make_ground():
    GLUquadric = gluNewQuadric()

    glColor3f(0.13, 0.37, 0.31)
    glPushMatrix()
    glRotatef(0.0, 0.00, 0.0, 1.0)
    glRectf(-200, 200, 200, -200);
    # gluCylinder(GLUquadric, base, base - (0.2 * base), height, 20, 20);
    glPopMatrix()
    glutSwapBuffers()


def make_cylinder(height, base):
    GLUquadric = gluNewQuadric()

    glColor3f(0.36, 0.25, 0.20)
    glPushMatrix()
    glRotatef(-90.0, 1.00, 0.0, 0.0)
    gluCylinder(GLUquadric, base, base - (0.2 * base), height, 20, 20);
    glPopMatrix()
    glutSwapBuffers()


def get_tree_rands():
    tree_rands = []
    for a in range(0, 3):
        tree_rands.append(random.randint(0, 32767))
    return


rand_index = 0


def make_tree(height, base, ORI):
    angle = None
    make_cylinder(height, base)
    glTranslatef(0.0, height, 0.0)
    height -= height * 0.2
    base -= base * 0.3

    # ramas = random.randint(0, 32767) % 3 + 3
    # ramas = rands.pop().pop() % 3 + 3
    ramas = one_rand[ORI] % 3 + 3
    ORI = ORI + 1

    for a in range(0, ramas):
        # print str(len(rands))

        # angle = rands.pop().pop() % 50 + 20
        angle = one_rand[ORI] % 50 + 20
        ORI = ORI + 1
        # random.randint(0,32767) % 50 + 20
        if (angle > 48):
            # angle = -(rands.pop().pop() % 50 + 20)
            angle = -(one_rand[ORI] % 50 + 20)
            ORI = ORI + 1
        if (height > 1):
            glPushMatrix();
            randy = one_rand[ORI] % 4
            ORI = ORI + 1
            # rands.pop().pop() % 4
            if (randy % 2 == 0):
                glRotatef(angle, 1, randy, 1)

            else:
                glRotatef(angle, 1, (-randy), 1)

            make_tree(height, base, ORI)
            glPopMatrix();

    glColor3f(0.0, 1.0 / (one_rand[ORI] % 3 + 1), 0.0)
    glutSolidSphere(0.2, 10, 10)


def multiply_vertices(cube_vertices, factor):
    new_cube_vertices = []
    for (a, b, c) in cube_vertices:
        a, b, c = a * factor, b * factor, c * factor
        new_cube_vertices.append((a, b, c))

    return new_cube_vertices

import OpenGL.GL as ogl
def draw_text( textString):
    font = pygame.font.Font (None, 64)
    textSurface = font.render(textString, True, (255,255,255,255), (0,0,0,255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glRasterPos3d(1, 1, 1)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Cube2():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies2[vertex])
    glEnd()


def cuber(vertices):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def main():
    # verticies = (
    #     (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1),
    #     (-1, 1, 1))
    pygame.init()
    display = (1200, 1200)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    playerx = 0
    playery = 0
    playerz = 0
    flying = False
    player_rot_x = 0
    player_rot_y = 0
    player_rot_z = 0
    # glMatrixMode(GL_PROJECTION)
    # gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #
    # glTranslatef(0.0,-10, -40)
    #
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()
    # glTranslatef(0, 0, -5)
    # glGetFloatv(GL_MODELVIEW_MATRIX, view_mat)
    # glLoadIdentity()
    # speed=0
    ORI = 0
    tx = 0
    ty = 0
    tz = 0
    ry = 0
    rz = 0
    #teddy = ObjLoader("creature.OBJ")

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), .1, 300.0)
    # gluPerspective(45.0f,(GLfloat)width/(GLfloat)height,0.1f,100.0f);
    view_mat = IdentityMat44()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #glTranslatef(0, 0, -20)
    glGetFloatv(GL_MODELVIEW_MATRIX, view_mat)
    glLoadIdentity()

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable( GL_BLEND );
    #
    # make_ground()
    # make_tree(5, .2, ORI)

    # glTranslatef(0.0, -10, -40)
    # make_tree(7, .6)
    b = 0
    while True:
        b = b + 1
        glLoadIdentity()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # wheel rolled up
                glScaled(1.05, 1.05, 1.05)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # wheel rolled down
                glScaled(0.95, 0.95, 0.95)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_TAB:
                    flying = False if flying else True
                if event.key == pygame.K_a:
                    tx = 1
                    glTranslate(tx, 0, 0)
                elif event.key == pygame.K_d:
                    tx = -1
                    glTranslate(tx, 0, 0)
                elif event.key == pygame.K_e:
                    ty = 1
                    glTranslate(0, ty, 0)
                elif event.key == pygame.K_q:
                    ty = -1
                    glTranslate(0, ty, 0)

                elif event.key == pygame.K_w:
                    tz = 1
                    glTranslate(0, 0, tz)
                elif event.key == pygame.K_s:
                    tz = -1
                    glTranslate(0, 0, tz)
                elif event.key == pygame.K_RIGHT:
                    ry = 1.0
                    glRotatef(ry * 2, 0, 1, 0)
                elif event.key == pygame.K_LEFT:
                    ry = -1.0
                    glRotatef(ry * 2, 0, 1, 0)
                elif event.key == pygame.K_UP:
                    rz = 1.0
                    glRotatef(ry * 2, 0, 0, 1)
                elif event.key == pygame.K_DOWN:
                    rz = -1.0
                    glRotatef(ry * 2, 0, 0, 1)
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
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         speed += 2
            #         #glTranslatef(0, 0, speed)
            #     if event.key == pygame.K_DOWN:
            #         speed -= 2
            #         #glTranslatef(0, 0, speed)

        #c
        #glLoadIdentity()
        if playerx > .05:
            print("out of bounds x")
            #glTranslate(tx + .5, ty, tz)
        if playery > .05:
            print("out of bounds y")
        if playerz > 1:
            print("out of bounds z")
                # glTranslate(tx
            effect = pygame.mixer.Sound('bullet.wav')
            effect.play()
        playerx = playerx + tx
        playery = playery + ty
        playerz = playerz + tz

        if flying:
            glTranslatef(tx, ty, tz)
            glRotatef(ry*2, 0, 1, 0)
            glRotatef(rz*2, 0, 0, 1)

        glMultMatrixf(view_mat)


        glGetFloatv(GL_MODELVIEW_MATRIX, view_mat)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glRotatef(90, 0, 0, 1)
        # glRotatef(1, 3, 1, 1)
        # glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # make_tree(5, .2)
        # if b==1 else None

        # glTranslatef(0,0,speed)
        # make_tree(5, .2)
        # glColor3f(0.97, 0.97, 1.0)
        # for a in range(1,2):
        #     glPushMatrix()
        #     new_cube_verts = multiply_vertices(verticies, a)
        #     cuber(new_cube_verts)
        #     glPopMatrix()
        #make_tunnel()
        draw_sword()
        #glTranslate(2, 22, 14)

        glPushMatrix()
        #draw_text()
        #print(str(glGetFloatv(GL_MODELVIEW_MATRIX, view_mat)))
        #make_tunnel()
        from pygame import mixer

        # pygame.init()

        # make_ground()
        # glTranslatef(10, ty, tz)
        #3 glPopMatrix()
        # for tree_loop in range(0, 50):
        #     #glPushMatrix()
        #     make_tree(tree_height_rands[tree_loop], .8, ORI)
        #     glTranslatef(tx, 6, tz)
        # for tree_loop in range(0, 4):
        #     # glPushMatrix()
        #     make_tree(tree_height_rands[tree_loop], .7, ORI)
        #     glTranslatef(tx, 6, tz)

        # glPopMatrix()
        #glTranslate(0, 0, 0)
        # make_tree(2, .6, ORI)
        #
        # glTranslatef(tx, 4, tz)
        # make_tree(2, .3, ORI)
        # glTranslatef(tx, 4, tz)
        # make_tree(2, .6, ORI)
        # glTranslatef(50, ty, tz)
        # make_tree(3, .3,ORI)
        # glTranslatef(3, ty, tz)
        # make_tree(2, .6, ORI)
        #
        #
        # glTranslatef(tx, 4, tz)
        # make_tree(2, .3, ORI)
        # glTranslatef(3, ty, tz)
        # make_tree(3, .6, ORI)
        # glTranslatef(10, ty, tz)
        # make_tree(1, .3,ORI)
        # glTranslatef(10, ty, tz)
        # make_tree(1, .8, ORI)
        # make_tree(1, .3, ORI)
        # glTranslatef(tx, ty, 4)
        # make_tree(2, .6, ORI)
        #
        # glTranslatef(tx, 4, tz)
        # make_tree(2, .3, ORI)
        # glTranslatef(tx, 4, tz)
        # make_tree(2, .6, ORI)
        # glTranslatef(10, ty, tz)
        # make_tree(3, .3, ORI)
        # glTranslatef(10, ty, tz)
        # make_tree(2, .6, ORI)
        #
        # glTranslatef(tx, 4, tz)
        # make_tree(2, .3, ORI)
        # glTranslatef(tx, 4, tz)
        # make_tree(3, .6, ORI)
        # glTranslatef(10, ty, tz)
        # make_tree(1, .3, ORI)
        # glTranslatef(10, ty, tz)
        # make_tree(1, .8, ORI)
        #
        print(str(playerx))

        #   effect = pygame.mixer.Sound('bullet.wav')
        #    effect.play()
        glPopMatrix()

        pygame.display.flip()
        #glTranslatef(0, 0, 700)
        # if b==1 else None
        # glTranslatef(0.0, 0.0, speed)
        pygame.time.wait(100)
        mixer.init()
        # if tz == 1:
        #     effect = pygame.mixer.Sound('bullet.wav')
        #     effect.play()


main()