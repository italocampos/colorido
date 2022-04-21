'''
Color Module
------------

This module implements the general functions used to color your logs printed in
the screen. To use these funtions, import the 'color' module and call the
funtions in a print context.

@author: @italocampos
'''

import foreground, style as st


def style(text, style = 'normal'):
    ''' Returns the text styled according the provided parameter.

    Possible styles:
        - 'd', 'dim' : the dim font style;
        - 'n', 'normal' : the normal font style;
        - 'b', 'bold' : the bold font style;
    The default style is 'normal'.
    
    Parameters
    ----------
    text : str
        The text to be styled.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled text according the provided 'style' parameter.
    '''

    if style in ['d', 'dim']:
        return f'{st.DIM}{text}{st.RESET}'.format(text = text)
    elif style in ['n', 'normal']:
        return f'{st.NORMAL}{text}{st.RESET}'.format(text = text)
    elif style in ['b', 'bold']:
        return f'{st.BRIGHT}{text}{st.RESET}'.format(text = text)
    else:
        raise(Exception('Unknown style.'))



def red(text_, style_ = 'normal'):
    ''' Returns the red colored text.

    Parameters
    ----------
    text : str
        The text to be colored with the red color.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled and colored text according the provided 'style_' parameter.
    '''

    return f'{foreground.RED}' + '{text}'.format(text = style(text = text_, style = style_))


def black(text_, style_ = 'normal'):
    ''' Returns the black colored text.

    Parameters
    ----------
    text : str
        The text to be colored with the black color.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled and colored text according the provided 'style_' parameter.
    '''

    return f'{foreground.BLACK}' + '{text}'.format(text = style(text = text_, style = style_))


def green(text_, style_ = 'normal'):
    ''' Returns the green colored text.

    Parameters
    ----------
    text : str
        The text to be colored with the green color.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled and colored text according the provided 'style_' parameter.
    '''

    return f'{foreground.GREEN}' + '{text}'.format(text = style(text = text_, style = style_))


def yellow(text_, style_ = 'normal'):
    ''' Returns the yellow colored text.

    Parameters
    ----------
    text : str
        The text to be colored with the yellow color.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled and colored text according the provided 'style_' parameter.
    '''

    return f'{foreground.YELLOW}' + '{text}'.format(text = style(text = text_, style = style_))


def blue(text_, style_ = 'normal'):
    ''' Returns the blue colored text.

    Parameters
    ----------
    text : str
        The text to be colored with the blue color.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled and colored text according the provided 'style_' parameter.
    '''

    return f'{foreground.BLUE}' + '{text}'.format(text = style(text = text_, style = style_))


def magenta(text_, style_ = 'normal'):
    ''' Returns the magenta colored text.

    Parameters
    ----------
    text : str
        The text to be colored with the magenta color.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled and colored text according the provided 'style_' parameter.
    '''

    return f'{foreground.MAGENTA}' + '{text}'.format(text = style(text = text_, style = style_))


def cyan(text_, style_ = 'normal'):
    ''' Returns the cyan colored text.

    Parameters
    ----------
    text : str
        The text to be colored with the cyan color.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled and colored text according the provided 'style_' parameter.
    '''

    return f'{foreground.CYAN}' + '{text}'.format(text = style(text = text_, style = style_))


def white(text_, style_ = 'normal'):
    ''' Returns the white colored text.

    Parameters
    ----------
    text : str
        The text to be colored with the white color.
    style : str, optional
        The style to be used with the font.
    
    Returns
    -------
    str
        The styled and colored text according the provided 'style_' parameter.
    '''

    return f'{foreground.WHITE}' + '{text}'.format(text = style(text = text_, style = style_))