/*
 * SilkTex - Document outline sidebar
 * Copyright (C) 2026 Bela Georg Barthelmes
 * SPDX-License-Identifier: GPL-3.0-or-later
 */
#pragma once

#include <gtk/gtk.h>
#include "editor.h"

G_BEGIN_DECLS

#define SILKTEX_TYPE_STRUCTURE (silktex_structure_get_type())
G_DECLARE_FINAL_TYPE(SilktexStructure, silktex_structure, SILKTEX, STRUCTURE, GtkWidget)

SilktexStructure *silktex_structure_new(void);

/* Sets the editor the outline should reflect.  Automatically triggers a refresh
 * and subscribes to the editor's `changed` signal. */
void silktex_structure_set_editor(SilktexStructure *self, SilktexEditor *editor);

void silktex_structure_refresh(SilktexStructure *self);

G_END_DECLS
