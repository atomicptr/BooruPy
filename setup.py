from distutils.core import setup

setup(
    name='BooruPy',
    version='0.1.5',
    keywords = ['pictures', 'anime', 'booru', 'gelbooru', 'danbooru', 'image',
     'board', 'imageboard'],
    author='Christopher Kaster',
    author_email='ikasoki@gmail.com',
    maintainer='Giuliano Di Pasquale',
    maintainer_email='gdipasquale@gmx.de',
    packages=['BooruPy'],
    url='http://github.com/Kasoki/BooruPy',
    license='GNU GENERAL PUBLIC LICENSE',
    description='BooruPy is a simple library for interacting with various image board "Booru" systems.',
    long_description=open('README.rst').read(),
    platforms='OS Independent',
    classifiers= [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
    ]
)
