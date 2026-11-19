# Installation

## Install

::::{tab-set}
:::{tab-item} Installer
```bash
curl -fsSL https://raw.githubusercontent.com/Akademie-Olympia/aco-arch-dotfiles/main/install.sh | bash -s -- waybar
```
:::
:::{tab-item} pacman
If the repository is already set up (installer of `aco-arch-dotfiles`):

```bash
sudo pacman -S aco-arch-dotfiles-waybar
aco install waybar
```
:::
::::

The installer verifies the signing key, sets up the pacman repository, installs `aco-arch-dotfiles-waybar` with its dependencies and activates the
configuration. Existing files are backed up first.

## Update

```bash
sudo pacman -Syu        # or: aco update
```

New defaults are merged with your own changes. Where they differ, `aco` places a `.pacnew` file next to yours. After changes restart the
application (`Super + Shift + B` reloads Waybar).

## Remove

```bash
aco deactivate waybar                 # restores the backed-up settings
sudo pacman -Rns aco-arch-dotfiles-waybar
```

`pacman` never deletes your home directory, backups or your own changes.

## Where things live

| Location | Content |
| --- | --- |
| `/usr/share/arch-dotfiles/waybar/` | Package defaults (managed by pacman) |
| `~/.local/share/arch-dotfiles/config/waybar/` | Your editable copy – change things here |
| `~/.config/waybar` | Link to your copy |

`aco path` prints the directory of your copies. Sources and package recipe:
[`packaging/arch/PKGBUILD`](https://github.com/Akademie-Olympia/aco-waybar/blob/main/packaging/arch/PKGBUILD).
