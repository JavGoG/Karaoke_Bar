class Guest:
    def __init__(self, name):
        self.name = name

    
    def check_in_guests_to_rooms(self, guest_name, room_to_add):
        for room in self.list_of_rooms:
            if room[room_to_add] == room_to_add:
                self.list_of_rooms[room_to_add] = guest_name