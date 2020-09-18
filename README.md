# Color lib

A small Python 3.x lib to speed up the coloring usage throughout your Python
projects. You ever can make your logs prettier.


## About the lib

This lib has a module that implements the gereral functions to color strings
that are printed in the screen by the 'print' functions of Python 3.x. This
package depends on [Colorama](https://pypi.org/project/colorama/) Python lib.
In a nutshell, use these functions by importing the `color` module and calling
the functions in a print context.


## Installation

You can use this lib without installation. To do that, in a Terminal, install
the Colorama lib by typing:

``` Shell
pip install colorama
```

After installed the Colorama lib, copy the file `color/color.py` to your
project and use that with `import color`. All is ready!

If you want to install it, you can do that easily by cloning this Github
repository and installing it with `pade -e`. In a Terminal, type:

``` Shell
git clone git@github.com:italocampos/color.git
pip install -e color
```


## Usage

To use the functions, download and import the lib within your code. After, just
call the function with the color you want to print. See the example below:

``` Python
import color
print('This is the color ' + color.red('red') + '.')
```


### Coloring

You can choose among the available colors in the [Colorama](https://pypi.org/project/colorama/)
library to color the foreground of your texts. To make your life more easy, I
listed below the colors available in this version of **Color** lib:

| Text color   | Function       |
| ------------ | -------------- |
| Black        | `black(srt)`   |
| Blue         | `blue(srt)`    |
| Cyan         | `cyan(srt)`    |
| Green        | `green(srt)`   |
| Magenta      | `magenta(srt)` |
| Red          | `red(srt)`     |
| White        | `black(srt)`   |
| Yellow       | `black(srt)`   |

> **Important: ** The Color lib only colors text in the foreground. To use
background colored texts, refer to the [Colorama](https://pypi.org/project/colorama/)
lib or other.

Remember that the colors above may vary according the configuration of your
Terminal or system.

More examples of coloring:

Example 1:

``` Python
import color
text = color.yellow('BR') + color.green('AZ') + color.blue('IL')
print('Come visit %s.' % text)
```

Example 2:

``` Python
import color
print('sudo %s' % color.red('rm -rf /'))
```

Example 3:
``` Python
import color
print('Is the zebra {black} with {white} stripes or {white} with {black} stripes?'.format(
    black = color.black('BLACK'),
    white = color.white('WHITE'),
))
```


### Styling

The Color lib also support text styling, according the [Colorama](https://pypi.org/project/colorama/)
lib. The supported styles are three:

- Dim text
- Normal text
- Bold text

You can style your text by passing an extra parameter to the color functions,
which is optional. The list with the parameters are below:

| Text style | Parameter                     |
| ---------- | ----------------------------- |
| Dim        | `'d'` or `'dim'`              |
| Normal     | `'n'` or `'normal'` (default) |
| Bold       | `'b'` or `'bold'`             |

In a practical way, you can style your text like:

Example 4:

``` Python
import color
print('This is the {text}.'.format(text = color.yellow('bold style', style_ = 'bold')))
# or simply
print('This is the {text}.'.format(text = color.yellow('bold style', 'b')))
```

Example 5:

``` Python
import color
print('Use {color} {lib}.'.format(
    color = color.blue('Color', 'bold'),
    lib = color.black('lib', 'dim'),
))
```

If you want, you can use only the style function, without color your text. See
that:

Example 6:

``` Python
import color
print('I {love} {linux}.'.format(
    love = color.style('<3', 'dim'),
    linux = color.style('Linux', 'bold'),
))
```

That's all folks!


## Who is this lib for?

This lib is addressed to anyone who wants want a simple lib to print colored
texts in the screen without a hundred of things to learn. You just need to 
import the module and call the functions.

This lib doesn't match the programmers that want a full-featured lib. This lib
just returns colored texts to be printed in the screen. If that is your case,
search for other python libraries.


## License

This lib is a free software and is distributed under the [MIT License](https://opensource.org/licenses/MIT).