# Waybar in daily use

Waybar is the slim top bar of the Hyprland session. With transparency on it has no background and floats over the
wallpaper; with transparency off it is a solid strip. It shows only what you need all the time and keeps launching and
switching on shortcuts and in the rofi launcher (`aco-menu`, {kbd}`Super + Space`).

## Layout

```text
  ●  ○  ○  ○  ○   Terminal                        󰤨  󰕾  󰂀 82%   Thu 26. Nov  14:32  󰂚
  left                                             right
```

| Area | Module | Function |
| --- | --- | --- |
| Left | `hyprland/workspaces` | One circle per workspace of this monitor; the one on screen is filled (accent on the focused monitor, grey on the others), circles with windows are drawn stronger. Click switches, the mouse wheel steps through the monitor's workspaces |
| Left | `hyprland/window` | Name of the focused app (`rewrite` maps classes such as `kitty` to "Terminal") |
| Right | `tray` | Tray icons of running apps |
| Right | `privacy` | Orange icon while the microphone or screen sharing is in use; hidden otherwise |
| Right | `bluetooth` | Only visible while a device is connected; click opens *Einstellungen > Bluetooth* |
| Right | `network` | Icon only, details in the tooltip; click opens *Einstellungen > WLAN & Netzwerk* |
| Right | `wireplumber` | Volume icon; click = mute, right click opens *Einstellungen > Ton*, mouse wheel ±2 % (max. 100 %) |
| Right | `backlight` | Laptops only: brightness icon, mouse wheel changes the brightness |
| Right | `battery` | Charge, tooltip with remaining time and power; click opens *Einstellungen > Energie* |
| Right | `clock` | Weekday, date and time in the system language, calendar in the tooltip; click opens the control centre |
| Right | `custom/control-centre` | From `swaync-client -swb`: accent while notifications wait, crossed out with *Nicht stören*; click opens the control centre ({kbd}`Super + U`), right click toggles *Nicht stören* |

Height 32 px. The bar appears on **every** monitor and each one shows its own workspaces. How workspaces are grouped per
monitor and the "all monitors at once" mode are part of aco-hypr (`workspaces.lua`, *Einstellungen > Bildschirme*).

### Battery states

From **25 %** the battery turns yellow (`warning`), from **12 %** red (`critical`); while charging or plugged in it is green.

## Control centre instead of a system menu

Lock, settings and power off are tiles in the control centre (aco-swaync), next to quick toggles for WLAN, Bluetooth,
*Nicht stören*, microphone, dark mode and transparency. The keyboard variants are {kbd}`Super + L`, {kbd}`Super + I`
and {kbd}`Super + Esc` (`powermenu.sh`).

## Reload

After changing `config.jsonc` or `style.css`:

- {kbd}`Super + Shift + B` – sends Waybar `SIGUSR2` (reloads configuration and style); if that fails Waybar is restarted.
- In a terminal: `killall -SIGUSR2 waybar`

Configuration errors are printed when you start `waybar` from a terminal (`waybar -l debug`).

## Appearance (`style.css`)

Waybar uses GTK CSS. `style.css` holds only layout; font, colours and rounding come from the generated `~/.config/aco/theme/waybar/colors.css` (aco-theme).
Every module has a CSS id (`#workspaces button`, `#window`, `#tray`, `#privacy`, `#bluetooth`, `#network`, `#wireplumber`,
`#backlight`, `#battery`, `#clock`, `#custom-control-centre`); states are classes (`.active`, `.visible`, `.empty`,
`.urgent`, `.muted`, `.charging`, `.warning`, `.critical`).

| Role | Theme token (`@define-color` in colors.css) |
| --- | --- |
| Bar background | `bar` = `bg_alt` at `bar_alpha` (0 with transparency on, 1 with it off) |
| Module hover | `hover` (text at 10 %) |
| Workspaces | rings in `ring`, with windows `subtext`, on screen filled `subtext`, focused filled `accent`, urgent `red` |
| States | muted/disconnected `muted`, charging `green`, warning `yellow`, critical `red` |
| Menus and tooltips | `menu` surface, `line` border, hovered item `accent` / `on_accent` |

## Add your own modules

The bar is intentionally small. Adding a module takes two steps – for example CPU load:

```javascript
// ~/.config/waybar/config.jsonc
"modules-right": [ "tray", "cpu", "network", "wireplumber", "battery", "clock", "custom/control-centre" ],

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
- **No circles:** Waybar is running outside a Hyprland session (`HYPRLAND_INSTANCE_SIGNATURE` is missing), or
  `workspaces.lua` from aco-hypr is not loaded (`hyprctl configerrors`).

## Customise and reset

`~/.config/waybar` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/waybar/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate waybar` restores the
previous settings and `aco install waybar` activates the package defaults again.
