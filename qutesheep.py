# xenmacs - a simple, preconfigured Emacs binding set for qutebrowser
# xenmacs is ultimately work on a (currently) four-year-old script, qutemacs, uploaded by jumper047. 

# The aim of this binding set is to provide an Emacserian keymap for as much as possible inside of qutebrowser.
# As fast as qutebrowser is and feels to use, I do wish it'd make me think harder about my decisions. 
# This is my mindfulness browser. 
# It is important that this idea is tested or frameworked thoroughly enough to work smoothly.

# Installation
#
# 1. Copy this file or add this repo as a submodule to your dotfiles
# 2. Add this line to your config.py, and point the path to this file:
# config.source('xenmacs.py')


config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103

c.input.insert_mode.auto_enter = False 

c.input.insert_mode.auto_leave = False

c.input.insert_mode.plugins = True

c.input.insert_mode.auto_load = False

config.unbind("<ESC>", mode='insert') 

c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt', 'https://easylist-downloads.adblockplus.org/easylistdutch.txt', 'https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt', 'https://www.i-dont-care-about-cookies.eu/abp/', 'https://secure.fanboy.co.nz/fanboy-cookiemonster.txt']

# Forward unbound keys

# c.input.forward_unbound_keys = "all"

#ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'

ESC_BIND = 'fullscreen --leave'

c.bindings.default['normal'] = {}

c.editor.command = [ '/usr/bin/urxvt-256color', '-e', 'emacs', '-nw', '{file}' ]

c.fileselect.folder.command =  [ '/usr/bin/urxvt-256color', '-e', 'ranger', '--choosefiles={}' ]

#c.fileselect.folder.command =  [ '/usr/bin/urxvt-256color', '-e', 'mc', '-f', '{}' ]

#c.fileselect.multiple_files.command = [ '/usr/bin/urxvt-256color', '-e', 'mc', '-f', '{}' ]

c.fileselect.multiple_files.command = [ '/usr/bin/urxvt-256color', '-e', 'ranger', '--choosefiles={}' ]

c.fileselect.handler = 'external'

c.colors.webpage.darkmode.policy.images = "never" 

c.colors.webpage.darkmode.algorithm =  "lightness-cielab"

c.content.cookies.accept = "no-3rdparty" 

c.content.headers.do_not_track = False

c.url.default_page = "https://seraphgrid.github.io"

c.url.start_pages = [ "https://seraphgrid.github.io" ] 

# Bindings

