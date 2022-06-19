"""
pyopenxr example program green_blue.py

Different way to get similar display to the venerable gl_example.py

TODO: why are both eye views blue?
The same problem happens in hello_xr if you try difference glClearColors in each view.
"""

import time

from OpenGL import GL

import xr


# ContextObject is a high level pythonic class meant to keep simple cases simple.
with xr.ContextObject(
    instance_create_info=xr.InstanceCreateInfo(
        enabled_extension_names=[
            # A graphics extension is mandatory (without a headless extension)
            xr.KHR_OPENGL_ENABLE_EXTENSION_NAME,
        ],
    ),
) as context:
    eye_colors = [
        (0, 1, 0, 1),  # Left eye green
        (0, 0, 1, 1),  # Right eye blue
        (1, 0, 0, 1),  # Right eye blue
    ]

    for frame_index, (view_index, view) in enumerate(context.render_loop()):
        # set each eye to a different color (not working yet...)
        GL.glClearColor(*eye_colors[view_index])
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        # Slow things down
        time.sleep(0.010)
        # Don't run forever
        if frame_index > 200:
            break
