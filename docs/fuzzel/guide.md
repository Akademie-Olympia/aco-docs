# Fuzzel as the shared menu

Fuzzel is the application launcher of ACO – and more: it is the **common menu** of almost every script in the environment.
With `--dmenu` it shows any list a script gives it, with type-to-search, arrow keys and Enter. That is why every selection menu
on the system looks and behaves the same.

## Where Fuzzel is used

| Call | Key | Purpose |
| --- | --- | --- |
| `fuzzel` | {kbd}`Super + Space`, {kbd}`Alt + Space`, {kbd}`Super + D` | Launch programs |
| `windowswitcher.sh` | {kbd}`Super + G` | Windows across all monitors and workspaces |
| `powermenu.sh` | {kbd}`Super + Esc` | Lock, log out, suspend, reboot, shut down |
| `settings.sh` | {kbd}`Super + I` | Settings hub: appearance, wallpaper, displays, network … |
| `settings.sh appearance` | {kbd}`Super + I` > Erscheinungsbild, or the control centre tiles ({kbd}`Super + U`) | Light/dark, transparency, accent, theme |
| `wallpaper.sh tui` | {kbd}`Super + Shift + W` | Choose a wallpaper |
| `monitors.sh menu` | {kbd}`Super + Shift + D` | Monitor layout |
| `aco keys --menu` | {kbd}`Super + K` | Search every shortcut |

Pressing the key again closes the menu (`pkill -x fuzzel`).

## Using it

Just type – the search matches name, description, category and command
(`fields=name,generic,comment,categories,keywords,filename`).
{kbd}`↑`/{kbd}`↓` or {kbd}`Ctrl + P`/{kbd}`Ctrl + N` move, {kbd}`Enter` runs, {kbd}`Esc` cancels. The menu also closes when it loses focus.

## What this package sets

| Setting | Value | Effect |
| --- | --- | --- |
| `terminal` | `kitty -e` | Programs flagged “run in terminal” open in Kitty |
| `anchor` / `width` / `lines` | centre / 40 / 7 | Spotlight-like search window in the middle of the screen |
| `line-height` / paddings | 34 px, 16/14/10 | Large, calm rows |
| `layer` | `overlay` | Appears above fullscreen windows |
| `icons-enabled` | on (Adwaita) | Application icons |
| Font, colours, border | aco-theme | `~/.config/aco/theme/fuzzel/theme.ini`: UI font 13 pt, translucent surface, accent selection, rounded corners |

## Build your own menus

```bash
choice=$(printf 'One\nTwo\nThree\n' | fuzzel --dmenu --prompt 'Pick: ')
echo "$choice"
```

Useful options: `--lines N`, `--width N`, `--anchor top-right`, `--hide-prompt`, `--index` (prints the number instead of the text).
`settings.sh` in the Hyprland package is an example of a menu built from a list of label/command pairs.

## Troubleshooting

- **No change after editing?** Fuzzel re-reads the file on every start; syntax errors are printed in the terminal.
- **Icons missing:** the `adwaita-icon-theme` package must be installed.
- **No symbols in the font:** `ttf-jetbrains-mono-nerd` is missing.

## Colours

Colours come from the shared ACO theme and follow `aco-theme mode|accent|transparency`. The template is `aco-theme/theme.ini.tpl` in this component; the palette is documented in [aco-theme](https://github.com/Akademie-Olympia/aco-theme).

## Customise and reset

`~/.config/fuzzel` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/fuzzel/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate fuzzel` restores the
previous settings and `aco install fuzzel` activates the package defaults again.
