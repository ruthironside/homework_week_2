class Room:
    def __init__(self, name, capacity, songs):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.songs = songs
        



    def guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def song_count(self):
        return len(self.songs)


    # def add_song_to_room(self, song):
    #     self.song_list.append(song)