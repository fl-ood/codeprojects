from cmu_graphics import *
import random

def onAppStart(app):
    app.currguess = ''
    app.istyping = False
    app.lo = 1
    app.hi  = 100
    app.guesscount = 0
    app.message = 'Enter your next guess'
    app.showHint = False
    app.showAnswer = False
    app.gameOver = False
    app.answer = random.randrange(1, 101)
    
def newGame(app):
    app.currguess = ''
    app.istyping = False
    app.lo = 1
    app.hi  = 100
    app.guesscount = 0
    app.message = 'Enter your next guess'
    app.showHint = False
    app.showAnswer = False
    app.gameOver = False
    app.answer = random.randrange(1, 101)
def redrawAll(app):
    # Draw the instructions:
    drawLabel('Number Guessing Game', 200, 20, size=20, bold=True)
    drawLabel(f'Guess a number between 1 and 100 (inclusive)',
              200, 50)
    drawLabel('To enter a guess, type the number followed by the enter key',
              200, 70)
    drawLabel('Press n to play a new game', 200, 90)
    drawLabel('Press h to toggle displaying the hint', 200, 110)
    drawLabel('Press a to see the answer', 200, 130)
    drawLine(50, 150, 350, 150)
    # Draw the current guess and the message:
    drawLabel('Current Guess: ' + app.currguess, 200, 170,
              size=20, bold=True)
    drawLabel(app.message, 200, 200)
    drawLine(50, 220, 350, 220)
    # Draw the hint and answer (if they are visible):
    if app.showHint:
        drawLabel(f'hint: The range is now {app.lo} to {app.hi}, so try {(app.lo + app.hi) //2}.', 200, 240)
    if app.showAnswer:
        drawLabel(f'answer: {app.answer}', 200, 270)

def onKeyPress(app, key):
    if not app.gameOver:
        if key.isdigit():
            app.currguess += key
        if key == 'delete' or key == 'backspace':
            app.currguess = app.currguess[:-1]
        if app.currguess != '':
            if key == 'enter':
                handleGuess(app)
        if key =='h':
            app.showHint = not app.showHint
        if key == 'a':
            app.showAnswer = not app.showAnswer
    if key == 'n':
        newGame(app)
def handleGuess(app):
    app.guesscount += 1
    guess = int(app.currguess)
    if guess < app.lo:
        app.currguess = ''
        app.message = f'We know the number is at least {app.lo}'
    if guess > app.hi:
        app.currguess = ''
        app.message = f'We know the number is at most {app.hi}'
    if app.lo < guess < app.answer:
        app.currguess = ''
        app.message = 'Too low!'
        app.lo = guess + 1
    if app.hi > guess > app.answer:
        app.currguess = ''
        app.message = 'Too high!'
        app.hi = guess - 1
    if guess == app.answer:
        app.currguess = ''
        app.gameOver = True
        if app.gameOver:
            app.showHint = False
            app.showAnswer = False
        app.message = f'You got it in {app.guesscount} guesses!'
def main():
    runApp()

main()