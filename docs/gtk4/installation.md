# Installation

## Install

::::{tab-set}
:::{tab-item} Installer
```bash
curl -fsSL https://raw.githubusercontent.com/Akademie-Olympia/aco-arch-dotfiles/main/install.sh | bash -s -- gtk-4.0
```
:::
:::{tab-item} pacman
If the repository is already set up (installer of `aco-arch-dotfiles`):

```bash
sudo pacman -S aco-arch-dotfiles-gtk-4.0
aco install gtk-4.0
```
:::
::::

The installer verifies the signing key, sets up the pacman repository, installs `aco-arch-dotfiles-gtk-4.0` with its dependencies and activates the
configuration. Existing files are backed up first.

## Update

```bash
sudo pacman -Syu        # or: aco update
```

New defaults are merged with your own changes. Where they differ, `aco` places a `.pacnew` file next to yours. After changes restart the
application.

## Remove

```bash
aco deactivate gtk-4.0                 # restores the backed-up settings
sudo pacman -Rns aco-arch-dotfiles-gtk-4.0
```

`pacman` never deletes your home directory, backups or your own changes.

## Where things live

| Location | Content |
| --- | --- |
| `/usr/share/arch-dotfiles/gtk-4.0/` | Package defaults (managed by pacman) |
| `~/.local/share/arch-dotfiles/config/gtk-4.0/` | Your editable copy – change things here |
| `~/.config/gtk-4.0` | Link to your copy |

`aco path` prints the directory of your copies. Sources and package recipe:
[`packaging/arch/PKGBUILD`](https://github.com/Akademie-Olympia/aco-gtk4/blob/main/packaging/arch/PKGBUILD).
