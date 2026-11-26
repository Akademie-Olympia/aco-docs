# Wallpaper in daily use

The package consists of one command – `wallpaper` (short: `wp`) – and a configuration file. The command draws the images with
**swaybg** (one small process per monitor, shared memory, works on every GPU and in VMs) and remembers which image applies to which
monitor. Without an own choice the default is the **generated ACO background**: licence-free, made from the theme palette, light or
dark with the accent.

## How it fits together

```text
wallpaper  ──reads──►   wallpaper.conf (folders, fit)
    │      ──stores──►  ~/.local/state/wallpaper/state (default + overrides)
    ├──swaybg -o MON -i …───►  swaybg  (draws the image; new instance first, then the old one ends)
    ├──hyprctl monitors -j──►  which monitors exist (evaluated with jq)
    ├──rsvg-convert─────────►  ~/.cache/aco/wallpaper/generated/aco.png (from aco-theme's aco.svg)
    └──aco-menu --grid──────►  preview grid (Super + Shift + W, Einstellungen > Hintergrundbild)
```

- **Generated background:** aco-theme renders `aco-theme/aco.svg.tpl`; `wallpaper` converts it at the size of the largest monitor
  whenever the theme or the monitor changes. A theme switch re-applies the assignment, so it updates only this image – an image you
  chose stays.
- **Own images:** put them into `~/Pictures/Wallpapers` (or add a folder with `wallpaper dirs add`) and pick them in the grid.
  Previews are cached in `~/.cache/aco/wallpaper/thumbnails`.
- The **state** lives in `~/.local/state/wallpaper/state`, outside the configuration. A package update never overwrites it.
- On **Hyprland start** (`wallpaper apply --quiet`) and when a **monitor is plugged in** (`monitor.added` event) Hyprland restores the remembered
  assignment. The [monitor tool](https://aco-hypr.readthedocs.io/en/latest/configuration/) also calls `wallpaper apply` after a layout change.

## Default and overrides

- **Default** – the image for all monitors without their own setting. New, unknown monitors get it too.
- **Override** – an own image for a specific monitor (for example a portrait second screen).

In `wallpaper list` ★ marks the default and ● the overrides. `wallpaper current` shows the current assignment per monitor.

## Commands

| Command | Effect |
| --- | --- |
| `wallpaper` | Selection menu: the target (only with several monitors), then a preview grid with *Zufällig* and *Darstellung* |
| `wallpaper list` | All images found |
| `wallpaper current` | Assignment per monitor |
| `wallpaper set <image>` | Set the default |
| `wallpaper set <image> --monitor DP-1` | Override for one monitor |
| `wallpaper set <image> --all` | Same image everywhere, delete overrides |
| `wallpaper default <image>` | Change only the default |
| `wallpaper monitor DP-1 <image\|default>` | Set or remove an override |
| `wallpaper clear DP-1` / `clear --all` | Delete override(s) |
| `wallpaper next` / `prev` / `random` | Cycle through images |
| `wallpaper add <file> [--set] [--move]` | Add an image to the library |
| `wallpaper fit [cover\|contain\|tile\|fill\|default] [--monitor DP-1]` | Show or set the display mode, globally or for one monitor |
| `wallpaper dirs` | Folders that are searched |
| `wallpaper dirs add <folder>` / `dirs remove <folder>` | Add or drop an extra image folder (only the list changes, nothing is deleted) |
| `wallpaper apply [--quiet]` | Re-apply the remembered assignment |
| `wallpaper reload` | Restart swaybg and apply the assignment |
| `wallpaper doctor` | Check dependencies (`hyprctl`, `swaybg`, `rsvg-convert`, `magick`, `jq`, `aco-menu`) and setup |

`<image>` is a file name from the library or a path. Names must be unambiguous; otherwise use the path.

## Configuration (`wallpaper.conf`)

| Variable | Default | Effect |
| --- | --- | --- |
| `WALLPAPER_DIRS` | `~/.local/share/arch-dotfiles/config/pictures`, `~/Pictures/Wallpapers`, `/usr/share/hypr/wall*.png` | Folders (recursive) and file patterns that are searched; the generated ACO background is always listed first |
| `WALLPAPER_FIT` | `cover` | `cover` fills and crops, `contain` shows everything with borders, `tile` tiles, `fill` stretches |
| `WALLPAPER_NOTIFY` | `1` | Notification after switching (`0` = off) |

### Customising per monitor

Beyond the default/override image, how an image is **fitted** can be set per monitor – useful when one screen is a different shape:

```bash
wallpaper fit                          # show the effective mode of every monitor
wallpaper fit contain                  # all monitors
wallpaper fit tile --monitor HDMI-A-1  # only this one
wallpaper fit default --monitor HDMI-A-1   # remove the override
wallpaper fit default                  # remove every customisation (back to wallpaper.conf)
```

The effective mode is: monitor override → global setting → `WALLPAPER_FIT` from `wallpaper.conf`. The same choices are available in the menu
({kbd}`Super + Shift + W` → “Change display mode”). Extra folders added with `wallpaper dirs add` and the fit settings are stored in the state file
`~/.local/state/wallpaper/state`, so `wallpaper.conf` stays exactly as the package ships it and never produces a `.pacnew` for your tweaks.

Drop new images into one of the folders – they show up in the menu and list immediately. The file is a Bash script that gets sourced, so keep it
free of commands other than variable assignments.

:::{note}
**Images are not part of the package.** For copyright reasons `aco-arch-dotfiles-wallpaper` ships only the tool. Your images live in
`~/Pictures/Wallpapers` or the library folder and should be backed up separately.
:::

## Keys

| Key | Action |
| --- | --- |
| {kbd}`Super + Shift + W` | Open the selection menu (a second press closes it) |

## Troubleshooting

- **“swaybg nicht aktiv”:** `wallpaper current` shows it; `wallpaper reload` starts swaybg again. Run it inside the Hyprland session (it needs `WAYLAND_DISPLAY`).
- **“hyprctl not found”:** the command only works inside a Hyprland session.
- **A new monitor stays black:** wait a moment (Hyprland applies the assignment with a one to two second delay) or run `wallpaper apply`.
- **Image not found:** check `wallpaper dirs` and `wallpaper list`; recognised formats are png, jpg, jpeg, webp, gif, bmp, avif, jxl and tif/tiff.
- **Blurry or cropped:** `WALLPAPER_FIT=contain` shows the whole image.

## Customise and reset

`~/.config/wallpaper` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/wallpaper/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate wallpaper` restores the
previous settings and `aco install wallpaper` activates the package defaults again.
