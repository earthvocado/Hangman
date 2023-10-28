import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 1000, 550
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# button variables
RADIUS = 30
GAP = 5
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 65)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = [
    "Elephant", "Computer", "Butterfly", "Chocolate", "Telephone", "Sunshine", "Adventure", "Rainbow", 
    "Baseball", "Mountain", "Universe", "Elephant", "Pineapple", "Detective", "Watermelon", "ANT", 
    "TIGER", "CAT", "DOG", "HORSE", "GOAT", "CAMEL", "HEN", "OX", "SHARK", "ZEBRA", "RAT", "BEE", 
    "SPIDER", "SEAL", "PANDA", "ELEPHANT", "MOUSE", "ANIMAL", "MONKEY"
]
word = random.choice(words)
guessed = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 204, 0)

def draw():
    win.fill(WHITE)

    # หัวเกม
    text = TITLE_FONT.render("Hnagman", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # แสดงคำที่ทาย
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (140, 200))

    # สร้างปุ่ม
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
    win.blit(images[hangman_status], (500, -40))
    pygame.display.update()

# แสดงข้อความจบเกม
def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text,(WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status
    FPS = 60
    clock = pygame.time.Clock()
    # run = True
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:False
                # run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        draw()
        won = True
        # ลูปจนกว่าจะเจอตัวอักษรใน word ที่ยังไม่กด
        for letter in word:
            if letter not in guessed:
                won = False
                break 
        # อันนี้ของ while ลูปเช็คว่าชนะหรือแพ้ ถ้าไม่ใช่ทั้งสองอย่างก็ลูปต่อไป
        if won:
            display_message("You WON!")
            break
        if hangman_status == 6:
            display_message("You LOST!")
            break

while True:
    main()
pygame.quit()