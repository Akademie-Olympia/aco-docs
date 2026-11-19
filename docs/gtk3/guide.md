# GTK 3 – dialogs, menus, PCManFM

GTK 3 draws PCManFM, file dialogs (“Open/Save”), Firefox menus and many older programs. This package makes them appear dark and in the
colours of the desktop.

## How the files work together

GTK reads two files when an application starts:

- `settings.ini` – **behaviour**: prefer the dark theme, icon set, font, cursor, animations.
- `gtk.css` – **appearance**: overrides the theme's colours and borders with the Catppuccin Mocha palette.

The theme stays `Adwaita-dark`; `gtk.css` recolours it. Layout and widgets stay familiar, only the colours match the rest of the desktop.

| Setting (`settings.ini`) | Value | Effect |
| --- | --- | --- |
| `gtk-application-prefer-dark-theme` | `1` | Prefer the dark variant |
| `gtk-theme-name` | `Adwaita-dark` | Base theme |
| `gtk-icon-theme-name` | `Adwaita` | Icons (`adwaita-icon-theme`) |
| `gtk-font-name` | JetBrainsMonoNL Nerd Font 10 | Font of all dialogs and menus |
| `gtk-cursor-theme-name` / `-size` | Adwaita / 20 | Matches `XCURSOR_SIZE` in Hyprland |
| `gtk-enable-animations` | `0` | No animations – feels faster |

## What `gtk.css` covers

The file recolours the named theme colours (`theme_bg_color`, `theme_selected_bg_color`, `borders`, `warning_color` …) and then overrides
specific widgets: windows, header bars, entries (focus = accent border), buttons (hover = accent), tabs, lists, side panels, menus, status bar
and scrollbars. All corners are square (`border-radius: 0`) so GTK windows match Waybar and the terminal.

## Customise

A different accent, for example green instead of blue:

```css
/* ~/.config/gtk-3.0/gtk.css – replace #89b4fa with #a6e3a1 */
@define-color theme_selected_bg_color #a6e3a1;
```

Restart the affected program to see the change. GTK reports CSS errors in the terminal when you start the program from there
(`GTK_DEBUG=interactive pcmanfm` opens the GTK inspector).

## Troubleshooting

- **A program stays light:** it uses its own theming (for example Electron). Check `gsettings get org.gnome.desktop.interface color-scheme`.
- **Wrong icons:** install `adwaita-icon-theme`; the package depends on it.
- **GTK 4 programs:** see [GTK 4](../gtk4/index).

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

`~/.config/gtk-3.0` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/gtk-3.0/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate gtk-3.0` restores the
previous settings and `aco install gtk-3.0` activates the package defaults again.
