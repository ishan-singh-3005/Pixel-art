import pygame

pygame.init()

RED = (255, 0, 0)
GREEN= (0, 255, 0)
BLUE= (0, 0, 255)
YELLOW= (255, 255, 0)
WHITE= (255, 255, 255)
BLACK= (0, 0, 0)
PURPLE= (128, 0, 128)
ORANGE= (255, 165, 0)
GREY= (128, 128, 128)
TURQUOISE= (64, 224, 208)

FONT = pygame.font.SysFont('comicsans', 40)

WIDTH = 650
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pixel Art")

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.width = width
        self.total_rows = total_rows

# return pos of spot that is clicked
    def get_pos(self):
        return self.row, self.col
    
# draw spot
    def draw(self, win):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, self.width, self.width))

# change to set colours
    def reset(self):
        self.colour = WHITE

    def make_orange(self):
        self.colour = ORANGE

    def make_red(self):
        self.colour = RED

    def make_green(self):
        self.colour = GREEN
    
    def make_black(self):
        self.colour = BLACK
    
    def make_turquoise(self):
        self.colour = TURQUOISE
    
    def make_purple(self):
        self.colour = PURPLE
    
    def make_grey(self):
        self.colour = GREY
    
    def make_blue(self):
        self.colour = BLUE
    
    def make_yello(self):
        self.colour = YELLOW

def make_grid(rows, width):
    grid = []
    gap= width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col

def handle_pressed(keys_pressed, rows, width, grid):

    if keys_pressed[pygame.K_o] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_orange()
    
    if keys_pressed[pygame.K_r] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_red()

    if keys_pressed[pygame.K_g] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_green()
    
    if keys_pressed[pygame.K_b] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_black()

    if keys_pressed[pygame.K_t] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_turquoise()
    
    if keys_pressed[pygame.K_p] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_purple()

    if keys_pressed[pygame.K_q] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_grey()
    
    if keys_pressed[pygame.K_w] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_blue()

    if keys_pressed[pygame.K_y] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.make_yello()

    if keys_pressed[pygame.K_w] and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.reset()
    
    if keys_pressed[pygame.K_c]:
        grid = make_grid(rows, width)
        for row in grid:
            for spot in row:
                spot.reset()
    
    if pygame.mouse.get_pressed()[2]:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, rows, width)
        spot = grid[row][col]

        spot.reset()

def instructions(win, width):
    win.fill(BLACK)
    command_1 = FONT.render("Press C to replay", 1, ORANGE)
    command_2 = FONT.render("Press Q to quit", 1, ORANGE)
    win.blit(command_1, (width / 2 - command_1.get_width() / 2, 100))
    win.blit(command_2, (width / 2 - command_2.get_width() / 2, 140))
    pygame.display.update()

def main(win, width):
    ROWS = 50

    grid = make_grid(ROWS, width)
    run = True

    selected_colour = None

    while run:
        draw(win, grid, ROWS, width)
        keys_pressed = pygame.key.get_pressed()
        handle_pressed(keys_pressed, ROWS, width, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    grid = make_grid(ROWS, width)
                    for row in grid:
                        for spot in row:
                            spot.reset()
                if event.key == pygame.K_i:
                    instructions(win, width)
                    print("pressed")
        pygame.display.update()

    
    pygame.quit()

main(WIN, WIDTH)