import os


def join_muspath(name: str):
    return os.path.join("assets", "audio", "music", name)


menu1 = join_muspath("menu1.ogg")
menu2 = join_muspath("menu2.ogg")

piano1 = join_muspath("piano1.ogg")


MENU = [menu1, menu2, piano1]
