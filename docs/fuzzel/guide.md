# Fuzzel as the shared menu

Fuzzel is the application launcher of ACO – and more: it is the **common menu** of almost every script in the environment.
With `--dmenu` it shows any list a script gives it, with type-to-search, arrow keys and Enter. That is why every selection menu
on the system looks and behaves the same.

## Where Fuzzel is used

| Call | Key | Purpose |
| --- | --- | --- |
| `fuzzel` | {kbd}`Super + Space`, {kbd}`Alt + Space`, {kbd}`Super + D` | Launch programs |
| `windowswitcher.sh` | {kbd}`Super + G` | Windows across all monitors and workspaces |
| `powermenu.sh` | {kbd}`Super + Esc` | Shutdown, reboot, suspend, lock |
| `wallpaper.sh tui` | {kbd}`Super + Shift + W` | Choose a wallpaper |
| `monitors.sh menu` | {kbd}`Super + Shift + D` | Monitor layout |
| `aco keys --menu` | {kbd}`Super + K` | Search every shortcut |

Pressing the key again closes the menu (`pkill -x fuzzel`).

## Using it

Just type – the search matches name, description, category and command
(`fields=name,generic,comment,categories,keywords,exec,filename`).
{kbd}`↑`/{kbd}`↓` or {kbd}`Ctrl + P`/{kbd}`Ctrl + N` move, {kbd}`Enter` runs, {kbd}`Esc` cancels. The menu also closes when it loses focus.

## What this package sets

| Setting | Value | Effect |
| --- | --- | --- |
| `terminal` | `kitty -e` | Programs flagged “run in terminal” open in Kitty |
| `width` / `lines` | 44 / 10 | Width in characters, visible rows |
| `layer` | `overlay` | Appears above fullscreen windows |
| `match-counter` | on | Shows the number of matches |
| `icons-enabled` | on (Adwaita) | Application icons |
| `border` | 1 px, accent colour | `radius=0` – square, matching Waybar and the terminals |

## Build your own menus

```bash
choice=$(printf 'One\nTwo\nThree\n' | fuzzel --dmenu --prompt 'Pick: ')
echo "$choice"
```

Useful options: `--lines N`, `--width N`, `--anchor top-right`, `--hide-prompt`, `--index` (prints the number instead of the text).
`powermenu.sh` in the Hyprland package is an example of a menu with its own position.

## Troubleshooting

- **No change after editing?** Fuzzel re-reads the file on every start; syntax errors are printed in the terminal.
- **Icons missing:** the `adwaita-icon-theme` package must be installed.
- **No symbols in the font:** `ttf-jetbrains-mono-nerd` is missing.

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

`~/.config/fuzzel` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/fuzzel/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate fuzzel` restores the
previous settings and `aco install fuzzel` activates the package defaults again.
