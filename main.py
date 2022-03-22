# https://www.youtube.com/watch?v=fGSOHM4mv40
# https://www.youtube.com/watch?v=eoP47BgS4GU&list=PLIPftk-0JEAd7ut8iqmpam9JacB_6LDb8&index=3

from game import Game

def main():
    game = Game()

    while True:
        game.handle_events()
        game.update()
        game.draw()


if __name__ == "__main__":
    main()