import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 5
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

class TicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.reset_game()
        self.game_state = "menu"  # "menu", "playing", "game_over"
        
    def reset_game(self):
        self.board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.current_player = 1  # 1 for X, 2 for O
        self.winner = 0
        self.game_over = False
        
    def draw_menu(self):
        self.screen.fill(WHITE)
        
        # Title
        title_text = self.font.render("TIC TAC TOE", True, BLACK)
        title_rect = title_text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 - 100))
        self.screen.blit(title_text, title_rect)
        
        # Play button
        play_button = pygame.Rect(WINDOW_SIZE//2 - 100, WINDOW_SIZE//2, 200, 60)
        pygame.draw.rect(self.screen, BLUE, play_button)
        pygame.draw.rect(self.screen, BLACK, play_button, 3)
        
        play_text = self.small_font.render("PLAY", True, WHITE)
        play_text_rect = play_text.get_rect(center=play_button.center)
        self.screen.blit(play_text, play_text_rect)
        
        # Instructions
        inst_text = self.small_font.render("Click PLAY to start a 2-player game", True, GRAY)
        inst_rect = inst_text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 + 100))
        self.screen.blit(inst_text, inst_rect)
        
        return play_button
        
    def draw_grid(self):
        # Draw vertical lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, 
                           (i * CELL_SIZE, 0), 
                           (i * CELL_SIZE, WINDOW_SIZE), 
                           LINE_WIDTH)
        
        # Draw horizontal lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, 
                           (0, i * CELL_SIZE), 
                           (WINDOW_SIZE, i * CELL_SIZE), 
                           LINE_WIDTH)
    
    def draw_symbols(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == 1:  # X
                    self.draw_cross(col, row)
                elif self.board[row][col] == 2:  # O
                    self.draw_circle(col, row)
    
    def draw_cross(self, col, row):
        # Calculate center position
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        
        # Draw X
        pygame.draw.line(self.screen, RED, 
                        (center_x - SPACE, center_y - SPACE),
                        (center_x + SPACE, center_y + SPACE), 
                        CROSS_WIDTH)
        pygame.draw.line(self.screen, RED, 
                        (center_x + SPACE, center_y - SPACE),
                        (center_x - SPACE, center_y + SPACE), 
                        CROSS_WIDTH)
    
    def draw_circle(self, col, row):
        # Calculate center position
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        
        # Draw O
        pygame.draw.circle(self.screen, BLUE, 
                          (center_x, center_y), 
                          CIRCLE_RADIUS, 
                          CIRCLE_WIDTH)
    
    def check_winner(self):
        # Check rows
        for row in range(GRID_SIZE):
            if (self.board[row][0] == self.board[row][1] == self.board[row][2] != 0):
                return self.board[row][0]
        
        # Check columns
        for col in range(GRID_SIZE):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] != 0):
                return self.board[0][col]
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != 0):
            return self.board[0][0]
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] != 0):
            return self.board[0][2]
        
        return 0
    
    def is_board_full(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == 0:
                    return False
        return True
    
    def handle_click(self, pos):
        if self.game_state == "playing" and not self.game_over:
            col = pos[0] // CELL_SIZE
            row = pos[1] // CELL_SIZE
            
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                if self.board[row][col] == 0:
                    self.board[row][col] = self.current_player
                    
                    # Check for winner
                    self.winner = self.check_winner()
                    if self.winner != 0:
                        self.game_over = True
                        self.game_state = "game_over"
                    elif self.is_board_full():
                        self.game_over = True
                        self.game_state = "game_over"
                    else:
                        # Switch player
                        self.current_player = 2 if self.current_player == 1 else 1
    
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        if self.winner != 0:
            winner_text = "X WINS!" if self.winner == 1 else "O WINS!"
            color = RED if self.winner == 1 else BLUE
        else:
            winner_text = "IT'S A TIE!"
            color = GRAY
        
        text = self.font.render(winner_text, True, color)
        text_rect = text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 - 50))
        self.screen.blit(text, text_rect)
        
        # Play again button
        play_again_button = pygame.Rect(WINDOW_SIZE//2 - 100, WINDOW_SIZE//2 + 20, 200, 60)
        pygame.draw.rect(self.screen, GREEN, play_again_button)
        pygame.draw.rect(self.screen, BLACK, play_again_button, 3)
        
        play_again_text = self.small_font.render("PLAY AGAIN", True, WHITE)
        play_again_rect = play_again_text.get_rect(center=play_again_button.center)
        self.screen.blit(play_again_text, play_again_rect)
        
        return play_again_button
    
    def draw_current_player(self):
        if not self.game_over:
            player_text = f"Player {'X' if self.current_player == 1 else 'O'}'s Turn"
            color = RED if self.current_player == 1 else BLUE
            text = self.small_font.render(player_text, True, color)
            # Position text at the bottom of the screen
            self.screen.blit(text, (10, WINDOW_SIZE - 30))
    
    def run(self):
        running = True
        play_button = None
        play_again_button = None
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        
                        if self.game_state == "menu":
                            if play_button and play_button.collidepoint(mouse_pos):
                                self.game_state = "playing"
                                self.reset_game()
                        
                        elif self.game_state == "playing":
                            self.handle_click(mouse_pos)
                        
                        elif self.game_state == "game_over":
                            if play_again_button and play_again_button.collidepoint(mouse_pos):
                                self.game_state = "playing"
                                self.reset_game()
            
            # Draw based on game state
            if self.game_state == "menu":
                play_button = self.draw_menu()
            
            elif self.game_state == "playing":
                self.screen.fill(WHITE)
                self.draw_grid()
                self.draw_symbols()
                self.draw_current_player()
                
                if self.game_over:
                    self.game_state = "game_over"
            
            elif self.game_state == "game_over":
                self.screen.fill(WHITE)
                self.draw_grid()
                self.draw_symbols()
                play_again_button = self.draw_game_over()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Create and run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()