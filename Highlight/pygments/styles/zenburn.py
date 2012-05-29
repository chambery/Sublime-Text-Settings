# -*- coding: utf-8 -*-
"""
    pygments.styles.monokai
    ~~~~~~~~~~~~~~~~~~~~~~~

    Mimic the Monokai color scheme. Based on tango.py.

    http://www.monokai.nl/blog/2006/07/15/textmate-color-theme/

    :copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

class ZenburnStyle(Style):
    """
    This style mimics the Zenburn color scheme.
    """

    #background_color = "#1f1f1f" #high contrast
    background_color = "#3f3f3f"
    highlight_color = "#2f2f2f"
    #highlight_color = "#dcdccc"

    styles = {
        # No corresponding class for the following:
        Text:                      "#dcdccc", # class:  ''
        Whitespace:                "#000000",        # class: 'w'#TODO
        #Error:                     "#80d4aa bg:#2f2f2f", # class: 'err'#errormsg
        Error:                     "#e37170 bg:#3d3535", # class: 'err'
        Other:                     "#000000",        # class 'x'#TODO

        Comment:                   "italic #7f9f7f", # class: 'c'
        Comment.Multiline:         "#000000",        # class: 'cm'#TODO
        Comment.Preproc:           "#000000",        # class: 'cp'#TODO
        Comment.Single:            "#000000",        # class: 'c1'#TODO
        Comment.Special:           "#000000",        # class: 'cs'#82a282

        Keyword:                   "bold #f0dfaf", # class: 'k'
        Keyword.Constant:          "#dca3a3",        # class: 'kc'
        Keyword.Declaration:       "#000000",        # class: 'kd'#TODO
        Keyword.Namespace:         "bold #dfaf8f", # class: 'kn' #import
        Keyword.Pseudo:            "#000000",        # class: 'kp'#TODO
        Keyword.Reserved:          "#000000",        # class: 'kr'#TODO
        Keyword.Type:              "#000000",        # class: 'kt'#TODO

        Operator:                  "#f0efd0", # class: 'o'
        Operator.Word:             "#f0efd0",        # in not is

        Punctuation:               "#8f8f8f", # class: 'p'#TODO

        Name:                      "#dcdccc", # class: 'n'#TODO
        Name.Attribute:            "#000000", # class: 'na' - to be revised#TODO
        Name.Builtin:              "#efef8f",        # class: 'nb'#works
        Name.Builtin.Pseudo:       "#efef8f",        # class: 'bp'#(self) works
        Name.Class:                "#efef8f", # class: 'nc' - to be revised
        Name.Constant:             "#000000", # class: 'no' - to be revised
        Name.Decorator:            "#000000", # class: 'nd' - to be revised#TODO
        Name.Entity:               "#000000",        # class: 'ni'#TODO
        Name.Exception:            "bold #c3bf9f", # class: 'ne'
        Name.Function:             "#efef8f", # class: 'nf'
        Name.Property:             "#000000",        # class: 'py'#TODO
        Name.Label:                "#000000",        # class: 'nl'#TODO
        Name.Namespace:            "#8fbede",        # class: 'nn' - to be revised#import names
        Name.Other:                "#000000", # class: 'nx'#TODO
        Name.Tag:                  "#000000", # class: 'nt' - like a keyword
        Name.Variable:             "#000000",        # class: 'nv' - to be revised#TODO
        Name.Variable.Class:       "#efef8f",        # class: 'vc' - to be revised
        Name.Variable.Global:      "#000000",        # class: 'vg' - to be revised#TODO
        Name.Variable.Instance:    "#000000",        # class: 'vi' - to be revised#TODO

        Number:                    "#8cd0d3", # class: 'm'
        #Number.Float:              "#000000",        # class: 'mf'#TODO
        #Number.Hex:                "#000000",        # class: 'mh'#TODO
        #Number.Integer:            "#000000",        # class: 'mi'#TODO works
        #Number.Integer.Long:       "#000000",        # class: 'il'#TODO
        #Number.Oct:                "#000000",        # class: 'mo'#TODO

        Literal:                   "#000000", # class: 'l'#TODO
        Literal.Date:              "#000000", # class: 'ld'#TODO

        String:                    "#cc9393", # class: 's'
        String.Backtick:           "#000000",        # class: 'sb'#TODO
        String.Char:               "#000000",        # class: 'sc'#TODO
        #String.Doc:                "italic #7f9f7f",        # class: 'sd' - """comment"""#TODO
        String.Double:             "#000000",        # class: 's2'#TODO
        String.Escape:             "#000000", # class: 'se'#TODO
        String.Heredoc:            "#000000",        # #TODO
        String.Interpol:           "#000000",        # class: 'si'#TODO
        String.Other:              "#000000",        # class: 'sx'#TODO
        String.Regex:              "#000000",        # class: 'sr'#TODO
        String.Single:             "#000000",        # class: 's1'#TODO
        String.Symbol:             "#000000",        # class: 'ss'#TODO

        Generic:                   "#000000",        # class: 'g'#TODO
        Generic.Deleted:           "#000000",        # class: 'gd',#TODO
        Generic.Emph:              "#000000",  # class: 'ge'#TODO
        Generic.Error:             "#000000",        # class: 'gr'#TODO
        Generic.Heading:           "#000000",        # class: 'gh'#TODO
        Generic.Inserted:          "#000000",        # class: 'gi'#TODO
        Generic.Output:            "#000000",        # class: 'go'#TODO
        Generic.Prompt:            "#000000",        # class: 'gp'#TODO
        Generic.Strong:            "#000000",    # class: 'gs'#TODO
        Generic.Subheading:        "#000000",        # class: 'gu'#TODO
        Generic.Traceback:         "#000000",        # class: 'gt'#TODO
    }