c.bindings.commands['normal'] = {

    # Navigation
    

    '<w>': 'scroll-page 0 -0.2',
    '<a>': 'scroll-page -0.2 0',
    '<s>': 'scroll-page 0 0.1',
    '<d>': 'scroll-page 0.2 0',
    

  # '<Backspace>': 'scroll-page 0 -0.9',
 
  # '<Space>': 'scroll-page 0 0.9',

  # '<alt-shift-.': 'scroll-to-perc',

    '<ctrl-z>': 'scroll-to-perc 100',
    '<ctrl-w>': 'scroll-to-perc 0',
    
    # xenutility
    
    '<ctrl-x><ctrl-s>': 'set-cmd-text -s :session-save',

#   '<ctrl-x><ctrl-s><ctrl-d>': 'set-cmd-text -s :session-delete',

    '<ctrl-x><shift-s>': 'set-cmd-text -s :session-load',

    '<ctrl-x><ctrl-x><ctrl-s>': 'set-cmd-text :config-write-py --force',
    
    '<alt-z>': 'spawn -d urxvt -e emacs -nw --file ~/.config/qutebrowser/xenmacs.py ',
    
    '<ctrl-x><ctrl-r>': 'restart',
    
    '<ctrl-x><ctrl-u>': 'undo',

#    '<ctrl-y>': 'set-cmd-text :redo',

    '<ctrl-x><ctrl-x><ctrl-x>': 'quit',

    '<alt-shift-5>': 'set-cmd-text :screenshot',   

    # '<ctrl-x><c><o><n><ctrl-s>': 'set-cmd-text :config-write-py --force',
    # '<ctrl-x><c><o><n><ctrl-f>': 'spawn -d urxvt -e emacs -nw --file ~/.config/qutebrowser/xenmacs.py ',
    
    # '<ctrl-x><c><ctrl-f>': 'config-edit',

    
    # '<ctrl-x><ctrl-c>': 'session-save ;; quit', , with a prompt before ;; quit. 
    
    # xen mini buffer

    '</>': 'set-cmd-text /',
    '<?>': 'set-cmd-text ?', 

    '<:>': 'set-cmd-text :',

    '<ctrl-b><x>': 'set-cmd-text -s :unbind',
    '<ctrl-b><s>': 'set-cmd-text -s :bind',
    '<ctrl-x><alt-x>': 'set-cmd-text -s :set',
    '<F11>': 'fullscreen',
    '<F12>': 'devtools',
    '<shift-F12>': 'devtools-focus',
    # Will eventually be all necessary minibuffer commands, with patience. 

    # xen hinting
    
    '<h>': 'hint all',
    '<v>': 'hint images',
    '<ctrl-d>': 'hint all download',
    '<i>': 'hint inputs',
    '<ctrl-h><h>': 'hint all hover',
    '<ctrl-h><p>': 'hint all pretty-url',
    '<ctrl-h><v>': 'hint links spawn --detach mpv --loop --force-window=immediate --volume=50 {hint-url}',
    '<ctrl-h><f>': 'hint all tab-fg',
    '<ctrl-h><b>': 'hint all tab-bg',
    
    # xen copying
    
    '<ctrl-c><d>': 'hint all yank download',
    '<ctrl-c><p>': 'hint all yank',
#    '<ctrl-c><u>': 'hint all yank url',
    '<ctrl-c><s>': 'yank selection',
    '<ctrl-c><f>': 'yank url', # Copy frame url.

    # xen buffer nav
    
    '<shift-r>': 'reload',
    '<ctrl-left>': 'forward',
    '<ctrl-right>': 'back',
   

    # xenmarks
    
    '<ctrl-space>': 'set-cmd-text -s :bookmark-add {url}',
    '<space>': 'set-cmd-text -s :quickmark-add {url}',
    
    # saturn (download opening)

    '<ctrl-x><i>': 'download-open',
#    '<s><a><t><u><r><n>': 'set-cmd-text :download-open',
    
    # xentabs
   
    '<ctrl-t><shift-left>': 'tab-move +',
    '<ctrl-t><shift-right>': 'tab-move -',

    '<ctrl-x><0>': 'tab-close',
    # '<0><0><0>': 'tab-close',
    '<ctrl-t><ctrl-1>': 'tab-pin',
    '<ctrl-t><m>': 'tab-mute',
    '<ctrl-t><o>': 'tab-only',
    '<ctrl-t><c>': 'tab-clone',
    
    '<ctrl-t><ctrl-g>': 'set-cmd-text -s tab-give',
    '<ctrl-t><ctrl-t>': 'set-cmd-text -s :tab-take',
    '<ctrl-t><ctrl-s>': 'set-cmd-text -s :tab-select',

    '<alt-1>': 'tab-focus 1',
    '<alt-2>': 'tab-focus 2',
    '<alt-3>': 'tab-focus 3',
    '<alt-4>': 'tab-focus 4',
    '<alt-5>': 'tab-focus 5',
    '<alt-6>': 'tab-focus 6',
    '<alt-7>': 'tab-focus 7',
    '<alt-8>': 'tab-focus 8',
    '<alt-9>': 'tab-focus 9',
    '<alt-0>': 'tab-focus 10',
    '<ctrl-x><o>': 'tab-focus -1',
    '<ctrl-x><ctrl-b>': 'set-cmd-text :tab-focus 1', 
    
    # '<ctrl-x><ctrl-t><f>': 'set-cmd-text -s :tab-focus', # hastily seen as redundant. i will remember to take another look.
    
    # xenframes

    '<ctrl-f><c>': 'set-cmd-text :close',
    '<ctrl-f><1>': 'window-only',
    '<ctrl-x><2>': 'set-cmd-text -s :open -w',
  # '<ctrl-x><shift-f><p>': 'set-cmd-text -s :open -p',
    '<ctrl-x><5><2>': 'set-cmd-text -s :open -p',

    # frame shift (reality)
    
    '<ctrl-x><ctrl-f>': 'set-cmd-text -s :open',
    '<ctrl-x><3>': 'set-cmd-text -s :open -t', 
    
    # '<ctrl-x><shift-s>': 'set-cmd-text -s :open -t',
    # '<ctrl-x><ctrl-t>': 'set-cmd-tab',

    # editing

    '<shift-m>': 'set-cmd-text -s :mode-enter',

    '<ctrl-x><i>': 'mode-enter insert', 
   # '<v><o><i><d>': 'mode-enter insert',
    '<ctrl-x><c>': 'mode-enter caret',
   # '<ctrl-x><e><m><s>': 'mode-enter caret ;; toggle-selection --line',
   # '<ctrl-x><p>': 'mode-enter passthrough', 
   # '<ctrl-f>': 'fake-key <Right>',
   # '<ctrl-b>': 'fake-key <Left>',
   # '<ctrl-a>': 'fake-key <Home>',
   # '<ctrl-e>': 'fake-key <End>',
   # '<ctrl-n>': 'fake-key <Down>',
   # '<ctrl-p>': 'fake-key <Up>',
   # '<alt-f>': 'fake-key <Ctrl-Right>',
   # '<alt-b>': 'fake-key <Ctrl-Left>',
   # '<ctrl-d>': 'fake-key <Delete>',
   # '<alt-d>': 'fake-key <Ctrl-Delete>',
   # '<alt-backspace>': 'fake-key <Ctrl-Backspace>',
   # '<ctrl-w>': 'fake-key <Ctrl-backspace>',
   # '<ctrl-y>': 'insert-text {clipboard}',
    

    # Numbers, The Language of the Stars (read the link if confused)
    # https://github.com/qutebrowser/qutebrowser/issues/4213

    '1': 'fake-key 1',
    '2': 'fake-key 2',
    '3': 'fake-key 3',
    '4': 'fake-key 4',
    '5': 'fake-key 5',
    '6': 'fake-key 6',
    '7': 'fake-key 7',
    '8': 'fake-key 8',
    '9': 'fake-key 9',
    '0': 'fake-key 0',

    # Control Your Meta
    
    # Will add external editor and file manager here.
    
    '<ctrl-m><v>': 'spawn -d mpv --loop --force-window=immediate --volume=50 {url}',
    '<ctrl-m><r>': 'spawn -d goodvibes',
    '<ctrl-m><p>': 'spawn -d keepassxc', 
    '<ctrl-m><e>': 'spawn -d emacs',
    '<ctrl-m><w>': 'spawn -d firefox {url}', # lol
    '<ctrl-m><f>': 'spawn -d urxvt -e mc',
    
    '<x><e><n><i><a>': 'set-cmd-text :',
    '<ctrl-x><v><v>': ':version',

    # Will add config edit commands when I find time. 
    
    # Ask For Help

    '<shift-h><ctrl-b>': 'open -t qute://bindings',
    '<shift-h><shift-b>': 'open -t qute://bookmarks',    
    '<shift-h><shift-h>': 'open -t qute://quickmarks',
    '<shift-h><shift-d>': 'open -t qute://downloads',
    '<shift-h><ctrl-h>': 'set-cmd-text -s :help',

    # '<ctrl-x><e><n>': ESC_BIND,

    # Websites
    # will be <alt-x><o>, then the name.
    # <alt-x><o> as :open will become <ctrl-x><ctrl-s> (visit)
    
    '<alt-w><y>': 'open -t https://youtube.com', # GARBAGE website.

    '<alt-w><m><1>': 'open -t https://discord.com/app', # GARBAGE website.

    '<alt-w><m><2>': 'open -t https://guilded.gg/', # GOATED website.
    
    '<alt-w><d><u><o>': 'open -t https://duolingo.com', # GOATED(?) website.
    '<alt-w><a><m><b>': 'open -t https://ambientsleepingpill.com', # GOATED website.
    '<alt-w><g>': 'open -t https://github.com', # GOGARTED
    '<alt-w><w><g>': 'open -t https://4chan.org/wg/', # GOATED website.
    '<alt-w><c>': 'open -t https://broward.edu',
    # Will figure out how to call it :search in this state. Patience. 

    # Will also find a way to do a custom query before opening a link to a site like YouTube? 
    
    '<alt-w><s><u>': 'open -t https://sushigirl.us'

    # Add M-x find
    
    # Miscellaneous
    
    }

