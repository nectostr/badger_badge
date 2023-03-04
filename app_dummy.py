from utils import warning
from main_badge import main_badge

def enter(display) -> None:
    main_badge.main(display)

def process_a(display) -> None:
    main_badge.main(display)


def process_b(display) -> None:
    warning("Dummy module: process_b", display)


def process_c(display) -> None:
    warning("Dummy module: process_c", display)
