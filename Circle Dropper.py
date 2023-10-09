from cmu_graphics import *
import random

def onAppStart(app):
    app.score = 0
    app.cy = random.randint(15,185)
    app.cx = random.randint(15,485)
    app.gameover = False
    app.stepsPerSecond = 50
    app.speed = 1
    

def onStep(app):
    app.cy += int(1 * app.speed)
    if app.cy + 15 >= 350:
        app.gameover = True
        
def onMousePress(app, mouseX, mouseY):
    if not app.gameover:
        if app.cx - 15 <= mouseX <= app.cx + 15:
            app.speed += 0.2
            app.cy = random.randint(0,200)
            app.cx = random.randint(15,385) 
            app.score += 1
            

def onKeyPress(app, key):
    if key == 'r':
        app.score = 0
        app.cy = random.randint(0,200)
        app.cx = random.randint(0,400)
        app.gameover = False
        app.stepsPerSecond = 50
        app.speed = 1
            
    

def redrawAll(app):
    if not app.gameover:
        drawCircle(app.cx,app.cy,15,fill='red')
        drawRect(0,350,400,50,fill='green')
        drawLabel(f'{app.score}',200,375)
    else:
        drawRect(0,350,400,50,fill='green')
        drawLabel("Game Over press 'r' to restart",200,375)
    

runApp()