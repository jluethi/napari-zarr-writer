import napari
import numpy as np

from ._widget import zarr_writer_widget


viewer = napari.Viewer()
viewer.add_image(np.random.rand(20, 20), name="Layer 1")
viewer.add_image(np.random.rand(20, 20), name="Layer 2")

viewer.window.add_dock_widget(zarr_writer_widget)

napari.run()


