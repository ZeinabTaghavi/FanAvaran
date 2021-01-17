def Boxing(box_number, box_size, object_volume_array, base_index):
    a_index = base_index
    object_counter = 0
    for b_n in range(box_number):  # filling each box
        total_objects_volume = 0
        while total_objects_volume <= box_size and a_index < len(object_volume_array):
            # until box is full or no object left in array
            total_objects_volume += object_volume_array[a_index]
            a_index += 1
            object_counter += 1
        if total_objects_volume > box_size:  # in case counter counts one extra object
            a_index -= 1
            object_counter -= 1
    return a_index, object_counter  # returns index of last object in boxes and numbers of objects


if __name__ == '__main__':
    while 1:
        try:
            n, m, k = map(int, input().split())
            if n < 0 or m < 0 or k < 0:
                print("wrong input! input is not a positive integer! please try again:")
                continue
            a = input().split()
            try:
                a = [int(x) for x in a]
                negative = 0
                for x in a:
                    if x < 0:
                        negative += 1
                if negative > 0:
                    print("wrong input! input is not a positive integer! please try again:")
                    continue
            except ValueError:
                print("wrong input! input is not a integer! please try again:")
                continue
        except ValueError:
            print("wrong input! input is not a integer! please try again:")
            continue
        break

    if len(a) != n:  # in case input array size is wrong
        print("wrong input! array size is wrong!")
    else:
        Base_index = 0
        last_index_in_box = 0
        object_count = 0
        while last_index_in_box < len(a):
            # until last object in boxes is the last object in array
            last_index_in_box, object_count = Boxing(m, k, a, Base_index)
            Base_index += 1
        print(object_count)
