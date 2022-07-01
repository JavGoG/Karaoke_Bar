class Room:
    def __init__(self, name_of_guest, name_of_room):
        self.name = name_of_room
        self.name_of_guest = name_of_guest
        self.list_of_rooms = [
                                {"Rock":[]  },
                                {"Pop":[] },
                                {"Opera":[] }
                            ]
        # self.rock_room = []
        # self.pop_room = []
        # self.opera_room = []
        # self.guests_in_rooms = {"Rock": name_of_guest}

    def check_in_guests_to_rooms(self, guest_name, room_to_add):
        for room in self.list_of_rooms:
            if room[room_to_add] == room_to_add:
                self.list_of_rooms[room_to_add] = guest_name
                
                


