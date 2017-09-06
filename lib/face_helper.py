def faces_between_vertex_groups(
    group_1, group_2, create_loop=False, face_count=None):
    if not face_count:
        face_count = 2 if create_loop else 1
    if create_loop:
        group_1 = __wrap_tuple(group_1)
        group_2 = __wrap_tuple(group_2)

    split_group_1 = __split_tuple(group_1, face_count)
    split_group_2 = __split_tuple(group_2, face_count)

    faces = [__face(g1, g2) for g1, g2 in zip(split_group_1, split_group_2)]
    return faces

def __wrap_tuple(tuple_to_wrap):
    return tuple_to_wrap + (tuple_to_wrap[0],)

def __split_tuple(tuple_to_split, number_of_chunks):
    chunk_size = len(tuple_to_split) // number_of_chunks
    chunks = []
    for i in range(number_of_chunks):
        chunk = tuple_to_split[chunk_size * i : chunk_size * (i + 1) + 1]
        chunks.append(chunk)
    return tuple(chunks)

def __face(group_1, group_2):
    return tuple(group_1) + tuple(reversed(group_2))
