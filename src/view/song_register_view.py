import os

class SongRegisterView:
    def registry_song_initial(self) -> dict:
        self.__clear()
        print("Implementar Nova Música \n \n")

        title = input("Título: ")
        artist = input("Artista: ")
        year = input("Ano: ")

        new_song_information = {
            "title": title, "artist": artist, "year": year
        }

        return new_song_information
    
    def __clear(self):
        os.system("cls") or os.system("clear")

