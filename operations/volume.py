import os

def set_volume(volume_level):
    """
    Set the volume level using amixer.

    :param volume_level: Volume level in percentage (0-100)
    """
    os.system(f"amixer sset 'Master' {volume_level}%")
