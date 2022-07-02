from sre_constants import GROUPREF_LOC_IGNORE
from classes import guest
class Room:
    def __init__(self, name_of_room, capacity,fee):
        self.name_of_room = name_of_room
        self.name_of_room_list = []
        self.capacity = capacity
        self.list_of_fees = {}
        self.fee = fee
        self.list_of_room_lists =[]
        self.fee_total = 0
    
    
    
    def check_in_guests_to_room(self, guest_name, room_to_add, fee):
        if room_to_add in self.list_of_rooms:
            if self.capacity <= len(self.name_of_room_list):
                self.name_of_room.append(guest_name)
                self.list_of_rooms += [self.name_of_room_list]
                self.add_entry_fee_room(guest_name,room_to_add)
                self.fee_total += fee
        else:
            print(f"The room {room_to_add} is full")
    
    def check_out_guests_from_room(self, guest_name, room_leaving):
        self.name_of_room_list.remove(guest_name) 
    
    def add_entry_fee_room(self, guest_name, room_name):
        if self.list_of_fees[room_name] != guest_name:
            self.list_of_fees.update(room_name, guest_name)

    def remove_entry_fee_room(self, guest_name, room_name):
        if self.list_of_fees[room_name] == guest_name:
            self.list_of_fees.remove([room_name][guest_name])

    def track_entry_fee_per_room(self, room_name):
        return self.list_of_fees[room_name]
            
    def get_total_fee(self):
        return self.fee_total