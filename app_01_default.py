from utils import warning
from main_badge.main_badge import Badge, draw_badge, read_badge_from_file

lines, img = read_badge_from_file("main_badge/badge.txt", "main_badge/linked_in.bin")
sizes = [2, 0.5, 1, 1]
badge = Badge(lines, img, sizes=sizes)
def enter(display) -> None:
    draw_badge(display, badge)
    display.update()

def process_a(display) -> None:
    draw_badge(display, badge)
    display.update()


def process_b(display) -> None:
    warning("Dummy module: process_b", display)


def process_c(display) -> None:
    warning("Dummy module: process_c", display)
