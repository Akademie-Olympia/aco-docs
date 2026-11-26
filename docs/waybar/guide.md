# Waybar in daily use

Waybar is the slim, translucent bar at the top of the Hyprland session. It shows only what you need all the time and keeps
launching and switching on shortcuts and in the [Fuzzel](../fuzzel/index) launcher.

## Layout

```text
┌──────────────────────┬──────────┬───────────────────────────────────┐
│    Terminal         │  ━  •  •  │  󰤨  󰕾  󰂀 82%   26.11.  14:32  󰒓 │
└──────────────────────┴──────────┴───────────────────────────────────┘
  left                   centre     right
```

| Area | Module | Function |
| --- | --- | --- |
| Left | `custom/logo` | System menu (left click): settings, appearance, lock, log out, suspend, reboot, shut down; right click opens the launcher |
| Left | `hyprland/window` | Name of the focused app (`rewrite` maps classes such as `kitty` to "Terminal") |
| Centre | `hyprland/workspaces` | Dots per workspace, the active one stretches into an accent pill; mouse wheel switches |
| Right | `tray` | Tray icons of running apps |
| Right | `network` | Icon only, details in the tooltip; click opens `nmtui` |
| Right | `wireplumber` | Volume icon; click = mute, mouse wheel ±2 % (max. 100 %) |
| Right | `battery` | Charge, tooltip with remaining time and power |
| Right | `clock` | `DD.MM.  HH:MM`, calendar in the tooltip |
| Right | `custom/settings` | Settings hub (`~/.config/hypr/settings.sh`, also {kbd}`Super + I`); right click opens the appearance picker |

Height 32 px. The bar appears on **every** monitor; `all-outputs` is off, so each monitor shows its own workspaces.

### Battery states

From **25 %** the battery turns yellow (`warning`), from **12 %** red (`critical`); while charging or plugged in it is green.

## System menu

The logo opens a GTK menu from `power_menu.xml`; the actions live in `config.jsonc` (`menu-actions`):
`~/.config/hypr/settings.sh`, `aco-theme menu`, `hyprlock`, `hyprctl dispatch 'hl.dsp.exit()'` and `systemctl suspend|reboot|poweroff`.
The keyboard variant is `powermenu.sh` from the Hyprland package ({kbd}`Super + Esc`).
The bar therefore needs **Hyprland and Hyprlock** – see [Design and dependencies](design).

## Reload

After changing `config.jsonc` or `style.css`:

- {kbd}`Super + Shift + B` – sends Waybar `SIGUSR2` (reloads configuration and style); if that fails Waybar is restarted.
- In a terminal: `killall -SIGUSR2 waybar`

Configuration errors are printed when you start `waybar` from a terminal (`waybar -l debug`).

## Appearance (`style.css`)

Waybar uses GTK CSS. `style.css` holds only layout; font, colours and rounding come from the generated `~/.config/aco/theme/waybar/colors.css` (aco-theme).
Every module has a CSS id (`#custom-logo`, `#window`, `#workspaces button`, `#tray`, `#network`, `#wireplumber`, `#battery`,
`#clock`, `#custom-settings`); states are classes (`.active`, `.urgent`, `.muted`, `.charging`, `.warning`, `.critical`).

| Role | Theme token (`@define-color` in colors.css) |
| --- | --- |
| Bar background | `bar` = `bg_alt` at the surface opacity, blurred when transparency is on |
| Module hover | `hover` (text at 10 %) |
| Workspaces | dots in `pill`, the active one an `accent` pill, urgent `red` |
| States | muted/disconnected `muted`, charging `green`, warning `yellow`, critical `red` |
| Menus and tooltips | `menu` surface, `line` border, hovered item `accent` / `on_accent` |

## Add your own modules

The bar is intentionally small. Adding a module takes two steps – for example CPU load:

```javascript
// ~/.config/waybar/config.jsonc
"modules-right": [ "tray", "cpu", "network", "wireplumber", "battery", "clock", "custom/settings" ],

"cpu": { "format": "󰍛 {usage}%", "interval": 5 }
```

```css
/* ~/.config/waybar/style.css – reuse the theme colours, never hex values */
#cpu { margin: 4px 2px; padding: 0 9px; color: @subtext; }
```

The `network` module needs `networkmanager`, Bluetooth needs `bluez-utils` (both are optional dependencies of the package).
`man waybar-<module>` documents every module, for example `man waybar-network`.

## Troubleshooting

- **Bar missing:** does Hyprland start Waybar? `pgrep -x waybar`; otherwise {kbd}`Super + Shift + B`.
- **Symbols show as boxes:** `ttf-jetbrains-mono-nerd` is missing.
- **Volume has no effect:** `wpctl status` must show a default output (PipeWire/WirePlumber).
- **Battery missing:** `bat` does not match the device (see above); on desktop machines remove the module from `modules-right`.
- **Workspace list empty:** Waybar is running outside a Hyprland session (`HYPRLAND_INSTANCE_SIGNATURE` is missing).

## Customise and reset

`~/.config/waybar` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/waybar/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate waybar` restores the
previous settings and `aco install waybar` activates the package defaults again.