c.bindings.commands['command'] = {

    '<ctrl-q>': 'search-next',
    '<ctrl-s>': 'search-prev',

    '<alt-m>': 'completion-item-focus prev',
    '<alt-x>': 'completion-item-focus next',

    '<shift-m>': 'command-history-prev',
    '<shift-x>': 'command-history-next',

    # escape hatch
    '<ctrl-g>': 'mode-enter normal',
}

c.bindings.commands['hint'] = {
    # escape hatch
    '<ctrl-g>': 'mode-enter normal',
}


c.bindings.commands['caret'] = {

    '<q>': 'fake-key <Up>',
    '<s>': 'fake-key <Down>',
    '<j>': 'fake-key <PgDown>',
    '<k>': 'fake-key <PgUp>',
    '<shift-q>': 'fake-key <Home>',
    '<shift-s>': 'fake-key <End>',
    
    # escape hatch
    '<ctrl-g>': 'mode-enter normal',
}

c.bindings.commands['insert'] = {

    # editing

    '<ctrl-x><ctrl-e>': 'edit-text',
    '<ctrl-c>': 'fake-key <Space>',
    '<ctrl-v>': 'fake-key <Backspace>',
    '<ctrl-x><s><a>': 'fake-key <Ctrl-a>',
    '<ctrl-x><left>': 'fake-key <Ctrl-Shift-Left>',
    '<ctrl-x><right>': 'fake-key <Ctrl-Shift-Right>',
    '<left>': 'fake-key <Left>',
    '<right>': 'fake-key <Right>',
    '<ctrl-f>': 'fake-key <Ctrl-Right>',
    '<ctrl-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    '<alt-f>': 'fake-key <Ctrl-Right>',
    '<alt-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl-Delete>',
    # '<ctrl-x><u>': 'fake-key <Ctrl-u>',
    '<ctrl-x><backspace>': 'fake-key <Ctrl-Backspace>',
    # '<alt-d>': 'fake-key <Ctrl-Backspace>',
    # '<ctrl-w>': 'fake-key <Ctrl-backspace>',
    '<ctrl-x><p>': 'fake-key <Ctrl-v>',
    '<ctrl-x><x>': 'fake-key <Ctrl-x>',
    '<ctrl-x><c>': 'fake-key <Ctrl-c>',
    '<ctrl-x><u>': 'fake-key <Ctrl-u>',
    '<ctrl-x><h>': 'hint inputs',
    '<ctrl-g>': 'mode-enter normal',
    

}
