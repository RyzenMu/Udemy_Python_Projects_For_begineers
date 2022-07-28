#  Dice Rolling Simulator

# number = 5

# def number_to_string(number):

#     switch = {
#         # 0:"zero",
#         1:"one",
#         2:"two",
#         3:"three",
#         4:"four",
#         5:"five",
#         6:"six",
#     }

#     return switch.get(number, "default")


# print(number_to_string(number))


from Visuals_For_1.visuals import visuals 
import random

# def number_to_string(number):
#     match number:
#         case 0:
#             print('zero')
#             return
#         case 1:
#             print('one')
#             return
#         case 2:
#             print('two')
#             return




# random generator
number = random.randint(1, 6)




if __name__ == "__main__":
        
    visuals(number)
    