import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)  # Moving right initially
        self.grow = False
        
    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            return False
            
        # Check self collision
        if new_head in self.positions:
            return False
            
        self.positions.insert(0, new_head)
        
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False
            
        return True
        
    def change_direction(self, new_direction):
        # Prevent moving backwards into itself
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
            
    def grow_snake(self):
        self.grow = True
        
    def draw(self, screen):
        for i, pos in enumerate(self.positions):
            x, y = pos[0] * GRID_SIZE, pos[1] * GRID_SIZE
            # Head is brighter green
            color = GREEN if i == 0 else (0, 200, 0)
            pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 1)

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.color = RED
        
    def generate_position(self):
        return (random.randint(0, GRID_WIDTH - 1), 
                random.randint(0, GRID_HEIGHT - 1))
                
    def draw(self, screen):
        x, y = self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE
        pygame.draw.rect(screen, self.color, (x, y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 1)

class PowerUp:
    def __init__(self):
        self.position = self.generate_position()
        self.type = random.choice(['speed', 'double_points', 'invincible'])
        self.timer = 300  # 5 seconds at 60 FPS
        self.colors = {
            'speed': BLUE,
            'double_points': YELLOW,
            'invincible': PURPLE
        }
        
    def generate_position(self):
        return (random.randint(0, GRID_WIDTH - 1), 
                random.randint(0, GRID_HEIGHT - 1))
                
    def draw(self, screen):
        x, y = self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE
        color = self.colors[self.type]
        pygame.draw.circle(screen, color, 
                         (x + GRID_SIZE // 2, y + GRID_SIZE // 2), 
                         GRID_SIZE // 2)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Interactive Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.reset_game()
        
    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.powerups = []
        self.score = 0
        self.game_over = False
        self.paused = False
        self.speed = 10
        self.speed_boost = 0
        self.double_points = 0
        self.invincible = 0
        self.powerup_spawn_timer = 0
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset_game()
                    elif event.key == pygame.K_q:
                        return False
                else:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((1, 0))
                    elif event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                        
        return True
        
    def update(self):
        if self.game_over or self.paused:
            return
            
        # Update power-up timers
        if self.speed_boost > 0:
            self.speed_boost -= 1
        if self.double_points > 0:
            self.double_points -= 1
        if self.invincible > 0:
            self.invincible -= 1
            
        # Move snake
        if not self.snake.move() and self.invincible == 0:
            self.game_over = True
            return
            
        # Check food collision
        if self.snake.positions[0] == self.food.position:
            self.snake.grow_snake()
            points = 10 if self.double_points == 0 else 20
            self.score += points
            
            # Generate new food position (avoid snake)
            while True:
                self.food.position = self.food.generate_position()
                if self.food.position not in self.snake.positions:
                    break
                    
        # Power-up spawning
        self.powerup_spawn_timer += 1
        if self.powerup_spawn_timer > 600:  # Every 10 seconds
            if len(self.powerups) < 2 and random.random() < 0.3:
                powerup = PowerUp()
                # Ensure powerup doesn't spawn on snake or food
                while (powerup.position in self.snake.positions or 
                       powerup.position == self.food.position):
                    powerup.position = powerup.generate_position()
                self.powerups.append(powerup)
            self.powerup_spawn_timer = 0
            
        # Check power-up collisions
        for powerup in self.powerups[:]:
            if self.snake.positions[0] == powerup.position:
                if powerup.type == 'speed':
                    self.speed_boost = 300  # 5 seconds
                elif powerup.type == 'double_points':
                    self.double_points = 600  # 10 seconds
                elif powerup.type == 'invincible':
                    self.invincible = 180  # 3 seconds
                    
                self.powerups.remove(powerup)
                self.score += 5
                
        # Update power-up timers and remove expired ones
        for powerup in self.powerups[:]:
            powerup.timer -= 1
            if powerup.timer <= 0:
                self.powerups.remove(powerup)
                
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw game objects
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        for powerup in self.powerups:
            powerup.draw(self.screen)
            
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw active power-ups
        y_offset = 50
        if self.speed_boost > 0:
            speed_text = self.small_font.render(f"Speed Boost: {self.speed_boost // 60 + 1}s", True, BLUE)
            self.screen.blit(speed_text, (10, y_offset))
            y_offset += 25
            
        if self.double_points > 0:
            double_text = self.small_font.render(f"Double Points: {self.double_points // 60 + 1}s", True, YELLOW)
            self.screen.blit(double_text, (10, y_offset))
            y_offset += 25
            
        if self.invincible > 0:
            invincible_text = self.small_font.render(f"Invincible: {self.invincible // 60 + 1}s", True, PURPLE)
            self.screen.blit(invincible_text, (10, y_offset))
            
        # Draw instructions
        if not self.game_over:
            instruction_text = self.small_font.render("SPACE: Pause | Arrow Keys: Move", True, WHITE)
            self.screen.blit(instruction_text, (10, WINDOW_HEIGHT - 30))
            
        # Draw pause screen
        if self.paused:
            pause_text = self.font.render("PAUSED - Press SPACE to continue", True, WHITE)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(pause_text, text_rect)
            
        # Draw game over screen
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, RED)
            score_final = self.font.render(f"Final Score: {self.score}", True, WHITE)
            restart_text = self.small_font.render("Press R to restart or Q to quit", True, WHITE)
            
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            score_rect = score_final.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
            
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(score_final, score_rect)
            self.screen.blit(restart_text, restart_rect)
            
        pygame.display.flip()
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            
            # Adjust speed based on power-ups
            current_speed = self.speed + (5 if self.speed_boost > 0 else 0)
            self.clock.tick(current_speed)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

