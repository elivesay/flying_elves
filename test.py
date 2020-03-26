import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from PIL.Image import open
from OpenGL.GLUT import *
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

def draw_sword():
    main_viewport = glViewport(0, 0, 1200, 1100);

    # glPushMatrix()

    glMatrixMode(GL_MODELVIEW);
    sword_texture_id = load_texture("chrome.jpeg")
    setup_texture(sword_texture_id)
    glLoadIdentity()
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


def draw_hud( enabled=True):
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
       glVertex3f(-1, -1, -10);
       glVertex3f(1, -1, -10);
       glVertex3f(1, 1, -10);
       glVertex3f(-1, 1, -10);
       glEnd();
       #glMatrixMode(GL_MODELVIEW);

       #glPopMatrix()

def move(rot):

    glRotate(rot, 1, 0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # wheel rolled up
            glScaled(1.05, 1.05, 1.05)
            print('mousebutton recognized')
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
                print('a typed')
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
                elif event.key == pygame.H_DOWN:
                    hud_enabled = False if hud_enabled else True;
def main():
    pygame.init()
    display = (1200,1200)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
   
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    draw_hud()
    status_viewport = glViewport(0, 1100, 1200, 100);
    health_texture_id = load_texture("pil_text.png")
    setup_texture(health_texture_id)
    rot = 3
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
        glTranslate(0,-4,0)
        draw_hud()

        glPopMatrix()

        glViewport(0, 0, 1200, 1100);
        glMatrixMode(GL_MODELVIEW);
        #glLoadIdentity();
        #gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

        #glTranslate(0,0, 0)
        glRotatef(rot, 1, 1, 1)

        Cube()


        glPopMatrix()


        glPushMatrix()
        move(rot)
        draw_sword()

        glPopMatrix()
        rot = rot + 1
        glFlush()
        pygame.display.flip()
        pygame.time.wait(10)


main()