import setuptools


setuptools.setup(
    name='color-lib',
    version='0.0.1',
    author='Italo Campos',
    author_email='italo.ramon.campos@gmail.com',
    description='A small Python 3.x lib to speed up the coloring usage'
    'throughout your Python projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/italocampos/color',
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
