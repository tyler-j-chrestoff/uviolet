# uviolet
Learning Astral's Python uv tool.

## `uv init`
The `init` command starts a project. Adds `pyproject.toml`, `.python-version`, and `main.py`.

## `uv add`
The `add` command installs dependencies to a project. It adds `dependencies` to the `pyproject.toml` file and adds a `uv.lock` file if one does not exist.

### --script
With the `--script` option, `uv` manages dependencies at the script level by adding metadata-comments to the `.py` file.
