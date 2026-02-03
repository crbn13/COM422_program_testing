from dataclasses import dataclass

@dataclass
class Table:
    def __init__(self, table_number:int, seat_count:int, is_outside:bool=False, booking=None):
        self.table_number = table_number
        self.seat_count = seat_count
        self.is_outside = is_outside

class Restaurant:
    def __init__(self):
        self.tables = {}
        pass

    def add_table(self, table:Table):
        self.tables[table.table_number] = table
        pass

    def remove_table(self, table_num:int):
        del self.tables[table_num]
        pass
