from utils import warning
from main_badge.main_badge import Badge, draw_badge, read_badge_from_file

lines, img = read_badge_from_file("main_badge/contact.txt", "main_badge/website.bin")
sizes = [2, 2, 1, 1]
badge = Badge(lines, img, sizes=sizes)


def enter(display) -> None:
    draw_badge(display, badge)
    display.update()


def process_a(display) -> None:
    badge.lines = lines
    draw_badge(display, badge)
    display.update()


def process_b(display) -> None:
    new_lines = badge.lines.copy()
    new_lines[1] = " "*len(new_lines[1])
    badge.lines = new_lines
    draw_badge(display, badge)
    display.update()


def process_c(display) -> None:
    new_lines = badge.lines.copy()
    new_lines[2] = " "*len(new_lines[2])
    badge.lines = new_lines
    draw_badge(display, badge)
    display.update()
