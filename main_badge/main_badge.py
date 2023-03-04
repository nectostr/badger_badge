import time
import badger2040
import config

# Global Constants
WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

IMAGE_WIDTH = config.IMAGE_SIZE

NAME_HEIGHT = 20
TEXT_WIDTH = WIDTH - IMAGE_WIDTH

COMPANY_TEXT_SIZE = 0.6
DETAILS_TEXT_SIZE = 0.5

LEFT_PADDING = 5
NAME_PADDING = 20
DETAIL_SPACING = 10




# ------------------------------
#      Utility functions
# ------------------------------

# Reduce the size of a string until it fits within a given width
# def truncatestring(text, text_size, width):
#     while True:
#         length = display.measure_text(text, text_size)
#         if length > 0 and length > width:
#             text = text[:-1]
#         else:
#             text += ""
#             return text


# ------------------------------
#      Drawing functions
# ------------------------------
class Badge:
    def __init__(self, name, company, details, image):
        self.name = name
        self.company = company
        self.details = details
        self.image = image

# Draw the badge, including user text
def draw_badge(display, badge: Badge):
    display.pen(0)
    display.clear()

    # Draw badge image
    display.image(badge.image, IMAGE_WIDTH, IMAGE_WIDTH, WIDTH - IMAGE_WIDTH, 0)

    # Draw a border around the image
    display.pen(0)
    display.thickness(1)
    display.line(WIDTH - IMAGE_WIDTH, 0, WIDTH - 1, 0)
    display.line(WIDTH - IMAGE_WIDTH, 0, WIDTH - IMAGE_WIDTH, IMAGE_WIDTH - 1)
    display.line(WIDTH - IMAGE_WIDTH, IMAGE_WIDTH - 1, WIDTH - 1, IMAGE_WIDTH - 1)
    display.line(WIDTH - 1, 0, WIDTH - 1, IMAGE_WIDTH - 1)

    # Uncomment this if a white background is wanted behind the company
    display.pen(15)
    display.rectangle(1, 1, TEXT_WIDTH, NAME_HEIGHT - 1)

    # Draw the name
    display.pen(15)  # Change this to 0 if a white background is used
    display.font("serif")
    display.thickness(3)
    display.text(badge.name, LEFT_PADDING, (NAME_HEIGHT // 2) + 1, COMPANY_TEXT_SIZE)
    #
    # # Draw a white background behind the name
    # display.pen(15)
    # display.thickness(1)
    # display.rectangle(1, COMPANY_HEIGHT + 1, TEXT_WIDTH, NAME_HEIGHT)
    #
    # # Draw the name, scaling it based on the available width
    # display.pen(0)
    # display.font("sans")
    # display.thickness(4)
    # name_size = 2.0  # A sensible starting scale
    # while True:
    #     name_length = display.measure_text(name, name_size)
    #     if name_length >= (TEXT_WIDTH - NAME_PADDING) and name_size >= 0.1:
    #         name_size -= 0.01
    #     else:
    #         display.text(name, (TEXT_WIDTH - name_length) // 2, (NAME_HEIGHT // 2) + COMPANY_HEIGHT + 1, name_size)
    #         break
    #
    # # Draw a white backgrounds behind the details
    # display.pen(15)
    # display.thickness(1)
    # display.rectangle(1, HEIGHT - DETAILS_HEIGHT * 2, TEXT_WIDTH, DETAILS_HEIGHT - 1)
    # display.rectangle(1, HEIGHT - DETAILS_HEIGHT, TEXT_WIDTH, DETAILS_HEIGHT - 1)
    #
    # # Draw the first detail's title and text
    # display.pen(0)
    # display.font("sans")
    # display.thickness(3)
    # name_length = display.measure_text(detail1_title, DETAILS_TEXT_SIZE)
    # display.text(detail1_title, LEFT_PADDING, HEIGHT - ((DETAILS_HEIGHT * 3) // 2), DETAILS_TEXT_SIZE)
    # display.thickness(2)
    # display.text(detail1_text, 5 + name_length + DETAIL_SPACING, HEIGHT - ((DETAILS_HEIGHT * 3) // 2), DETAILS_TEXT_SIZE)
    #
    # # Draw the second detail's title and text
    # display.thickness(3)
    # name_length = display.measure_text(detail2_title, DETAILS_TEXT_SIZE)
    # display.text(detail2_title, LEFT_PADDING, HEIGHT - (DETAILS_HEIGHT // 2), DETAILS_TEXT_SIZE)
    # display.thickness(2)
    # display.text(detail2_text, LEFT_PADDING + name_length + DETAIL_SPACING, HEIGHT - (DETAILS_HEIGHT // 2), DETAILS_TEXT_SIZE)


# ------------------------------
#        Program setup
# ------------------------------

def main(display):
# Create a new Badger and set it to update NORMAL

    # Open the badge file

    # # Read in the next 6 lines
    with open("badge.txt", "r") as f:
        name = f.readline().strip()
        company = f.readline().strip()
        details = f.readline().strip()
    BADGE_IMAGE = bytearray(int(IMAGE_WIDTH * IMAGE_WIDTH / 8))
    open("badge-image.bin", "rb").readinto(BADGE_IMAGE)
    badge = Badge(name, company, details, BADGE_IMAGE)
    draw_badge(display, badge)
    display.update()
    # while True:
    #     display.update()
    #     # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    #     display.halt()