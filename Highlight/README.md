SublimeHighlight
================

This [SublimeText2](http://www.sublimetext.com/2) package allows to highlight &
export currently edited code to HTML or RTF using [Pygments](http://pygments.org/).

Several commands are added to SublimeText2 when installed:

- **SublimeHighlight: convert to HTML**: will convert current code to
  highlighted HTML in a new SublimeText tab.
- **SublimeHighlight: convert to RTF**: will convert current code to
  highlighted RTF in a new SublimeText tab.
- **SublimeHighlight: view as HTML**: will convert current code to highlighted
  HTML and open it in your default browser.
- **SublimeHighlight: view as RTF**: will convert current code to an RTF
  document and open the generated file with your default program.
- **SublimeHighlight: copy to clipboard as HTML**: will convert current code to
  highlighted HTML and store it into the system clipboard.
- **SublimeHighlight: copy to clipboard as RTF**: will convert current code to
  raw highlighted RTF and store it into the system clipboard.

Settings
--------

You can find a dedicated user settings file in the `Preferences > Package
Settings > SublimeHighlight` menu, where you can choose the Pygments theme to
use. Example `Settings - User` file:

    {
        "theme": "vim"
    }

Available themes are:

- `autumn`
- `borland`
- `bw`
- `colorful`
- `default`
- `emacs`
- `friendly`
- `fruity`
- `manni`
- `monokai`
- `murphy`
- `native`
- `pastie`
- `perldoc`
- `rrt`
- `tango`
- `trac`
- `vim`
- `vs`

Why this package?
-----------------

Mostly for toying around with [SublimeText2 plugin API](http://www.sublimetext.com/docs/2/api_reference.html)
(which is great), but also to ease the process of copying/pasting richly
formatted code over softwares like Powerpoint, Word, Keynote and shits like
that.

License
-------

This software is released under the terms of the [MIT license](http://en.wikipedia.org/wiki/MIT_License).
