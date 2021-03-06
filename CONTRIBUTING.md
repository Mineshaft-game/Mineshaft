# Contribution rules
- Using git is preferred over GitHub web/Gitlab WebIDE.
- Describe what you changed in the commits: no stupid commits like "Update README.md"
- Please do not use release candidate versions of libmineshaft
## Codetags
Use these codetags in comments:
- TODO: Introduces a general reminder about work that needs to be done
- FIXME: Introduces a reminder that this part of the code doesn't entirely work  
- HACK:  Introduces a reminder that this part of the code works, perhaps barely, but that code should be improved
- WARNING: Something does not work
- XXX: Major problem
- NOTE: A note



Most text editor plugins/IDEs should automatically import them into tasks.
However, some of them like Eric, import only some (e.g. only TODO, FIXME, WARNING and NOTE).


-----


# Structure information
One of the core ideas of Mineshaft, is the replaceable modules.
You can replace any piece of the Mineshaft modules with your own.Think of Mineshaft as a puzzle where you can replace pieces with different ones.
The "puzzle" is split into these directories:
- `api` is the directory to store the APIs for the game
- `buildtools` are the various tools to make files like `.exe` or `.whl`
- `scripts` are the scripts to do various stuffs. The documentation for them is available in the directory.
- `lang` are the language files stored in `.xml` format.
- `index` contains the index for blocks, items, and other.
- `assets` are the game assets (music, images, fonts, etc.).

These have been converted into submodules:
- `render` is the rendering engine. The rendering engine manages how does the game get displayed. it also manages shading.
- `gen` is the world generation engine.

These no longer exist, but may be readded in the future:
- `resources` used to have some files related to Mineshaft, which are now moved to [`libmineshaft`](https://github.com/Mineshaft-game/libmineshaft).
- `assets` was a submodule previously, but was converted into a normal directory because of complexity. It may be readded as a submodule.

The main script is in the `main.py` file at directory root. It contains most of the code for Mineshaft.
# Setting up the developement enivroment
As always, clone the repository by any means, ssh, GCM core, normal clone,etc.

```
git clone https://github.com/Mineshaft-game/Mineshaft
```

after that, create a remote named `gitlab` using `git remote add gitlab https://gitlab.com/double-fractal/mineshaft2d/Mineshaft`



