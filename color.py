'''
Color Module
------------

This module implements the general functions used to color your logs printed in
the screen. To use these funtions, import the 'color' module and call the
funtions in a print context.

@author: @italocampos
'''

import background as bg
import foreground as fg
import style as st


def format(text: str, style='normal'):
    '''It returns the text styled according the provided `style` parameter. It
    returns the `text` with no changes if the provided `style` is invalid.

    Styles options:
        - 'd', 'dim' : the dim font style;
        - 'n', 'normal' : the normal font style;
        - 'b', 'bold' : the bold font style;
    The default style is 'normal'.

    Parameters
    ----------
    text : str
        The text to be styled.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.

    Returns
    -------
    str
        The styled `text` according the provided `style` parameter.
    '''

    if style in ['d', 'dim']:
        return f'{st.DIM}{text}{st.RESET}'.format(text=text)
    if style in ['n', 'normal']:
        return f'{st.NORMAL}{text}{st.RESET}'.format(text=text)
    if style in ['b', 'bold']:
        return f'{st.BRIGHT}{text}{st.RESET}'.format(text=text)
    return text


def set_foreground(text: str, color: str, style: str, bg: str):
    '''For internal use only. This function returns the `text` colored,
    formatted and with the suitable background set.

    Parameters
    ----------
    text : str
        The text to be colored with the provided `color`.
    color: str
        The color to be applied to the `text`.
    style : str
        The style to format the `text`.
    bg : str
        The color to be applied to `text` background.

    Returns
    -------
    str
        The colored, styled and background-colored `text` formatted according
        with the provided parameters.
    '''

    colored_text = f'{color}' + '{text}'.format(
        text=format(text=text, style=style)
    )
    return set_background(colored_text, color=bg)


def set_background(text: str, color: str = None):
    '''It returns a string with background color set according with the color
    provide in `color` parameter. It returns the `text` with no changes if the
    provided `color` is invalid.

    Parameters
    ----------
    text : str
        The text to have the background set.
    color : str, optional
        The string with the color name to be set in background of `color`.
        Defatult is `None`.

    Returns
    -------
    str
        The `text` with background colored with the color provided in `color`.
    '''

    if color == 'black':
        return f'{bg.BLACK}{text}{st.RESET}'
    if color == 'red':
        return f'{bg.RED}{text}{st.RESET}'
    if color == 'green':
        return f'{bg.GREEN}{text}{st.RESET}'
    if color == 'yellow':
        return f'{bg.YELLOW}{text}{st.RESET}'
    if color == 'blue':
        return f'{bg.BLUE}{text}{st.RESET}'
    if color == 'magenta':
        return f'{bg.MAGENTA}{text}{st.RESET}'
    if color == 'cyan':
        return f'{bg.CYAN}{text}{st.RESET}'
    if color == 'white':
        return f'{bg.WHITE}{text}{st.RESET}'
    return text


def red(text, style='normal', bg=None):
    '''It returns the `text` colored with red color.

    Parameters
    ----------
    text : str
        The text to be colored with the red color.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.
    bg : str, optional
        The color to be applied to `text` background. Default is no color
        (`None`).

    Returns
    -------
    str
        The styled and colored text according the provided `style` parameter.
    '''

    return set_foreground(text=text, color=fg.RED, style=style, bg=bg)


def black(text, style='normal', bg=None):
    '''It returns the `text` colored with black color.

    Parameters
    ----------
    text : str
        The text to be colored with the black color.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.
    bg : str, optional
        The color to be applied to `text` background. Default is no color
        (`None`).

    Returns
    -------
    str
        The styled and colored text according the provided `style` parameter.
    '''

    return set_foreground(text=text, color=fg.BLACK, style=style, bg=bg)


def green(text, style='normal', bg=None):
    '''It returns the `text` colored with green color.

    Parameters
    ----------
    text : str
        The text to be colored with the green color.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.
    bg : str, optional
        The color to be applied to `text` background. Default is no color
        (`None`).

    Returns
    -------
    str
        The styled and colored text according the provided `style` parameter.
    '''

    return set_foreground(text=text, color=fg.GREEN, style=style, bg=bg)


def yellow(text, style='normal', bg=None):
    '''It returns the `text` colored with yellow color.

    Parameters
    ----------
    text : str
        The text to be colored with the yellow color.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.
    bg : str, optional
        The color to be applied to `text` background. Default is no color
        (`None`).

    Returns
    -------
    str
        The styled and colored text according the provided `style` parameter.
    '''

    return set_foreground(text=text, color=fg.YELLOW, style=style, bg=bg)


def blue(text, style='normal', bg=None):
    '''It returns the `text` colored with blue color.

    Parameters
    ----------
    text : str
        The text to be colored with the blue color.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.
    bg : str, optional
        The color to be applied to `text` background. Default is no color
        (`None`).

    Returns
    -------
    str
        The styled and colored text according the provided `style` parameter.
    '''

    return set_foreground(text=text, color=fg.BLUE, style=style, bg=bg)


def magenta(text, style='normal', bg=None):
    '''It returns the `text` colored with magenta color.

    Parameters
    ----------
    text : str
        The text to be colored with the magenta color.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.
    bg : str, optional
        The color to be applied to `text` background. Default is no color
        (`None`).

    Returns
    -------
    str
        The styled and colored text according the provided `style` parameter.
    '''

    return set_foreground(text=text, color=fg.MAGENTA, style=style, bg=bg)


def cyan(text, style='normal', bg=None):
    '''It returns the `text` colored with cyan color.

    Parameters
    ----------
    text : str
        The text to be colored with the cyan color.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.
    bg : str, optional
        The color to be applied to `text` background. Default is no color
        (`None`).

    Returns
    -------
    str
        The styled and colored text according the provided `style` parameter.
    '''

    return set_foreground(text=text, color=fg.CYAN, style=style, bg=bg)


def white(text, style='normal', bg=None):
    '''It returns the `text` colored with white color.

    Parameters
    ----------
    text : str
        The text to be colored with the white color.
    style : str, optional
        The style to be used with the font. Default is 'normal' style.
    bg : str, optional
        The color to be applied to `text` background. Default is no color
        (`None`).

    Returns
    -------
    str
        The styled and colored text according the provided `style` parameter.
    '''

    return set_foreground(text=text, color=fg.WHITE, style=style, bg=bg)
