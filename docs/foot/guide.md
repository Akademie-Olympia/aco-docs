# Foot in daily use

Foot is a Wayland-only terminal: it starts in milliseconds, uses very little memory and has no tabs or splits. That is
deliberate – window layout is the job of Hyprland and [tmux](https://aco-tmux.readthedocs.io/en/latest/). Foot is the **lightweight
alternative** next to Kitty and Ghostty, handy for quick tasks, older hardware or as a server terminal (`footclient`).

## What this package sets

| Setting | Value | Effect |
| --- | --- | --- |
| `shell` | `/usr/bin/zsh` | Starts the ACO Zsh configuration directly |
| `font` | aco-theme: JetBrainsMonoNL Nerd Font, 10.5 pt | Same font as Kitty and Ghostty, no ligatures; Nerd symbols |
| `pad` | `10x10` | Inner padding so text does not touch the window edge |
| `[bell]` | off | No beep or notification on `\a` |
| `[cursor]` | beam | |
| `alpha` | aco-theme: 0.94, 1 with transparency off | Slightly transparent background |
| Colours | aco-theme | 16 terminal colours plus selection and cursor, light or dark |

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
initial-window-size-chars=120x32          # start size
```

Font size and transparency are theme tokens shared with the other terminals:
`mono_size = 12` in `~/.config/aco/theme.local.conf`, or `aco-theme transparency off`; new foot windows pick them up.

Start it with `foot` or through the launcher ({kbd}`Super + Space`). The Hyprland default terminal is Kitty; to use Foot,
change `local terminal = "kitty"` in `~/.config/hypr/hyprland.lua`.

## Troubleshooting

- **Symbols show as boxes:** `fc-list | grep -i jetbrains` must list the Nerd Font variant; otherwise install `ttf-jetbrains-mono-nerd`.
- **Configuration errors:** `foot --check-config` prints the line and the reason.
- **No transparency:** `alpha` only works in `[colors-dark]` and needs a compositor.

## Colours

Colours come from the shared ACO theme and follow `aco-theme mode|accent|transparency`. The template is `aco-theme/theme.ini.tpl` in this component; the palette is documented in [aco-theme](https://github.com/Akademie-Olympia/aco-theme).

## Customise and reset

`~/.config/foot` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/foot/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate foot` restores the
previous settings and `aco install foot` activates the package defaults again.
