from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='mineshaft2d',
    version='VERSION',
    description='Attempt to remake Minecraft in 2D',
    url='https://github.com/Mineshaft-game/mineshaft',
    author='Double Fractal Game Studios',
    author_email='mayu2kura1@gmail.com',
    license='Mineshaft License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['mineshaft2d'],
    install_requires=[
                      'pygame>=2.0.1',
                      'screeninfo',
                      'libmineshaft>=0.1.2',
                      'pygame-menu'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
    ],
)
