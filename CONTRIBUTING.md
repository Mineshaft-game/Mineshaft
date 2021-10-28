# Contribution rules
- Using git is preferred over GitHub web/Gitlab WebIDE.
- Describe what you changed in the commits: no stupid commits like "Update README.md"
# Structure information
One of the core ideas of Mineshaft, is the replaceable modules.
You can replace any piece of the Mineshaft modules with your own.Think of Mineshaft as a puzzle where you can replace pieces with different ones.
The "puzzle" is split into these directories:
- `api` is the directory to store the APIs for the game
- `buildtools` are the various tools to make files like `.exe` or `.whl`
- `scripts` are the scripts to do various stuffs. The documentation for them is available in the directory.
- `lang` are the language files stored in `.xml` format.
- `resources` used to have some files related to Mineshaft, which are now moved to [`libmineshaft`](https://github.com/Mineshaft-game/libmineshaft). This will be deprecated soon.
- `index` contains the index for blocks, items, and other.

These have been converted into submodules:
- `render` is the rendering engine. The rendering engine manages how does the game get displayed. it also manages shading.
- `gen` is the world generation engine.
- `assets` are the assets like music, sounds, textures, and other stuff. 

The main script is in the `main.py` file at directory root. It contains most of the code for Mineshaft.
# Setting up the developement enivroment
As always, clone the repository by any means, ssh, GCM core, normal clone,etc.

```
git clone https://github.com/Mineshaft-game/Mineshaft
```

after that, create a remote named `gitlab` using `git remote add gitlab https://gitlab.com/double-fractal/mineshaft2d/Mineshaft`



