class Room:
    def __init__(self, name, capacity, songs):
        self.name = name
        self.capacity = capacity
        self.songs = songs
        self.guests = []
        



    def guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def song_count(self):
        return len(self.songs)


    def add_song_to_room(self, song):
        self.songs.append(song)

    # def capacity_in_room(self, room):
    #     return room.capacity <= 9