#!/usr/bin/env python

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
import os




dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)


with dpg.font_registry():
    font = dpg.add_font(f"config{os.sep}FiraCode.ttf", 28)

dpg.bind_font(font)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# import dearpygui.dearpygui as dpg

# dpg.create_context()

# with dpg.window(tag="Primary Window"):
#     dpg.add_text("Hello, world")
#     dpg.add_slider_int(label="M - Subnetworks")
#     dpg.add_slider_int(label="N - Elements")

# with dpg.font_registry():
#     font = dpg.add_font("FiraCode.ttf", 18)

# dpg.bind_font(font)


# dpg.create_viewport(title='Networks Fiability', width=600, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.set_primary_window("Primary Window", True)
# dpg.start_dearpygui()
# dpg.destroy_context()
