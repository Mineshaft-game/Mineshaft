from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="mineshaft2d",
    version="VERSION",
    description="Attempt to remake Minecraft in 2D",
    url="https://github.com/Mineshaft-game/mineshaft",
    author="Double Fractal Game Studios",
    author_email="mayu2kura1@gmail.com",
    license="Mineshaft License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["mineshaft2d"],
    install_requires=[
        "pygame>=2.0.1",
        "screeninfo",
        "libmineshaft>=0.1.2",
        "pygame-menu>=4.1.5",
        "python-lang>=1.0.0",
    ],
    classifiers=[
        "License :: Other/Proprietary License",
        "Topic :: Software Developement :: Libraries :: pygame",
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainement",
        "Topic :: Games/Entertainement :: Simulation",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
    ],
    keywords=[
        "Minecraft",
        "Mineshaft",
        "Pygame",
        "Minecraft clone",
        "2D",
        "Minecraft 2D",
        "Mineshaft 2D",
        "Minecraft remake",
    ],
)
