import pygame

pygame.init()
WINDOW_WIDTH = 720
PIXEL_WIDTH =  WINDOW_WIDTH // 3
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True



# Function that reads in the icons and the grid, before plotting them onto the screen.

def load_icons(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

ICON_X = load_icons('icons/x.png', [PIXEL_WIDTH, PIXEL_WIDTH])
ICON_O = load_icons('icons/o.png', [PIXEL_WIDTH, PIXEL_WIDTH])
GRID = load_icons('icons/grid.png', [WINDOW_WIDTH, WINDOW_WIDTH])
PLAYER_1 = 0
PLAYER_2 = 1
  #player 0 is the first player, then player 1 is the other.

player = PLAYER_1

def play_turn(current_player):
    curr_coordinate = pygame.math.Vector2(pygame.mouse.get_pos())
    normalized_coordinate = curr_coordinate // PIXEL_WIDTH
    #Index 0 checks the left click (1 is middle, 2 is right click)
    if pygame.mouse.get_pressed()[0]:
        col, row = map(int, normalized_coordinate)
        board[row][col] = current_player
        global player
        player = 1 - player

def draw_icons():
    for i, row in enumerate(board):
        for j, col in enumerate(board[i]):
            if board[i][j] == 0:
                screen.blit(ICON_O, (j * PIXEL_WIDTH, i * PIXEL_WIDTH))
            if board[i][j] == 1:
                screen.blit(ICON_X, (j * PIXEL_WIDTH, i * PIXEL_WIDTH))


def has_equal_icons(elements, game_player):
    for element in elements:
        if element != game_player:
            return False
    return True

def has_winning_row(game_player):
    return has_equal_icons(board[0], game_player) \
        or has_equal_icons(board[1], game_player) \
        or has_equal_icons(board[2], game_player)

def has_winning_col(game_player):
    return has_equal_icons([board[0][0], board[1][0], board[2][0]], game_player) \
        or has_equal_icons([board[0][1], board[1][1], board[2][1]], game_player) \
        or has_equal_icons([board[0][2], board[1][2], board[2][2]], game_player)

def has_winning_diagonal(game_player):
    return has_equal_icons([board[0][0], board[1][1], board[2][2]], game_player) \
        or has_equal_icons([board[0][2], board[1][1], board[2][0]], game_player)

def is_winner(game_player):
    return has_winning_row(game_player) \
        or has_winning_col(game_player)  \
        or has_winning_diagonal(game_player)


def check_victory():
    if is_winner(PLAYER_1):
        print("Player 1 Wins")
        return PLAYER_1
    if is_winner(PLAYER_2):
        print("Player 2 Wins")
        return PLAYER_2



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    #RENDER STUFF HERE
    pygame.display.flip()
    screen.fill('white')
    screen.blit(GRID, (0,0))
    play_turn(player)
    pygame.event.wait()
    draw_icons()
    check_victory()


pygame.quit()