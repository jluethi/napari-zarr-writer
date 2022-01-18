from ast import literal_eval as make_tuple

def get_data(layer):
    if layer:
        return layer.data, layer.metadata
    else:
        return None, dict()


def parse_chunks(chunks):
    if isinstance(chunks, str):
        if chunks == 'None':
            return None
        else:
            return make_tuple(chunks)
    else:
        return None