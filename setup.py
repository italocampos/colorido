import setuptools


setuptools.setup(
    name='colorido',
    version='1.0.0',
    author='Italo Campos',
    author_email='italo.ramon.campos@gmail.com',
    description='A small Python 3.x lib to speed up the coloring usage'
    'throughout your Python projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/italocampos/colorido',
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
