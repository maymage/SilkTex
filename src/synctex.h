/*
 * SilkTex - SyncTeX forward/inverse sync helpers
 * Copyright (C) 2026 Bela Georg Barthelmes
 * SPDX-License-Identifier: GPL-3.0-or-later
 */
#pragma once
#include <glib-object.h>
#include "editor.h"
#include "preview.h"

G_BEGIN_DECLS

gboolean silktex_synctex_forward(SilktexEditor *editor, SilktexPreview *preview,
                                 const char *pdf_path);
gboolean silktex_synctex_inverse(SilktexEditor *editor, const char *pdf_path, int page, double x,
                                 double y);

G_END_DECLS
