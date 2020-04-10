import os
from pathlib import Path

ROOT_DIR = os.path.join(Path.home().absolute().resolve().as_uri(), '.dreadlight')
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


def make_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def prepare_paths():
    make_path(ROOT_DIR)
    make_path(SAVE_DIR)
    make_path(SHOPS_DIR)
    make_path(ENEMIES_DIR)
    make_path(ITEMS_DIR)
    make_path(MAGIC_DIR)
    make_path(SKILLS_DIR)
    make_path(CLASSES_DIR)
    make_path(STATS_DIR)
    make_path(ATTRIBUTES_DIR)
    make_path(TYPES_DIR)
    make_path(CONCEPTS_DIR)
    make_path(LOCATIONS_DIR)
    make_path(DISCOVERIES_DIR)
