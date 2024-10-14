import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        count = 0
        enemy_power = 100
        print(f'{self.name}, на нас напали!')
        while enemy_power > 0:
            count += 1
            enemy_power -= self.power
            print(f'{self.name} сражается {count} день(дней), осталось {enemy_power} воинов\n')
            time.sleep(1)
        else:
            print(f'{self.name} одержал победу спустя {count} дней(дня)!\n')


k1 = Knight('Sir Lancelot', 10)
k2 = Knight("Sir Galahad", 20)

k1.start()
k2.start()

k1.join()
k2.join()

print('Все битвы закончились!')
