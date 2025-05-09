#!/usr/bin/python3
import importlib.util
import os

if __name__ == "__main__":
    # Chemin absolu vers le fichier .pyc compilé dans __pycache__
    base_dir = os.path.dirname(__file__)
    pyc_filename = [f for f in os.listdir(os.path.join(base_dir, "__pycache__")) if f.startswith("hidden_4") and f.endswith(".pyc")][0]
    pyc_path = os.path.join(base_dir, "__pycache__", pyc_filename)

    # Charger et exécuter le module
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Afficher les noms qui ne commencent pas par __
    for name in sorted(name for name in dir(module) if not name.startswith("__")):
        print(name)
