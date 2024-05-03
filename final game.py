# -*- coding: utf-8 -*-
"""
Brendan Eye 
final game 
"""
import simpleGE, pygame


        
class Steve_player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Main Ship - Base - Full health.png")
        self.setSize(150,150)
        self.position = (400,350)
        self.move_speed = 8
        
        
        self.top_left_corner = False 
        
        self.bottom_left_corner = False 
        
        self.top_right_corner = False 
        
        self.bottom_right_corner = False 
        
     
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            if self.x > 0:
                self.x -= self.move_speed
        
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.x < self.screenWidth:    
                self.x += self.move_speed
        
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.move_speed
            if self.y > self.screenHeight:
                self.y -= self.move_speed
        
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.move_speed
            if self.y < 0:
                self.y += self.move_speed
        
   
        self.position = (self.x, self.y)
       
     
  
                        
        
class Lbl_time(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left 10"
        self.center = (500,30)
        
            

            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("preview.png")
        self.response = "quit"
    
        
    
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 15
        self.lbl_time= Lbl_time()
        
       
       
        self.steve = Steve_player(self)
        
        self.sprites = [self.steve,self.lbl_time]
        
   
    def process(self):
              
        self.lbl_time.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        
        if self.timer.getTimeLeft() < 0:
           self.response = "lose"
           self.stop()
           
        self.corner()
        self.check_all_corners()
      
    def corner (self):
        
       
        
        print("self.steve.x:", self.steve.x)
        print("self.steve.y:", self.steve.y)
        print("self.screenWidth:", self.steve.screenWidth)
        print("self.screenHeight:", self.steve.screenHeight)
        
      
      
       
        if self.steve.x <= 0:
            if self.steve.y <= 10:
                self.steve.top_left_corner = True
                print("Player is in a corner! top left")
        
        if self.steve.x >=  self.steve.screenWidth - 10:
            if self.steve.y <= self.steve.screenHeight - 10:
             self.steve.top_right_corner = True 
             print("Player is in a corner! top right")
      
        if self.steve.x <= 0:
          if self.steve.y >= 478:
                self.steve.bottom_left_corner = True
                print("Player is in a corner! bottom left")
      
        if self.steve.x >= self.steve.screenWidth - 10:
            if self.steve.y >= self.steve.screenHeight - 10:
                self.steve.bottom_right_corner = True 
                print("Player is in a corner! bottom right")
     
    
    def check_all_corners(self):
        
     
        if self.steve.top_left_corner == True:
            if self.steve.bottom_left_corner == True:
                if self.steve.top_right_corner == True:
                    if self.steve.bottom_right_corner == True: 
                        self.response = "win"
                        self.stop()

class Win_panel(simpleGE.Scene):
    def __init__(self):
            super().__init__()
            
            self.setImage("preview.png")
            self.response = "quit"
            
            
            self.win_panel =  simpleGE.MultiLabel() 
            self.win_panel.textLines = ["good job",
                                        "I hereby promote you to exectuive delivery person"]
            
            
            self.win_panel.center = (320,240)
            self.win_panel.size = (500,150)
            
            self.button_play = simpleGE.Button()
            self.button_play.text = ("play again")
            self.button_play.center = (100,400)
            
              
            self.button_quit = simpleGE.Button()
            self.button_quit.text = ("quit")
            self.button_quit.center = (540,400)
           
            
            self.sprites = [self.win_panel , self.button_play, self.button_quit]
            

    
    def process(self):
        
       
    
        if self.button_play.clicked:
            self.response = "play"
            self.stop() 
        
        if self.button_quit.clicked:
            self.response = ("quit")
            self.stop()
                        
            
class Lose_panel(simpleGE.Scene):
    def __init__(self):
            super().__init__()
            
            
            
            self.setImage("preview.png")
            self.response = "quit"
            
            
            self.lose_panel =  simpleGE.MultiLabel() 
            self.lose_panel.textLines = ["bad news nobody you lost"]
            
            
            self.lose_panel.center = (320,240)
            self.lose_panel.size = (500,250)
            
            self.button_play = simpleGE.Button()
            self.button_play.text = ("try again")
            self.button_play.center = (100,400)
            
              
            self.button_quit = simpleGE.Button()
            self.button_quit.text = ("quit")
            self.button_quit.center = (540,400)
           
            
            self.sprites = [self.lose_panel , self.button_play, self.button_quit]
            

    
    def process(self):
        
       
    
        if self.button_play.clicked:
            self.response = "play"
            self.stop() 
        
        if self.button_quit.clicked:
            self.response = ("quit")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self):
            super().__init__()
            
            
            
            self.setImage("preview.png")
            self.response = "quit"
            
            
            self.tutorial =  simpleGE.MultiLabel() 
            self.tutorial.textLines = ["good news everyone!",
                                       "I made a new planet express traing program",
                                       "you need to deliver a packge to all for corners",
                                       "if the time runs out you lose"]
            
            
            self.tutorial.center = (320,240)
            self.tutorial.size = (500,250)
            
            self.button_play = simpleGE.Button()
            self.button_play.text = ("play")
            self.button_play.center = (100,400)
            
              
            self.button_quit = simpleGE.Button()
            self.button_quit.text = ("quit")
            self.button_quit.center = (540,400)
           
            
            self.sprites = [self.tutorial, self.button_play, self.button_quit]
            

    
    def process(self):
        
       
    
        if self.button_play.clicked:
            self.response = "play"
            self.stop() 
        
        if self.button_quit.clicked:
            self.stop()
       
    
def main():
    keep_going = True
    play_game = False  
    while(keep_going):   
        
        if play_game == False:
            tutorial = Instructions()
            tutorial.start()
        
        if tutorial.response == "play":
            play_game = True 
        
        if play_game == True:
            game = Game()
            game.start()
         
        if game.response == "win":
              win_panel = Win_panel()
              win_panel.start()
             
              if win_panel.response == "quit":
                  keep_going = False
              elif win_panel.response == "play again":
                  play_game = True 
                 
        
        if game.response == "lose":
              lose_panel = Lose_panel()
              lose_panel.start()
             
              if lose_panel.response == "quit":
                  keep_going = False
              elif lose_panel.response == "try again":
                  play_game = True 
                 
   
        if tutorial.response == "quit":
         keep_going = False
        
    
if __name__ == "__main__":
    main()

