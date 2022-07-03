from sre_constants import GROUPREF_LOC_IGNORE
from classes.guest import Guest
from classes.song  import Song

class Room:
    def __init__(self, name_of_room, capacity,fee):
        self.name_of_room = name_of_room
        self.capacity = capacity
        self.list_of_fees = {}
        self.fee = fee
        self.fee_total = 0
        self.room_list = []
        self.Rock_list =[]
        self.Pop_list = []
        self.Opera_list = []
        self.total_capacity = 0

    def check_in_guests_to_room(self, guest_name, room_to_add, fee):
        self.add_entry_fee_room(guest_name, room_to_add, fee)
        self.room_list.append(guest_name)

    
    # def check_in_guests_to_room(self, guest_name, room_to_add, fee):
    #         if self.capacity <= self.total_capacity:
    #             self.name_of_room_list.append(guest_name)
    #             self.list_of_rooms += [self.name_of_room_list]
    #             self.add_entry_fee_room(guest_name,room_to_add)
    #             self.fee_total += fee
    #         else:
    #             print(f"The room {room_to_add} is full")
        
    def check_out_guests_from_room(self, guest_name):
        self.room_list.remove(guest_name) 
    
    def add_entry_fee_room(self, guest_name, room_name, fee):
        self.fee_total += fee
        self.list_of_fees.update({room_name:guest_name})

    def remove_entry_fee_room(self, guest_name, room_name):
        guest_name in self.list_of_fees
        self.list_of_fees[room_name] = "no fee"

    def track_entry_fee_per_room(self, room_name):
        return self.list_of_fees
            
    def get_total_fee(self):
        return self.fee_total