"""
This script is handy when you need to rename multiple files
in a folder based on specific criteria. For example, you can
add a prefix, suffix, or replace text in filenames.
"""

import os

folder_path = '/path/to/folder'
for filename in os.listdir(folder_path):
    if filename.startswith('prefix_'):
        new_filename = filename.replace('prefix_', 'new_prefix_')
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
