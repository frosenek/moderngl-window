from pathlib import Path

import moderngl
from pyrr import Matrix44
import moderngl_window
from base import CameraWindow


class FragmentPicking(CameraWindow):
    title = "Fragment Picking"
    gl_version = 3, 3
    aspect_ratio = None
    resource_dir = (Path(__file__) / '../../resources').resolve()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.projection.update(near=1.0, far=1000)
        self.camera.velocity = 100
        self.scene = self.load_scene('scenes/fragment_picking/Rogers_Thermal_11_14_Edited.obj')

    def render(self, time, frametime):
        self.ctx.enable_only(moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        self.scene.draw(
            self.camera.projection.matrix,
            self.camera.matrix,
        )
        print(self.camera.matrix)


if __name__ == '__main__':
    moderngl_window.run_window_config(FragmentPicking)
