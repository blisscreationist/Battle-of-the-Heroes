import pygame
import random

# Класс героя
class Hero:
    def __init__(self, name, image_path, x, y, health=100, attack_power=20):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.attack_animation = False
        self.attack_count = 0

    def attack(self, other):
        self.attack_animation = True
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.attack_animation:
            self.attack_count += 1
            if self.attack_count > 10:
                self.attack_animation = False
                self.attack_count = 0

        # Рисуем полоску здоровья
        health_bar_width = 100
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 20, health_bar_width, 10))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 20, health_bar_width * health_ratio, 10))

    def __str__(self):
        return f"{self.name}: {self.health} HP"

# Класс игры
class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name, 'fox_1.png', 100, 300)
        self.computer = Hero(computer_name, 'mvSatyr.prev.png', 600, 300)

        # Инициализация Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Битва героев")
        self.font = pygame.font.Font(None, 36)

        # Кнопки
        self.attack_button = pygame.Rect(350, 500, 100, 50)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (x, y))

    def draw_button(self, rect, text):
        pygame.draw.rect(self.screen, (0, 128, 0), rect)
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (rect.x + 10, rect.y + 10))

    def start(self):
        print("Игра началась!")
        turn = 0  # 0 - ход игрока, 1 - ход компьютера
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.attack_button.collidepoint(event.pos):
                        if turn == 0:
                            self.player.attack(self.computer)
                        else:
                            self.computer.attack(self.player)
                        turn = 1 - turn

            self.screen.fill((0, 0, 0))

            self.player.draw(self.screen)
            self.computer.draw(self.screen)

            self.draw_text(str(self.player), 50, 50)
            self.draw_text(str(self.computer), 500, 50)

            self.draw_button(self.attack_button, "Атака")

            pygame.display.flip()
            pygame.time.delay(1000)

            if not self.player.is_alive() or not self.computer.is_alive():
                running = False

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

        pygame.quit()

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()