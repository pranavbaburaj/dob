import math
import random

class List():
    def __init__(self, data_type):
        self.members = []
        self.data_type = data_type
    
    def len(self):
        # grab the length of 
        return len(self.members)

    @staticmethod
    def create(data):
        # Create a  new Single list instance
        # via a static metnod
        return SingleList(data)

    # add a new member to the list
    def add(self, d_to_add):
        if isinstance(d_to_add, self.data_type):
            # check the type
            if d_to_add not in self.members:
                self.members.append(d_to_add)
        else:
            raise TypeError("Invalid type")

    def elementAt(self, i):
        return self.members[i]

    def median(self):
        if self.data_type == int or self.data_type == float:
            # odd array = [1, 2, 3]
            if len(self.members) % 2 == 0:
                # even aray = [1, 2, 3, 4]
                a_lenght_h = int(len(self.members) / 2)   
                s_sum_of = self.members[a_lenght_h] + self.members[a_lenght_h - 1]
                return s_sum_of / 2
            else:
                return self.members[math.floor(len(self.members) / 2)]
        else:
            raise TypeError("Type not supported for finding the median")

    # delete an element by index
    def delete_index(self, i_t_d):
        return self.members.pop(i_t_d)

    def search_insert_position(self, target):
        if isinstance(target, self.data_type):
            if target in self.members:
                return self.members.index(target)
            else:
                self.members.append(target)
                return self.members.index(target)
        else:
            raise TypeError("Invalid target type")

    def index(self, e_f_i):
        if e_f_i in self.members:
            return self.members.index(e_f_i)

        return None

    def peak_index(self):
        return self.members.index(max(self.members))

    # def range(self):
    #     return Ranges(self.members)

    def all(self):
        return self.members

    def count(self, i):
        if i in self.members:
            return self.members.count(i)

        return None

    def sort(self):
        self.members.sort()
        return self.members

    def find(self, d_t_f):
        indexes = []
        for x in range(len(self.members)):
            if self.members[x] == d_t_f:
                indexes.append(x)

        return indexes

    def delete(self, data_to_delete):
        access_data_indexes = []
        for index in range(len(self.members)):
            if self.members[index] == data_to_delete:
                access_data_indexes.append(index)
        
        for i in range(len(access_data_indexes)):
            del self.members[access_data_indexes[i]]
        
        return self.members

    def clear(self):
        self.members = []
        return self.members

    def reverse(self):
        self.members.reverse()
        return self.members

    def alternate_indexes(self):
        v_a_r = [[],[]]
        for x in range(len(self.members)):
            if x % 2 == 0:
                v_a_r[0].append(x)
            else:
                v_a_r[-1].append(x)

        return v_a_r

    def choice(self): 
        return self.members[random.randint(0, len(self.members))]