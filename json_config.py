import json
import os

SETTINGS_FILE = f"config{os.sep}settings.json"

settings = {
    "window": {
        "title": "Networks Fiability",
        "font": "FiraCode.ttf",
        "font_size": 18,
        "width": 800,
        "height": 600,
        "columns": 8,
        },

    "network": {
        "m_label": "M - Subnetworks",
        "m_min": 1, "m_max": 1000, "m_default": 50,

        "n_label": "N - Elements",
        "n_min": 1, "n_max": 1000, "n_default": 50,
        "n_max_rand": 20,

        "distr_label": "Distributions",
        "distributions": ["Normal", "Poisson", "Uniform"],
        },

    "output": {
        "colors": {
            "yellow": "ffff6d",
            "red": "ff6d6d",
            "green": "afd095"
        },
        "dir": "output"
    },
}


def save_settings(settings: dict):
    with open(SETTINGS_FILE, 'w') as outfile:
        outfile.write(json.dumps(settings, indent=4))

def load_settings() -> dict:
    with open(SETTINGS_FILE) as json_file:
        return json.load(json_file)

if __name__ == "__main__":
    save_settings(settings)
