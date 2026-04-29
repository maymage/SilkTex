# TODO

- [ ] Make fit-width preview a toggle that follows resize
- [ ] Clean up the bottom toolbar to follow Adwaita guidelines
- [ ] style the bottom bar following the adwaita and gnome
      style guide


⏺ Let me look at the current bottom bar implementation
 first.

Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(find /Users/beba/software/SilkTex/src -name "_.css"
 -o -name "_.c" | xargs grep -l
 "bottom.bar\|statusbar\|bottom_bar\|BottomBar"
❯ /clear
 ⎿  (no content)

❯ style the bottom bar following the adwaita and gnome style guide

⏺ Let me look at the current bottom bar implementation first.

Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(find /Users/beba/software/SilkTex/src -name "_.css" -o -name "_.c" | xargs grep -l
"bottom.bar\|statusbar\|bottom_bar\|BottomBar" 2>/dev/null | head -20)
⎿  /Users/beba/software/SilkTex/src/window.c

Searched for 4 patterns, read 3 files (ctrl+o to expand)

⏺ Let me check how the editor CSS is loaded to understand the pattern, and look at the
window.c for bottom bar setup.

Searched for 1 pattern, read 2 files (ctrl+o to expand)

⏺ Let me see the full CSS block to understand all current rules.

Read 1 file (ctrl+o to expand)

⏺ Now I have a clear picture. The bottom bar has several issues against Adwaita
guidelines:

1. Custom CSS actively strips the natural Adwaita border/shadow from the bottom toolbar
2. The margin-top/bottom: 4px is inconsistent with the Adwaita standard 6px, making the
   bar shorter than a headerbar (~42px vs ~46px)
3. root_toolbar_view bottom bar style is never set (defaults to FLAT with no separator),
   and the CSS overrides make the separation from content invisible
4. Dead separator CSS that nullifies any separators
