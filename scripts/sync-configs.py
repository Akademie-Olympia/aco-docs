#!/usr/bin/env python3
"""Copy the shipped configuration files of the small components into docs/_configs/.

    python3 scripts/sync-configs.py [--root DIR] [--check]

The configuration pages include these copies with ``literalinclude``, so the
documentation always shows what the packages really ship. Component repositories
are looked up next to this repository (the layout created by
aco-arch-dotfiles/scripts/clone-repos.sh). With --check nothing is written and the
exit status is 1 when a copy is out of date.
"""
import argparse
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent.parent
TARGET = HERE / "docs" / "_configs"
COMPONENTS = {  # page directory -> (repository, files)
    "foot": ("aco-foot", ["foot.ini"]),
    "fuzzel": ("aco-fuzzel", ["fuzzel.ini"]),
    "gtk3": ("aco-gtk3", ["settings.ini", "gtk.css"]),
    "gtk4": ("aco-gtk4", ["settings.ini", "gtk.css"]),
    "libfm": ("aco-libfm", ["libfm.conf"]),
    "pcmanfm": ("aco-pcmanfm", ["default/pcmanfm.conf"]),
    "wallpaper": ("aco-wallpaper", ["wallpaper.conf"]),
    "waybar": ("aco-waybar", ["config.jsonc", "style.css"]),
    "yazi": ("aco-yazi", ["yazi.toml", "theme.toml", "package.toml"]),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=HERE.parent)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for page, (repository, files) in COMPONENTS.items():
        for name in files:
            source = args.root / repository / name
            if not source.is_file():
                print(f"missing: {source}", file=sys.stderr)
                return 2
            target = TARGET / page / name
            if target.exists() and target.read_bytes() == source.read_bytes():
                continue
            stale.append(f"{page}/{name}")
            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(source.read_bytes())
    for item in stale:
        print(("outdated: " if args.check else "updated: ") + item)
    return 1 if args.check and stale else 0


if __name__ == "__main__":
    sys.exit(main())
