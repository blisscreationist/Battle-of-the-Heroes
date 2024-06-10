import pygame
import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} HP"


class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)


        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Битва героев")
        self.font = pygame.font.Font(None, 36)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (x, y))

    def start(self):
        print("Игра началась!")
        turn = 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))

            if self.player.is_alive() and self.computer.is_alive():
                if turn == 0:
                    self.player.attack(self.computer)
                else:
                    self.computer.attack(self.player)
                turn = 1 - turn  

            self.draw_text(str(self.player), 50, 50)
            self.draw_text(str(self.computer), 50, 100)

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