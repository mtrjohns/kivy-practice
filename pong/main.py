from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    # variable to keep track of score
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

class PongBall(Widget):
    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    
    # variable for (x, y) position of ball
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    # move function, moves the ball one step
    # equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    # create a ball ObjectProperty to hook up to the kv rule `ball: pong_ball`
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    
    # set a random x and y positon and reset the ball
    def serve_ball(self, vel = (4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel
    
    # update method to perform frames per second clock interval
    def update(self, dt):
        # move ball
        self.ball.move()
        
        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        
        # bounce off bottom or top of screen
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            # inverse ball y velocity
            self.ball.velocity_y *= -1
            
        # went off screen left or right
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    # respond to touch input
    def on_touch_move(self, touch):
        # if touch on left of the screen, player one's turn
        if touch.x < self.width/3:
            self.player1.center_y = touch.y
        # if touch on left of the screen, player two's turn
        if touch.x > self.width - self.width/3:
            self.player2.center_y = touch.y

# .kv file must match the name before App below (e.g. pong.kv)
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        # call the game object once every 60 seconds
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    PongApp().run()