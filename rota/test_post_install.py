#!/usr/bin/env python3

import os
import shutil
from pathlib import Path
import unittest
from .post_install import get_config_path, create_config

class TestPostInstall(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        # Save original env vars
        self.original_env = {}
        for var in ['XDG_CONFIG_HOME', 'ROTA_CONFIG_FILE', 'HOME']:
            self.original_env[var] = os.environ.get(var)
        
        # Create test home directory
        self.test_home = Path('/tmp/test_rota_home')
        self.test_home.mkdir(exist_ok=True)
        os.environ['HOME'] = str(self.test_home)

    def tearDown(self):
        """Clean up test environment."""
        # Restore original env vars
        for var, value in self.original_env.items():
            if value is None:
                os.environ.pop(var, None)
            else:
                os.environ[var] = value
        
        # Clean up test directories
        shutil.rmtree(self.test_home, ignore_errors=True)

    def test_default_path(self):
        """Test with no environment variables set."""
        for var in ['XDG_CONFIG_HOME', 'ROTA_CONFIG_FILE']:
            os.environ.pop(var, None)
        
        expected = Path(self.test_home) / '.config' / 'rota' / 'rota.conf'
        self.assertEqual(get_config_path(), expected)

    def test_xdg_config_home(self):
        """Test with XDG_CONFIG_HOME set."""
        os.environ.pop('ROTA_CONFIG_FILE', None)
        xdg_path = '/custom/xdg'
        os.environ['XDG_CONFIG_HOME'] = xdg_path
        
        expected = Path(xdg_path) / 'rota' / 'rota.conf'
        self.assertEqual(get_config_path(), expected)

    def test_rota_config_file(self):
        """Test with ROTA_CONFIG_FILE set."""
        custom_path = '/custom/config'
        os.environ['ROTA_CONFIG_FILE'] = custom_path
        
        # Should take precedence over XDG_CONFIG_HOME
        os.environ['XDG_CONFIG_HOME'] = '/should/not/use'
        
        self.assertEqual(get_config_path(), Path(custom_path))

    def test_empty_vars(self):
        """Test with empty environment variables."""
        os.environ['XDG_CONFIG_HOME'] = ''
        expected = Path(self.test_home) / '.config' / 'rota' / 'rota.conf'
        self.assertEqual(get_config_path(), expected)

        os.environ['ROTA_CONFIG_FILE'] = ''
        self.assertEqual(get_config_path(), Path(''))

    def test_relative_paths(self):
        """Test with relative paths."""
        os.environ['ROTA_CONFIG_FILE'] = './config'
        self.assertEqual(get_config_path(), Path('./config'))

    def test_create_config(self):
        """Test actual config creation."""
        os.environ.pop('ROTA_CONFIG_FILE', None)
        os.environ.pop('XDG_CONFIG_HOME', None)
        
        create_config()
        
        config_path = get_config_path()
        self.assertTrue(config_path.exists())
        self.assertEqual(config_path.stat().st_mode & 0o777, 0o600)
        self.assertTrue(config_path.read_text().startswith('[default]'))

if __name__ == '__main__':
    unittest.main() 