# PyTextColor lib

PyTextColor is a small Python 3.x lib to speed up the text coloring throughout
your Python projects. You ever can make your logs prettier. ;)

This package is "as it is", and you don't need to install any dependencies to
use it. In a nutshell, import the `color` module and call the functions in a
print context to start coloring your strings.


## Installation

Start cloning this GitHub repository and installing it with `pip install -e`.
In a Terminal, type:

``` Shell
git clone git@github.com:italocampos/color.git
pip install -e color
```


## Usage

To use the PyTextColor functions, import the lib in your code and just call the
function with the color you want to print. See the example below:

``` Python
import color

print('This is the color ' + color.red('red') + '.')
```


### Coloring

You can choose colors among the eight available options. The options are:

| Text color   | Function       |
| ------------ | -------------- |
| Black        | `black(str)`   |
| Blue         | `blue(str)`    |
| Cyan         | `cyan(str)`    |
| Green        | `green(str)`   |
| Magenta      | `magenta(str)` |
| Red          | `red(str)`     |
| White        | `white(str)`   |
| Yellow       | `yellow(str)`   |

Remember that the colors above may vary according the configuration of your
Terminal or system.


#### Basic examples

Below we have some examples of PyTextColor usage.

Example 1:

``` Python
import color

text = color.green('BR') + color.yellow('AZ') + color.blue('IL')
print('Come to visit %s.' % text)
```

Example 2:

``` Python
import color

print(f'sudo {color.red("rm -rf /")}')
```

Example 3:
``` Python
import color

print(
    'Is zebra {black} with {white} stripes or {white} with {black} stripes?'.format(
        black=color.black('BLACK'),
        white=color.white('WHITE'),
    )
)
```


### Styling

PyTextColor also support text styling. The supported styles are:

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

You can provide the `style` parameter as a second positional parameter in color
functions or explicity provide the `style` parameter. In a practical way, you
can do:

Example 4:

``` Python
import color

# Providing a explicity `style` parameter
print(
    'This is the {text}.'.format(text=color.yellow('bold style', style='bold'))
)
# or simply
print('This is the {text}.'.format(text=color.yellow('bold style', 'bold')))
# or yet
print('This is the {text}.'.format(text=color.yellow('bold style', 'b')))
```

Example 5:

``` Python
import color

print(
    'PyTextColor {_is} {easy}.'.format(
        _is=color.blue('is', 'bold'),
        easy=color.black('easy', 'dim'),
    )
)
```

You can still, if you want, use only the `font` function to ignore color
parameters and just style your text. See how:

Example 6:

``` Python
import color

print(
    '{I} {love} {linux}.'.format(
        I=color.font('I', 'bold'),
        love=color.red('<3', 'bold'),
        linux=color.font('Linux', 'dim'),
    )
)
```

### Background color

> New in version 1.0.0!

You can also color the background of your logs! To accomplish this, just
provide a `bg` parameter to any color function with the color name you want.

Example 7:

``` Python
import color

print(
    'The sun rules the {day} and the moon rules the {night}.'.format(
        day=color.yellow('day', bg='white')
        night=color.blue('night', bg='black'),
    )
)
```

The available colors are the same eight available to the text colors. We're
going to place a list with these color options below:

| Background color | Parameter   |
| ---------------- | ----------- |
| Black            | `'black'`   |
| Blue             | `'blue'`    |
| Cyan             | `'cyan'`    |
| Green            | `'green'`   |
| Magenta          | `'magenta'` |
| Red              | `'red'`     |
| White            | `'white'`   |
| Yellow           | `'yellow'`  |


If you want to use just the background color with no text color, just call the
`font` function, providing the `bg` parameter. You can also style the text
while choose your background color. See another example.

Example 8:

``` Python
import color

print(
    'The {white} {light} can split in a beautiful {ra}{i}{n}{b}{o}{w}.'.format(
        white=color.font('white', bg='white'),
        light=color.font('light', 'bold', bg='black'),
        ra=color.red('ra'),
        i=color.yellow('i'),
        n=color.green('n'),
        b=color.cyan('b'),
        o=color.blue('o'),
        w=color.magenta('w'),
    )
)
```


That's all folks!


## Who is this lib for?

PyTextColor is addressed to anyone who wants a simple lib to print colored
texts in the screen without a hundred of things to learn. You just need to
import the module and call the functions you want to.

PyTextColor doesn't match programmers that want a full-featured lib. It just
returns colored texts to be printed in the screen. No things more. If this is
your vibe, please, search for other python libraries (like colorama, or
PyColor).


## License

This lib is a free software and is distributed under the [MIT License](https://opensource.org/licenses/MIT).