# SilkTex - Modern LaTeX Editor
# Copyright (C) 2026 Bela Georg Barthelmes
# SPDX-License-Identifier: GPL-3.0-or-later

app_id = 'app.silktex.SilkTex'

install_data(
    'Silktex.svg',
    install_dir: join_paths(icondir, 'scalable/apps/'),
    rename: app_id + '.svg',
)

# Theme icon used by the in-app Git menu button. Installing it into the
# hicolor actions context ensures gtk_icon_theme_has_icon("git-symbolic")
# succeeds in Flatpak runtimes even if resources are not loaded yet.
install_data(
    'git-symbolic.svg',
    install_dir: join_paths(icondir, 'scalable/actions/'),
)

# A copy inside the app's private data dir so the code can find it even
# when no icon theme is available (e.g. inside the Flatpak sandbox).
install_data('Silktex.svg', install_dir: join_paths(pkgdatadir, 'icons'))
