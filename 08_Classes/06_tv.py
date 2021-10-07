class Tv:
    canal = 1
    volume = 10

    def trocar_canal(self, canal):
        if canal > 10 or canal < 0:
            print('__')
        else:
            self.canal = canal
            print(f'Canal: {self.canal}')

    def aumentar_volume(self):
        if self.volume < 20:
            self.volume += 1
            print(f'Volume: {self.volume}')
        else:
            print(f'Volume: {self.volume}')

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f'Volume: {self.volume}')
        else:
            print(f'Volume: {self.volume}')


tv = Tv()
tv.trocar_canal(5)
tv.aumentar_volume()
tv.diminuir_volume()
for x in range(0, 15):
    tv.aumentar_volume()

