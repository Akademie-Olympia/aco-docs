# GTK 4 – modern applications

GTK 4 (with libadwaita) draws newer GNOME programs and many portal dialogs. This package colours them in the desktop palette.

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

## The difference to GTK 3

GTK 4 and libadwaita use **their own named colours** (`window_bg_color`, `headerbar_bg_color`, `accent_bg_color` …) and largely ignore
`gtk-theme-name`. That is why `gtk.css` is short here: it only redefines those colours and leaves program layouts alone.

| Colour | Value | Purpose |
| --- | --- | --- |
| `window_bg_color` | `#1e1e2e` | Window background |
| `view_bg_color` | `#181825` | Lists, text fields |
| `headerbar_bg_color` | `#181825` | Header bar |
| `card_bg_color` | `#313244` | Cards, groups |
| `popover_bg_color` | `#1e1e2e` | Menus, popups |
| `accent_bg_color` | `#89b4fa` | Highlights, switches |

Current programs also receive the dark preference through the portal; windows that stay light can be checked with
`gsettings get org.gnome.desktop.interface color-scheme` (expected: `prefer-dark`).

## Customise

```css
/* ~/.config/gtk-4.0/gtk.css */
@define-color accent_bg_color #cba6f7;   /* mauve accent */
@define-color accent_color #cba6f7;
```

Restart the application; `GTK_DEBUG=interactive <program>` helps with testing.

## Troubleshooting

- **Nothing changes:** a Flatpak program does not see `~/.config/gtk-4.0` automatically.
- **Too little contrast:** `accent_fg_color` (text on accent) must suit the accent colour you chose.
- **Older programs:** [GTK 3](../gtk3/index).

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

`~/.config/gtk-4.0` is a link to your editable copy in
`~/.local/share/arch-dotfiles/config/gtk-4.0/`. Change anything there; `pacman -Syu` does **not** overwrite your
edits. When an update ships new defaults they appear as a `.pacnew` file next to yours and you merge what you want
(`aco sync` merges, `aco status` shows the state). To go back to the shipped defaults, `aco deactivate gtk-4.0` restores the
previous settings and `aco install gtk-4.0` activates the package defaults again.
