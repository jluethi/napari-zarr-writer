from ast import literal_eval as make_tuple

import napari
import zarr
import ome_zarr
import numpy as np

from magicgui import magicgui

from ._util import get_data

def parse_chunks(chunks):
    if isinstance(chunks, str):
        if chunks == 'None':
            return None
        else:
            return make_tuple(chunks)
    else:
        return None


@magicgui(
    call_button="Write to disk",
    layout="vertical",
    chunks={"widget_type": "LineEdit"},
    byte_order={"widget_type": "LineEdit"},
    rechunker={"widget_type": "CheckBox"},
    save_path={"widget_type": "FileEdit", "label": "Save file as:", "mode": "w"},
)
def zarr_writer_widget(
    layer: napari.layers.Layer,
    save_path,
    chunks=None,
    byte_order="tczyx",
    rechunker=False,
) -> None:
    data, meta = get_data(layer)
    # mock
    print(data.shape)
    print(meta)
    chunks = parse_chunks(chunks)
    img_np = np.asarray(data)
    store = zarr.DirectoryStore(save_path)
    g = zarr.group(store=store)
    ome_zarr.writer.write_image(img_np, g, chunks=chunks)
    print('File saved')
