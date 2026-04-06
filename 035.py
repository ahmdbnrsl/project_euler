import math as m

def check_is_tph(n):
    triangle_discriminant = 1 - 4*(-2)*n
    pentagon_discriminant = 1 - 4*3*(-2)*n
    hexagon_discriminant = 1 - 4*2*(-n)
    
    if triangle_discriminant < 0 or pentagon_discriminant < 0 or hexagon_discriminant < 0:
        return False
    
    d_t_sqrt = m.sqrt(triangle_discriminant)
    d_p_sqrt = m.sqrt(pentagon_discriminant)
    d_h_sqrt = m.sqrt(hexagon_discriminant)
    
    triangle_index = (-1 + d_t_sqrt)/2
    pentagon_index = (1 + d_p_sqrt)/6
    hexagon_index = (1 + d_h_sqrt)/4
    
    print("Triangle Index:", triangle_index, "Pentagon Index:", pentagon_index, "Hexagon Index:", hexagon_index)
    
    if triangle_index % 1 != 0 or pentagon_index % 1 != 0 or hexagon_index % 1 != 0:
        return False
    
    return True

triangle_number = lambda n: n*(n + 1)/2
pentagon_number = lambda n: n*(3*n - 1)/2
hexagon_number = lambda n: n*(2*n - 1)

# current_number = 40755
# next_number = 0
# while next_number < 1:
#     current_number += 1
#     if check_is_tph(current_number):
#         next_number = current_number

# print(next_number)

print(check_is_tph(1533776805))
print(triangle_number(55385), pentagon_number(31977), hexagon_number(27693))
