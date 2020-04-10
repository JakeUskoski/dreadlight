import os
from pathlib import Path

ROOT_DIR = os.path.join(str(Path.home().absolute().resolve()), '.dreadlight')
SAVE_DIR = os.path.join(ROOT_DIR, 'saves')
SHOPS_DIR = os.path.join(SAVE_DIR, 'shops')
ENEMIES_DIR = os.path.join(ROOT_DIR, 'enemies')
ITEMS_DIR = os.path.join(ROOT_DIR, 'items')
MAGIC_DIR = os.path.join(ROOT_DIR, 'magic')
SKILLS_DIR = os.path.join(ROOT_DIR, 'skills')
CLASSES_DIR = os.path.join(ROOT_DIR, 'classes')
STATS_DIR = os.path.join(ROOT_DIR, 'stats')
ATTRIBUTES_DIR = os.path.join(ROOT_DIR, 'attributes')
TYPES_DIR = os.path.join(ROOT_DIR, 'types')
CONCEPTS_DIR = os.path.join(ROOT_DIR, 'concepts')
LOCATIONS_DIR = os.path.join(ROOT_DIR, 'locations')
DISCOVERIES_DIR = os.path.join(SAVE_DIR, 'discoveries')


def make_paths(*paths):
    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)


def prepare_paths():
    make_paths(ROOT_DIR)
    make_paths(TYPES_DIR, ATTRIBUTES_DIR, STATS_DIR)
    make_paths(LOCATIONS_DIR, CONCEPTS_DIR)
    make_paths(ITEMS_DIR, MAGIC_DIR, SKILLS_DIR)
    make_paths(SAVE_DIR, SHOPS_DIR, DISCOVERIES_DIR)
    make_paths(CLASSES_DIR, ENEMIES_DIR)
