#!/usr/bin/env python

import dearpygui.dearpygui as dpg
import os
from json_config import load_settings

sett = load_settings()

dpg.create_context()

def start_btn_callback(sender, app_data, user_data):
    print(f"M slider : {dpg.get_value(m_slider)}")
    print(f"N slider : {dpg.get_value(n_slider)}")
    print(f"Distribution : {dpg.get_value(distribution)}")
    for i, n in enumerate(n_elements):
        print(f"{dpg.get_value(n)}, ", end="")

    count = dpg.get_value(progress)
    while count < 1:
        import time
        time.sleep(1)
        count = count + 0.01
        dpg.set_value(progress, count)
    dpg.set_value(progress, 0)

    
n_elements = []
def variable_n_callback(sender, app_data, user_data):
    global n_elements 
    if app_data:
        for item in dpg.get_item_children(elements)[1]:
            dpg.delete_item(item)

    else:
        dpg.add_checkbox(label="Random values for each n", default_value=True, callback=random_n_callback, parent=elements)

def random_n_callback(sender, app_data, user_data):
    global n_elements 
    if app_data:
        for item in dpg.get_item_children(elements)[1]:
            dpg.delete_item(item)
        n_elements = []
        dpg.add_checkbox(label="Random values for each n", default_value=True, callback=random_n_callback, parent=elements)

    else:
        total = dpg.get_value(m_slider)
        value = dpg.get_value(n_slider)
        i = 0
        while i <= total:
            with dpg.group(parent=elements, horizontal=True):
                second = 0
                while second != sett['window']['columns']:
                    n_elements.append(dpg.add_input_int(default_value=value, width=100))
                    i += 1
                    second += 1

with dpg.window(tag="Primary Window"):

    with dpg.menu_bar():

        with dpg.menu(label="Menu"):

            dpg.add_menu_item(label="Open output directory")
            dpg.add_menu_item(label="Clean output directory")

        with dpg.menu(label="Tools"):
            dpg.add_menu_item(label="Show About")
            dpg.add_menu_item(label="Show Metrics")
            dpg.add_menu_item(label="Show Documentation")
            dpg.add_menu_item(label="Show Debug")

        with dpg.menu(label="settings"):
            dpg.add_menu_item(label="Open settings window")

        dpg.add_menu_item(label="About")

    dpg.add_text("Number of subnetworks in current network")
    m_slider = dpg.add_drag_int(label=sett['network']['m_label'], 
            default_value=sett['network']['m_default'], 
            min_value=sett['network']['m_min'], 
            max_value=sett['network']['m_max'])

    dpg.add_text("Number of elements per subnetwork")

    n_checkbox = dpg.add_checkbox(label="N is Constant", default_value=True, callback=variable_n_callback)

    n_slider = dpg.add_drag_int(label=sett['network']['n_label'], 
            default_value=sett['network']['n_default'], 
            min_value=sett['network']['n_min'], 
            max_value=sett['network']['n_max'])

    with dpg.group() as elements:
        pass

    distribution = dpg.add_combo(items=sett['network']['distributions'],
            default_value=sett['network']['distributions'][0],
            label=sett['network']['distr_label'])

    with dpg.group(horizontal=True):
        progress = dpg.add_progress_bar(default_value=0.0)
        dpg.add_button(label="Start", callback=start_btn_callback)

with dpg.font_registry():
    font = dpg.add_font(f"config{os.sep}{sett['window']['font']}", sett['window']['font_size'])

dpg.bind_font(font)


dpg.create_viewport(title=sett["window"]["title"], 
        width=sett["window"]["width"], 
        height=sett["window"]["height"])


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
