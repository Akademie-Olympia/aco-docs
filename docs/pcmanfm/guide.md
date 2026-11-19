# PCManFM – graphical file manager

PCManFM is the fast, lean file manager for mouse work: mount drives, drag files, look at thumbnails. It complements
[Yazi](../yazi/index), the terminal file manager.

| Task | Tool |
| --- | --- |
| Navigate fast, type paths, batch rename | Yazi ({kbd}`Super + Y`) |
| Drives, drag & drop, thumbnails | PCManFM ({kbd}`Super + E`) |

## How the packages fit together

- **`aco-arch-dotfiles-pcmanfm`** – window behaviour (this page).
- **[libfm](../libfm/index)** – trash, terminal, icon sizes, side panel.
- **[GTK 3](../gtk3/index)** – colours and font.
- **`gvfs` and `udisks2`** – required for mounting and unmounting drives; the package depends on them.

All of them are dependencies; `pacman -S aco-arch-dotfiles-pcmanfm` pulls them in.

## What this package sets (`default/pcmanfm.conf`)

| Key | Value | Effect |
| --- | --- | --- |
| `maximized` | `1` | Starts maximised (Hyprland tiles anyway) |
| `view_mode` | `icon` | Icon view; `list`, `compact`, `thumbnail` are possible |
| `show_hidden` | `0` | Hidden files off ({kbd}`Ctrl + H` toggles) |
| `sort` | `name;ascending;` | By name, ascending |
| `side_pane_mode` | `places` | Places on the left; alternatively `dirtree` |
| `toolbar` | `newtab;navigation;home;` | Tab, back/forward/up, home |
| `show_statusbar` | `1` | Status line with item count and size |
| `always_show_tabs` | `0` | Tab bar only with more than one tab |
| `mount_on_startup` / `mount_removable` / `autorun` | `1` | Mount drives automatically |
| `close_on_unmount` | `1` | The window closes when its drive is unmounted |

## Usage

| Key | Action |
| --- | --- |
| {kbd}`Ctrl + T` / {kbd}`Ctrl + W` | New / close tab |
| {kbd}`Alt + ←` / {kbd}`Alt + →` / {kbd}`Alt + ↑` | Back / forward / up |
| {kbd}`Ctrl + L` | Type an address |
| {kbd}`F2` | Rename |
| {kbd}`Ctrl + H` | Toggle hidden files |
| {kbd}`Del` / {kbd}`Shift + Del` | Trash / delete permanently |
| {kbd}`F4` | Terminal in the current folder |

## Typical changes

```ini
# ~/.config/pcmanfm/default/pcmanfm.conf
view_mode=list        # list view instead of icons
show_hidden=1         # always show hidden files
side_pane_mode=dirtree
```

## Troubleshooting

- **A drive does not appear:** `gvfs` and `udisks2` must be installed and running; without them PCManFM cannot mount anything.
- **Window size is wrong:** under Hyprland tiling decides; `win_width`/`win_height` only apply to floating windows.
- **Light instead of dark:** check [GTK 3](../gtk3/index).

## Customise and reset

`~/.config/pcmanfm` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/pcmanfm/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate pcmanfm` restores the
previous settings and `aco install pcmanfm` activates the package defaults again.
