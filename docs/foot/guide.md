# Foot in daily use

Foot is a Wayland-only terminal: it starts in milliseconds, uses very little memory and has no tabs or splits. That is
deliberate – window layout is the job of Hyprland and [tmux](https://aco-tmux.readthedocs.io/en/latest/). Foot is the **lightweight
alternative** next to Kitty and Ghostty, handy for quick tasks, older hardware or as a server terminal (`footclient`).

## What this package sets

| Setting | Value | Effect |
| --- | --- | --- |
| `shell` | `/usr/bin/zsh` | Starts the ACO Zsh configuration directly |
| `font` | JetBrainsMono Nerd Font, 10.5 pt | Same font as Kitty and Ghostty; Nerd symbols for Waybar, Yazi, Neovim |
| `pad` | `8x8` | Inner padding so text does not touch the window edge |
| `[bell]` | off | No beep or notification on `\a` |
| `[cursor]` | block | |
| `alpha` | `0.90` | Slightly transparent background (visible because Hyprland composites) |
| Colours | Catppuccin Mocha | 16 terminal colours plus selection and cursor |

## Important keys

Foot keeps its defaults; the ones you will use most:

| Key | Action |
| --- | --- |
| {kbd}`Ctrl + Shift + C` / {kbd}`Ctrl + Shift + V` | Copy / paste |
| {kbd}`Shift + PageUp` / {kbd}`Shift + PageDown` | Scroll back / forward |
| {kbd}`Ctrl + Shift + R` | Search the scrollback |
| {kbd}`Ctrl + Shift + O` | Pick a link in the window to open |
| {kbd}`Ctrl + Shift + N` | New terminal window in the same directory |
| {kbd}`Ctrl + +` / {kbd}`Ctrl + -` / {kbd}`Ctrl + 0` | Bigger / smaller / reset font |

All bindings are listed in `man foot.ini` under `[key-bindings]`; override them there.

## Examples

```ini
# ~/.config/foot/foot.ini
[main]
font=JetBrainsMono Nerd Font:size=12      # larger font
initial-window-size-chars=120x32          # start size

[colors-dark]
alpha=1.0                                  # no transparency
```

Start it with `foot` or through the launcher ({kbd}`Super + Space`). The Hyprland default terminal is Kitty; to use Foot,
change `local terminal = "kitty"` in `~/.config/hypr/hyprland.lua`.

## Troubleshooting

- **Symbols show as boxes:** `fc-list | grep -i jetbrains` must list the Nerd Font variant; otherwise install `ttf-jetbrains-mono-nerd`.
- **Configuration errors:** `foot --check-config` prints the line and the reason.
- **No transparency:** `alpha` only works in `[colors-dark]` and needs a compositor.

## Colour palette (Catppuccin Mocha)

Every component uses the same colours so that terminal, launcher, file manager and dialogs match:

| Role | Colour | Used for |
| --- | --- | --- |
| Background | `#1e1e2e` | Windows, terminal |
| Darker background | `#181825` | Bars, lists, side panels |
| Surface | `#313244` | Inputs, buttons, selection |
| Text | `#cdd6f4` | Text |
| Accent | `#89b4fa` | Focus, borders, selection |
| Match | `#94e2d5` | Search matches |

## Customise and reset

`~/.config/foot` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/foot/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate foot` restores the
previous settings and `aco install foot` activates the package defaults again.
