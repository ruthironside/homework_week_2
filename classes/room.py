class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []

    # def add_song_to_room(self, song):
    #     self.rooms.append(song)

    def guest_count(self):
        return len(self.guests)

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)