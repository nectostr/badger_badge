from utils import warning
from main_badge.main_badge import Badge, draw_badge
def enter(display) -> None:
    warning("Dummy module: enter state", display)

def process_a(display) -> None:
    warning("Dummy module: process_a", display)


def process_b(display) -> None:
    warning("Dummy module: process_b", display)


def process_c(display) -> None:
    warning("Dummy module: process_c", display)
