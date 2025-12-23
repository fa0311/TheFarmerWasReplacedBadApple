from frames import d

frames = d()
size = 32
frame_count = len(frames) // (size * size)

def drone_function():
    start_x = get_pos_x()
    for frame_idx in range(frame_count):
        for y in range(size):
            move(South)
            index = frame_idx * size * size + y * size + start_x
            if frames[index] != (get_entity_type() == Entities.Grass):
                till()
        while num_items(Items.Water) % 512 != 0:
            pass

for x in range(size - 1):
    spawn_drone(drone_function)
    move(East)
drone_function()
