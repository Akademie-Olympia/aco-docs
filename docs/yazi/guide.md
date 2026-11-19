# Yazi in daily use

Yazi is a fast terminal file manager with three columns (parent · current folder · preview). It is built for the keyboard but also
understands the mouse. In ACO you start it with {kbd}`Super + Y` or, in a terminal, with **`y`**.

## `y` instead of `yazi`

The Zsh command `y` (from the [Zsh package](https://aco-zsh.readthedocs.io/en/latest/)) starts Yazi and, when you quit with {kbd}`q`,
**changes into the folder you ended up in**. {kbd}`Q` quits without changing the directory. That makes Yazi a comfortable `cd`:
`y`, navigate with `h j k l`, `q`.

## Navigation and files

| Key | Action |
| --- | --- |
| {kbd}`h` / {kbd}`l` or {kbd}`←` / {kbd}`→` | Up a folder / enter (or open the file) |
| {kbd}`j` / {kbd}`k` or {kbd}`↓` / {kbd}`↑` | Move the selection |
| {kbd}`g` {kbd}`g` / {kbd}`G` | Top / bottom |
| {kbd}`Space` | Mark a file (then act on all marked files) |
| {kbd}`y` / {kbd}`x` / {kbd}`p` | Copy / cut / paste |
| {kbd}`d` / {kbd}`D` | Trash / delete permanently |
| {kbd}`a` | Create a file (trailing `/` = folder) |
| {kbd}`r` | Rename |
| {kbd}`.` | Toggle hidden files |
| {kbd}`/` / {kbd}`n` / {kbd}`N` | Search in the folder / next / previous match |
| {kbd}`z` | Find a file or folder with **fzf** |
| {kbd}`Z` | Jump to frequently used folders with **zoxide** |
| {kbd}`~` or {kbd}`F1` | Show all keys |
| {kbd}`q` | Quit |

The complete list is shown by Yazi itself with {kbd}`~`; it is always up to date.

## What this package sets

`yazi.toml`:

| Setting | Value | Effect |
| --- | --- | --- |
| `ratio` | `[1, 3, 4]` | Column widths: narrow parent, medium folder, wide preview |
| `sort_by` | `natural` | `file2` before `file10` |
| `sort_dir_first` | `true` | Folders first |
| `show_hidden` | `true` | Hidden files visible |
| `scrolloff` | `5` | Keep five lines of context when scrolling |
| `mouse_events` | click, scroll, touch, move, drag | Full mouse support |

`theme.toml` selects the `catppuccin-mocha` flavor (shipped in the package under `flavors/`). `package.toml` pins the flavor version
(Yazi package manager `ya pkg`) so everything stays reproducible.

## Previews and dependencies

The package installs what Yazi needs for previews and search: `file` (file type), `poppler` (PDF), `imagemagick` (images), `ffmpeg` (video),
`7zip` (archives), `fd`/`ripgrep`/`fzf` (search), `zoxide` (folder jumps) and `jq`. If one is missing only the matching preview or search feature is missing.

## Typical changes

```toml
# ~/.config/yazi/yazi.toml
[mgr]
show_hidden = false     # hidden files only with '.'
ratio = [ 1, 2, 3 ]     # wider folder, narrower preview
```

Custom keys belong in a new `keymap.toml` in the same folder.

## Troubleshooting

- **No image preview:** the terminal must support an image protocol – Kitty and Ghostty do, Foot only to a limited extent.
- **`y` does not change the folder:** you started `yazi` directly or are in a shell without the ACO Zsh configuration.
- **Flavor missing:** `ya pkg install` restores the packages pinned in `package.toml`.

## Customise and reset

`~/.config/yazi` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/yazi/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate yazi` restores the
previous settings and `aco install yazi` activates the package defaults again.
