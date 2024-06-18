import os
import shutil
import pickle
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(base_dir, '../tmp/output')
plots_dir = os.path.join(base_dir, '../tmp/plots')
logs_dir = os.path.join(base_dir, '../tmp/logs')

def plot_file_name(type, model_type):
    return os.path.join(plots_dir, f'{model_type}-confusion-matrix-for-{type}-data.png')

def load_pickle(model):
    try:
        with open(f'tmp/models/{model}_DBT.pickle', 'rb') as f:
            loaded_model = pickle.load(f)
        return loaded_model
    except FileNotFoundError:
        print(f"Error: The file 'tmp/models/{model}_DBT.pickle' was not found.")
        return None
    except Exception as e:
        print(f"Error loading the pickle file: {str(e)}")
        return None


def setup_save_directory():
    os.makedirs(save_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)

def image_file_name(type, idx, value):
    return os.path.join(
        save_dir, f'{type}-{idx}-original-{value}-predict-{value}.png')

def create_log_file(name):
    log_path = os.path.join(logs_dir, name)
    if os.path.exists(log_path):
        prev_log_path = log_path.replace('.log', '-prev.log')
        if os.path.exists(prev_log_path):
            os.remove(prev_log_path)
        shutil.move(log_path, prev_log_path)
    return open(log_path, "w")
