#!/usr/bin/env python

import dearpygui.dearpygui as dpg
import os
from json_config import load_settings

settings = load_settings()

dpg.create_context()

def start_btn_callback(sender, app_data, user_data):
    print(f"M slider : {dpg.get_value(m_slider)}")
    print(f"N slider : {dpg.get_value(n_slider)}")
    print(f"Distribution : {dpg.get_value(distribution)}")
    

with dpg.window(tag="Primary Window"):

    with dpg.menu_bar():

        with dpg.menu(label="Menu"):

            dpg.add_text("This menu is just for show!")
            dpg.add_menu_item(label="Reset")
            dpg.add_menu_item(label="Open Output Directory")

        with dpg.menu(label="Tools"):
            dpg.add_menu_item(label="Show About")
            dpg.add_menu_item(label="Show Metrics")
            dpg.add_menu_item(label="Show Documentation")
            dpg.add_menu_item(label="Show Debug")

        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Wait For Input", check=True)
            dpg.add_menu_item(label="Toggle Fullscreen")

        dpg.add_menu_item(label="About")

    dpg.add_text("Hello, world")
    
    m_slider = dpg.add_slider_int(label=settings['network']['m_label'], 
            default_value=settings['network']['m_default'], 
            min_value=settings['network']['m_min'], 
            max_value=settings['network']['m_max'])

    n_slider = dpg.add_slider_int(label=settings['network']['n_label'], 
            default_value=settings['network']['n_default'], 
            min_value=settings['network']['n_min'], 
            max_value=settings['network']['n_max'])

    distribution = dpg.add_combo(items=settings['network']['distributions'],
            default_value=settings['network']['distributions'][0],
            label=settings['network']['distr_label'])

    with dpg.group(horizontal=True):
        dpg.add_progress_bar(default_value=0.78, overlay="1367/1753")
        dpg.add_button(label="Start", callback=start_btn_callback)

with dpg.font_registry():
    font = dpg.add_font(f"config{os.sep}{settings['window']['font']}", settings['window']['font_size'])

dpg.bind_font(font)


dpg.create_viewport(title=settings["window"]["title"], 
        width=settings["window"]["width"], 
        height=settings["window"]["height"])


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
