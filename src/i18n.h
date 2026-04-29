/*
 * SilkTex — gettext shorthand
 * Copyright (C) 2026 Bela Georg Barthelmes
 * SPDX-License-Identifier: GPL-3.0-or-later
 */
#pragma once

#include <glib.h>

#ifndef _
#define _(String) g_dgettext(GETTEXT_PACKAGE, (String))
#endif

#ifndef N_
#define N_(String) (String)
#endif

#ifndef C_
#define C_(Context, String) g_dpgettext2(GETTEXT_PACKAGE, (Context), (String))
#endif
