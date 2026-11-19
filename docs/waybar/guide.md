# Waybar in daily use

Waybar is the slim bar at the top of the Hyprland session. It shows only what you need all the time – workspace, clock, volume, battery – and
offers a power menu. Everything else (launching programs, switching windows, choosing a wallpaper) is deliberately **not** in the bar but on
shortcuts and in the [Fuzzel](../fuzzel/index) menu.

## Layout

```text
┌───────────────┬──────────────────────┬─────────────────────────────┐
│ 1 2 3 4 5 …   │  14:32  ·  19.11.2026 │  󰕾 65%    󰂀 82%    󰐥      │
└───────────────┴──────────────────────┴─────────────────────────────┘
  left             centre                 right
```

| Area | Module | Function |
| --- | --- | --- |
| Left | `hyprland/workspaces` | Workspaces of the monitor; mouse wheel switches, the active one is underlined blue, urgent ones red |
| Centre | `clock` | `HH:MM · DD.MM.YYYY`, calendar in the tooltip (hover) |
| Right | `wireplumber` | Volume; click = mute, mouse wheel ±2 % (max. 100 %) |
| Right | `battery` | Charge with icons, tooltip with remaining time and power in watts |
| Right | `custom/power` | Power menu (see below) |

Height 26 px, at the top, no gap to the edge. The bar appears on **every** monitor; `all-outputs` is off, so each monitor shows its own workspaces.

### Battery states

`battery` uses `BAT0` and `AC`. From **25 %** the display turns orange (`warning`), from **12 %** red (`critical`); while charging or plugged in it is
green. If your device has a different battery name (`ls /sys/class/power_supply`), change `"bat"` in `config.jsonc`.

## Power menu

The `󰐥` icon on the right offers two ways:

1. **Left click** – a GTK menu from `power_menu.xml` right under the bar: shutdown, reboot, suspend, lock, log out.
2. **Right click** – the Fuzzel menu `powermenu.sh` from the Hyprland package (also on {kbd}`Super + Esc`), keyboard only.

The actions are `systemctl poweroff|reboot|suspend`, `hyprlock` and `hyprctl dispatch 'hl.dsp.exit()'`.
The bar therefore needs **Hyprland and Hyprlock** – see [Design and dependencies](design).

## Reload

After changing `config.jsonc` or `style.css`:

- {kbd}`Super + Shift + B` – sends Waybar `SIGUSR2` (reloads configuration and style); if that fails Waybar is restarted.
- In a terminal: `killall -SIGUSR2 waybar`

Configuration errors are printed when you start `waybar` from a terminal (`waybar -l debug`).

## Appearance (`style.css`)

Waybar uses GTK CSS. The file sets the font (JetBrainsMono Nerd Font, 12 px), Catppuccin Mocha colours and square corners (`border-radius: 0`).
Every module has a CSS id (`#clock`, `#battery`, `#wireplumber`, `#custom-power`, `#workspaces button`); states are classes
(`.active`, `.urgent`, `.muted`, `.charging`, `.warning`, `.critical`).

| Role | Colour |
| --- | --- |
| Bar background | `#1e1e2e` |
| Module surface | `#181825` with `#313244` as separator |
| Volume | `#74c7ec` (Sapphire), muted `#6c7086` |
| Battery | `#94e2d5` (Teal), charging `#a6e3a1`, warning `#fab387`, critical `#f38ba8` |
| Active workspace | `#89b4fa` |

## Add your own modules

The bar is intentionally small. Adding a module takes two steps – for example network or window title:

```javascript
// ~/.config/waybar/config.jsonc
"modules-left":  [ "hyprland/workspaces", "hyprland/window" ],
"modules-right": [ "network", "wireplumber", "battery", "custom/power" ],

"hyprland/window": { "max-length": 50 },
"network": {
    "format-wifi": "󰤨 {essid}",
    "format-ethernet": "󰈀 {ipaddr}",
    "format-disconnected": "󰤭",
    "on-click": "kitty -e nmtui"
}
```

```css
/* ~/.config/waybar/style.css */
#network { padding: 0 10px; background-color: #181825; color: #94e2d5; border-left: 1px solid #313244; }
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
