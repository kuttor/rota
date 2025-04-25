# Changelog

## [Unreleased]

### Fixed
- Empty `XDG_CONFIG_HOME` handling in config path resolution
  - Issue: When `XDG_CONFIG_HOME` was set but empty, the config path was incorrectly resolved
  - Fix: Added explicit check for empty `XDG_CONFIG_HOME` value before falling back to `$HOME/.config`
  - Impact: Config files now correctly fall back to default location when `XDG_CONFIG_HOME` is empty
  - Code:
    ```python
    # Before (line 29)
    system = Path(os.environ.get('XDG_CONFIG_HOME', Path.home() / '.config')) / 'rota' / 'rota.conf'

    # After (lines 29-30)
    xdg_home = os.environ.get('XDG_CONFIG_HOME')
    system = Path(xdg_home if xdg_home else Path.home() / '.config') / 'rota' / 'rota.conf'
    ```