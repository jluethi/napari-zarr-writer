import napari
import zarr
import ome_zarr
import numpy as np

from magicgui import magicgui

from _util import get_data


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
    img_np = np.asarray(data)
    store = zarr.DirectoryStore(save_path)
    g = zarr.group(store=store)
    ome_zarr.writer.write_image(img_np, g)
    print('File saved')
