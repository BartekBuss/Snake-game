import pygame
import time
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
szerokosc = 800
wysokosc = 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Snake Game")

# Kolory
czarny = (0, 0, 0)
bialy = (255, 255, 255)
czerwony = (255, 0, 0)
zielony = (0, 255, 0)

# Rozmiar bloku i prędkość węża
rozmiar_bloku = 20
predkosc = 15

# Czcionka i rozmiar tekstu
czcionka = pygame.font.SysFont(None, 35)

# Funkcja rysująca węża na ekranie
def rysuj_weza(waz, rozmiar_bloku):
    for segment in waz:
        pygame.draw.rect(ekran, zielony, [segment[0], segment[1], rozmiar_bloku, rozmiar_bloku])

# Funkcja rysująca punkt na ekranie
def rysuj_punkt(punkt):
    pygame.draw.rect(ekran, czerwony, [punkt[0], punkt[1], rozmiar_bloku, rozmiar_bloku])

# Funkcja obsługująca główną pętlę gry
def gra():
    gra_aktywna = True
    koniec_gry = False

    # Inicjalizacja węża i punktu startowego
    waz = [[szerokosc / 2, wysokosc / 2]]
    kierunek = "RIGHT"

    punkt = [random.randrange(1, (szerokosc // rozmiar_bloku)) * rozmiar_bloku,
             random.randrange(1, (wysokosc // rozmiar_bloku)) * rozmiar_bloku]

    while gra_aktywna and not koniec_gry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gra_aktywna = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and kierunek != "RIGHT":
                    kierunek = "LEFT"
                elif event.key == pygame.K_RIGHT and kierunek != "LEFT":
                    kierunek = "RIGHT"
                elif event.key == pygame.K_UP and kierunek != "DOWN":
                    kierunek = "UP"
                elif event.key == pygame.K_DOWN and kierunek != "UP":
                    kierunek = "DOWN"

        # Aktualizacja położenia węża
        nowa_glowa = [waz[0][0], waz[0][1]]

        if kierunek == "LEFT":
            nowa_glowa[0] -= rozmiar_bloku
        elif kierunek == "RIGHT":
            nowa_glowa[0] += rozmiar_bloku
        elif kierunek == "UP":
            nowa_glowa[1] -= rozmiar_bloku
        elif kierunek == "DOWN":
            nowa_glowa[1] += rozmiar_bloku

        # Przejście przez przeciwną stronę ekranu
        nowa_glowa[0] = nowa_glowa[0] % szerokosc
        nowa_glowa[1] = nowa_glowa[1] % wysokosc

        waz.insert(0, nowa_glowa)

        # Sprawdzenie kolizji z punktem
        if waz[0] == punkt:
            punkt = [random.randrange(1, (szerokosc // rozmiar_bloku)) * rozmiar_bloku,
                     random.randrange(1, (wysokosc // rozmiar_bloku)) * rozmiar_bloku]
        else:
            # Jeśli wąż nie zjadł punktu, usuń ostatni segment, aby wydawało się, że wąż się porusza
            waz.pop()

        # Sprawdzenie kolizji z samym sobą
        for segment in waz[1:]:
            if waz[0] == segment:
                koniec_gry = True

        # Aktualizacja ekranu
        ekran.fill(czarny)
        rysuj_weza(waz, rozmiar_bloku)
        rysuj_punkt(punkt)

        pygame.display.update()

        # Ustawienie prędkości gry
        pygame.time.Clock().tick(predkosc)

    pygame.quit()
    quit()

# Rozpoczęcie gry
gra()
