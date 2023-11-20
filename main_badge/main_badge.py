import time
import badger2040
import config

# Global Constants
WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

IMAGE_WIDTH = config.IMAGE_SIZE

NAME_HEIGHT = 20
TEXT_WIDTH = WIDTH - IMAGE_WIDTH

NAME_TEXT_SIZE = 0.6
DETAILS_TEXT_SIZE = 0.5

LEFT_PADDING = 5
NAME_PADDING = 20
DETAIL_SPACING = 10


# ------------------------------
#      Utility functions
# ------------------------------
#
# Reduce the size of a string until it fits within a given width
# def truncatestring(text, text_size, width):
#     while True:
#         length = display.measure_text(text, text_size)
#         if length > 0 and length > width:
#             text = text[:-1]
#         else:
#             text += ""
#             return text

def read_badge_from_file(text_file, image_file):
    with open(text_file, "r") as f:
        lines = f.readlines()

    BADGE_IMAGE = bytearray(int(IMAGE_WIDTH * IMAGE_WIDTH / 8))
    open(image_file, "rb").readinto(BADGE_IMAGE)
    return lines, BADGE_IMAGE


# ------------------------------
#      Drawing functions
# ------------------------------
class Badge:
    def __init__(self, lines, image, sizes=None, boxes=None):

        self.image = image
        self.lines = lines

        self.sizes = sizes
        if self.sizes is None:
            self.sizes = [2] + [1] * (len(self.lines) - 1)

        self.boxes = boxes
        if self.boxes is None:
            self.boxes = [0, 0, 1] + [0] * (len(lines) - 2)


def calc_text_size(display, text, box_size, max_width):
    name_size = 2
    name_length = 1000
    while (name_length // len(text)) * 1.7 > box_size or name_length > max_width + 5:
        name_length = display.measure_text(text, name_size)
        name_size -= 0.1
    return name_size


# Draw the badge, including user text
def draw_badge(display, badge: Badge):
    lines = badge.lines
    sizes = badge.sizes
    if badge.boxes is None:
        edges = [0] * len(lines)
    else:
        edges = badge.boxes

    modifier = HEIGHT // sum(sizes)
    boxes = [(LEFT_PADDING, round(sum(sizes[j] for j in range(i)) * modifier))
             for i in range(len(lines) + 1)]
    # boxes.append((LEFT_PADDING, HEIGHT))
    # display.invert(0)  # Invert the display 0-15 black to white
    display.pen(15)  # WHITE
    display.clear()
    # White background for text
    # display.pen(15) # BLACK
    # display.rectangle(1, 1, WIDTH - 2, HEIGHT - 2)

    # Draw badge image
    display.image(badge.image, IMAGE_WIDTH, IMAGE_WIDTH, WIDTH - IMAGE_WIDTH - 1, 1)

    display.pen(0)
    display.text("^More here^", TEXT_WIDTH + 5, HEIGHT - 10, 0.6)

    display.pen(0)
    for i in range(0, len(lines)):
        display.font("sans")
        display.thickness(1)
        name_size = calc_text_size(display, lines[i], boxes[i + 1][1] - boxes[i][1], TEXT_WIDTH)

        display.text(lines[i],
                     boxes[i][0],
                     (boxes[i][1] + boxes[i + 1][1]) // 2
                     + 5 * ((1 - edges[i + 1]))
                     - 5 * ((1 - edges[i])),
                     name_size)

    display.line(0, 0, WIDTH, 0)
    for i in range(1, len(boxes) - 1):
        if edges[i]:
            display.line(0, boxes[i][1], TEXT_WIDTH - 1, boxes[i][1])
    display.line(0, 0, 0, HEIGHT)
    display.line(0, HEIGHT - 1, WIDTH, HEIGHT - 1)
