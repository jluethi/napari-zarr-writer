import napari
import zarr
import ome_zarr

from magicgui import magic_factory
from pathlib import Path

from ._util import *


@magic_factory(
    call_button="Write to disk",
    layout="vertical",
    save_path={"widget_type": "FileEdit", "label": "Save file as:", "mode": "w"},
    chunks={"widget_type": "LineEdit"},
    byte_order={"widget_type": "LineEdit"},
    # rechunker={"widget_type": "CheckBox"}, # not yet implemented
)
def zarr_writer_widget(
    viewer: napari.Viewer,
    layer: napari.layers.Layer,
    save_path: Path,
    chunks=None,
    byte_order="tczyx",
    # rechunker=False, # not yet implemented
) -> None:
    data, meta = get_data(layer)

    # hande special cases
    if isinstance(data, type(None)):
        return None
    elif str(save_path) == '.':
        viewer.status = 'ZarrWriter: No save path specified!'
        return None

    # init zarr dir
    store = zarr.DirectoryStore(save_path)
    group = zarr.group(store=store)

    # save layer
    chunks = parse_chunks(chunks)
    ome_zarr.writer.write_image(data, group, chunks=chunks, byte_order=byte_order)
    print('File saved')
