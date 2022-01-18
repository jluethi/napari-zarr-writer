import napari

from magicgui import magicgui


def get_data(layer):
    return layer.data, layer.meta


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
