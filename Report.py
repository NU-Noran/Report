from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *






def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 100)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(0.3,0.4,0, 0)

    


angle = 0
x = 0
forward = True
a=0
def arrowkey(key,x,y):
    global a
    if key == GLUT_KEY_LEFT:
        a+=1
    elif key == GLUT_KEY_RIGHT:
        a-=1
    elif key ==b"a":
        sys.exit()

def draw_Road():
    glRotate(90,0,1,0)
    glBegin(GL_QUADS)
    #GRAY
    glColor3f(0.5,0.5,0.4)
    glVertex(-50,0,-5)
    glVertex(-50,0,4)  
    glVertex(100,0,4)
    glVertex(100,0,-5)
    # كبير
    glColor3f(0.6,0.6,0.5)
    glVertex(-100,0,-5)
    glVertex(-100,0,-8)
    glVertex(100,0,-8)
    glVertex(100,0,-5)

    glVertex(-100,0,4)
    glVertex(-100,0,5)
    glVertex(100,0,5)
    glVertex(100,0,4)
    # صغير
    glColor3f(0.4,0.4,0.3)
    glVertex(-100,0,-5)
    glVertex(-100,0,-5.5)
    glVertex(100,0,-5.5)
    glVertex(100,0,-5)

    glVertex(-100,0,4)
    glVertex(-100,0,4.2)
    glVertex(100,0,4.2)
    glVertex(100,0,4)
    
#WHITE
    glColor3f(1,1,1)
    glVertex(-18,0,0.5)
    glVertex(-18,0,1)
    glVertex(-15,0,1)
    glVertex(-15,0,0.5)
    
    glVertex(-8,0,0.5)
    glVertex(-8,0,1)
    glVertex(-5,0,1)
    glVertex(-5,0,0.5)
    
    glVertex(-1,0,0.5)
    glVertex(-1,0,1)
    glVertex(2,0,1)
    glVertex(2,0,0.5)

    glVertex(5,0,0.5)
    glVertex(5,0,1)
    glVertex(9,0,1)
    glVertex(9,0,0.5)

    glVertex(12,0,0.5)
    glVertex(12,0,1)
    glVertex(17,0,1)
    glVertex(17,0,0.5)

    glVertex(20,0,0.5)
    glVertex(20,0,1)
    glVertex(26,0,1)
    glVertex(26,0,0.5)

    glVertex(28,0,0.5)
    glVertex(28,0,1)
    glVertex(33,0,1)
    glVertex(33,0,0.5)    
    glEnd()
    glLineWidth(3)

    glBegin(GL_LINES)
    glColor3f(0.3,0.3,0.2)
    for i in range (-40,100,4):
        glVertex(i,0,-5.5)
        glVertex(i,0,-8)
        glVertex(i,0,4.20)
        glVertex(i,0,5)
        i+=3
    glEnd()
def draw_TREE():
    for i in range(-30,100,10):
            glLoadIdentity()
            glRotate(90,0,1,0)
            glTranslate(-i,0,-15)
            glScale(1,8,1)
            glColor3f(0.5,0.2,0)
            glutSolidCube( 0.5 )
    
            glLoadIdentity()
            glRotate(90,0,1,0)
            glTranslate(-i,3,-15)
            glRotate(-90,1,0,0)
            glColor3f(0.5,0.7,0.2)
            glScale(1.5,1.5,1.5)
            glutWireSphere(1.5 , 15 , 15)
angle=0
x=0
forward=True

def display():
    global angle
    global x
    global forward
    global a
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    draw_Road()
    draw_TREE()
    glRotate(90,0,1,0)
    #TORUS 
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(2.5+x,-2.5*0.25,-0.5*2.5+a)
    glRotate(-angle,0,0,1)
    glColor3f(0,0,0)
    glutSolidTorus( 0.2,0.5 , 12 , 8 )

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-2.5+x,-2.5*0.25,-0.5*2.5+a)
    glRotate(-angle,0,0,1)
    glColor3f(0,0,0)
    glutSolidTorus( 0.2,0.5 , 12 , 8 )   
#CUBE
    glLoadIdentity()
    glRotate(90,0,1,0)
    glColor3f(0.4,0,0.1) 
    glTranslate(x,0,a)
    glScale( 1,0.25 ,0.5 )
    glutSolidCube(5)    
    
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(x,5*0.25,a)
    glScale( .5,0.25 ,.5) 
    glutSolidCube(5)
#TORUS
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(x+2.5,-2.5*0.25,a+0.5*2.5)
    glRotate(-angle,0,0,1)
    glColor3f(0,0,0)
    glutSolidTorus( 0.2,0.5 , 12 , 8 )
    
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-2.5+x,-2.5*0.25,a+0.5*2.5)
    glRotate(-angle,0,0,1)
    glColor3f(0,0,0)
    glutSolidTorus( 0.2,0.5 , 12 , 8 )

    #Sphere بتتحرك بالعكس
    glLoadIdentity()
    glColor3f(1, 0.55, 0)
    glRotate(90,0,1,0)
    glTranslate(-(x), 5*0.25, -(a-5))
    glutSolidSphere(.8 , 10 , 10)
    if forward:
         angle -= 0.1
         x += .002
         if x>5:
             forward = False
        
    else:
         angle += 0.1
         x -= .002
         if x<-10:
             forward = True
      
    glutSwapBuffers()        

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Report")
myInit()
glutDisplayFunc(display)
glutIdleFunc(display)
glutSpecialFunc(arrowkey)
glutMainLoop()

        
