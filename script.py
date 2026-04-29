import re

with open('data/ui/main.blp', 'r') as f:
    content = f.read()

# 1. Extract editor_bottom_bar
editor_bottom_bar_match = re.search(r'  \[bottom\]\n  Gtk\.Box editor_bottom_bar \{.*?\n    \} \n  \}\n\}', content, re.DOTALL)
if not editor_bottom_bar_match:
    print("Could not find editor_bottom_bar")
    exit(1)
editor_bottom_bar_content = editor_bottom_bar_match.group(0)
content = content.replace(editor_bottom_bar_content, '')

# 2. Extract preview_toolbar
preview_toolbar_match = re.search(r'            \[bottom\]\n            Gtk\.CenterBox preview_toolbar \{.*?\n              \}\n            \}\n', content, re.DOTALL)
if not preview_toolbar_match:
    print("Could not find preview_toolbar")
    exit(1)
preview_toolbar_content = preview_toolbar_match.group(0)
content = content.replace(preview_toolbar_content, '')

# 3. Create the unified bottom bar
unified_bottom_bar = """
    [bottom]
    Gtk.Box editor_bottom_bar {
      orientation: horizontal;
      margin-start: 6;
      margin-end: 6;
      margin-top: 4;
      margin-bottom: 4;
      spacing: 2;
      styles ["toolbar", "silktex-bottom-toolbar"]

      // ── LEFT ZONE ──────────────────────────────────────────────────────
      Gtk.Box {
        orientation: horizontal;
        spacing: 2;

        Gtk.Box {
          orientation: horizontal;
          spacing: 0;
          styles ["linked"]
          Gtk.Button btn_compile {
            icon-name: "media-playback-start-symbolic";
            tooltip-text: _("Compile");
            action-name: "win.compile";
            styles ["linked"]
          }
          Gtk.MenuButton {
            icon-name: "pan-down-symbolic";
            tooltip-text: _("Document tools");
            menu-model: document_menu;
            styles ["flat"]
          }
        }

        Gtk.ToggleButton btn_tools_toggle {
          icon-name: "go-next-symbolic";
          tooltip-text: _("Show insert/format tools");
          styles ["flat"]
        }

        Gtk.Revealer revealer_left {
          transition-type: none;
          reveal-child: bind btn_tools_toggle.active bidirectional;
          child: Gtk.Box {
            orientation: horizontal;
            spacing: 0;
            styles ["linked"]
            
            Gtk.MenuButton btn_insert {
              icon-name: "insert-object-symbolic";
              tooltip-text: _("Insert");
              menu-model: insert_menu;
              styles ["linked"]
            }
            Gtk.MenuButton btn_format {
              icon-name: "format-text-bold-symbolic";
              tooltip-text: _("Format");
              menu-model: format_menu;
              styles ["linked"]
            }
          };
        }
      }

      // ── LEFT SPACER ────────────────────────────────────────────────────
      Gtk.Box {
        orientation: horizontal;
        hexpand: true;
      }

      // ── CENTER ZONE ────────────────────────────────────────────────────
      Gtk.Box {
        orientation: horizontal;
        spacing: 12;

        Gtk.Revealer revealer_center {
          transition-type: none;
          reveal-child: bind btn_tools_toggle.active;
          child: Gtk.Box {
            orientation: horizontal;
            spacing: 2;
            Gtk.Button btn_undo {
              icon-name: "edit-undo-symbolic";
              tooltip-text: _("Undo");
              action-name: "win.undo";
              styles ["flat"]
            }
            Gtk.Button btn_find_replace {
              icon-name: "edit-find-replace-symbolic";
              tooltip-text: _("Find and replace");
              action-name: "win.find-replace";
              styles ["flat"]
            }
            Gtk.Button btn_redo {
              icon-name: "edit-redo-symbolic";
              tooltip-text: _("Redo");
              action-name: "win.redo";
              styles ["flat"]
            }
          };
        }

        Gtk.Box {
          orientation: horizontal;
          spacing: 4;
          visible: bind btn_preview.active;

          Gtk.Button btn_prev_page {
            icon-name: "go-previous-symbolic";
            tooltip-text: _("Previous Page");
            action-name: "win.prev-page";
            styles ["flat"]
          }

          Gtk.Label page_label {
            label: "—";
            margin-start: 6;
            margin-end: 6;
            styles ["numeric", "dim-label"]
          }

          Gtk.Button btn_next_page {
            icon-name: "go-next-symbolic";
            tooltip-text: _("Next Page");
            action-name: "win.next-page";
            styles ["flat"]
          }
        }
      }

      // ── RIGHT SPACER ───────────────────────────────────────────────────
      Gtk.Box {
        orientation: horizontal;
        hexpand: true;
      }

      // ── RIGHT ZONE ─────────────────────────────────────────────────────
      Gtk.Box {
        orientation: horizontal;
        spacing: 2;

        Gtk.Revealer revealer_right {
          transition-type: none;
          reveal-child: bind btn_tools_toggle.active;
          child: Gtk.Box tools_toggle_git_group {
            orientation: horizontal;
            spacing: 0;
            Gtk.MenuButton btn_git_menu {
              icon-name: "git-symbolic";
              tooltip-text: _("Git");
              menu-model: git_menu;
              styles ["flat"]
            }
          
            Gtk.Box {
              orientation: horizontal;
              spacing: 0;
              styles ["linked"]
              Gtk.Button btn_save {
                icon-name: "document-save-symbolic";
                tooltip-text: _("Save");
                action-name: "win.save";
                styles ["flat"]
              }
              Gtk.MenuButton {
                icon-name: "pan-down-symbolic";
                tooltip-text: _("Save and export");
                menu-model: save_menu;
                styles ["flat"]
              }
            }
          };
        } 
        
        Gtk.ToggleButton btn_log {
          icon-name: "utilities-terminal-symbolic";
          tooltip-text: _("Show compile log");
          action-name: "win.toggle-log";
          styles ["flat"]
        }

        Gtk.Box {
          orientation: horizontal;
          spacing: 2;
          visible: bind btn_preview.active;

          Gtk.MenuButton btn_zoom_menu {
            icon-name: "document-properties-symbolic";
            tooltip-text: _("View tools");
            menu-model: zoom_menu;
            styles ["flat"]
          }

          Gtk.Button btn_zoom_out {
            icon-name: "zoom-out-symbolic";
            tooltip-text: _("Zoom Out");
            action-name: "win.zoom-out";
            styles ["flat"]
          }

          Gtk.Button btn_zoom_in {
            icon-name: "zoom-in-symbolic";
            tooltip-text: _("Zoom In");
            action-name: "win.zoom-in";
            styles ["flat"]
          }

          Gtk.Label preview_status {
            label: "";
            margin-end: 4;
            styles ["dim-label"]
          }

          Gtk.Button btn_forward_sync {
            icon-name: "find-location-symbolic";
            tooltip-text: _("Sync to cursor");
            action-name: "win.forward-sync";
            styles ["flat"]
          }

          Gtk.Button btn_external_open {
            icon-name: "document-send-symbolic";
            tooltip-text: _("Open PDF externally");
            action-name: "win.open-pdf-external";
            styles ["flat"]
          }
        }
      }
    }
"""

# Insert unified_bottom_bar before "content: Adw.ToastOverlay toast_overlay {"
content = content.replace('content: Adw.ToastOverlay toast_overlay {', unified_bottom_bar + '\ncontent: Adw.ToastOverlay toast_overlay {')

with open('data/ui/main.blp', 'w') as f:
    f.write(content)

print("Done")
