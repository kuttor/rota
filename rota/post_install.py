#!/usr/bin/env python3

# This script creates a configuration file for the rota tool.
# Default location: $XDG_CONFIG_HOME/rota/rota.conf
# Custom location, set the $ROTA_CONFIG_FILE env-variable.

import os
from pathlib import Path

def get_config_template(profile_name: str = "default") -> str:
    """Create a configuration file template.
    
    Example output:
    [profile_name]
    secret_key = <SECRET_KEY>
    access_key = <ACCESS_KEY>
    region     = <REGION>
    bucket     = <BUCKET_NAME>
    """
    template = f"[{profile_name}]\n"
    template += "secret_key = <SECRET_KEY>\n"
    template += "access_key = <ACCESS_KEY>\n"
    template += "region     = <REGION>\n"
    template += "bucket     = <BUCKET_NAME>"
    return template

def get_config_path() -> Path:
    """Confirms rota.conf file location."""
    custom = os.environ.get('ROTA_CONFIG_FILE')
    xdg_home = os.environ.get('XDG_CONFIG_HOME')
    system = Path(xdg_home if xdg_home else Path.home() / '.config') / 'rota' / 'rota.conf'
    return Path(custom) if custom else system

def create_config():
    """Create a config file if it doesn't exist yet."""
    config_file = get_config_path()
    if not config_file.exists():
        config_file.parent.mkdir(parents=True, exist_ok=True)
        config_file.write_text(get_config_template())
        config_file.chmod(0o600)  # User read/write only

create_config()