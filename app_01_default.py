from utils import warning
from main_badge.main_badge import Badge, draw_badge
def enter(display) -> None:
    badge = Badge("main_badge/badge.txt", "main_badge/linked_in.bin")
    draw_badge(display, badge)
    display.update()

def process_a(display) -> None:
    badge = Badge("main_badge/badge.txt", "main_badge/linked_in.bin")
    draw_badge(display, badge)
    display.update()


def process_b(display) -> None:
    warning("Dummy module: process_b", display)


def process_c(display) -> None:
    warning("Dummy module: process_c", display)
