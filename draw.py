#!/usr/bin/env python3
"""Draw the front page for Wednesday 25 November 2026 and save entry.png.

Flat newspaper style: navy masthead, red date strip, one lead story and
five numbered stories, plus a markets strip along the bottom.
Run:  python3 draw.py   (writes entry.png next to this file)
"""
import os

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
NAVY = (22, 38, 63)
RED = (193, 39, 45)
INK = (26, 26, 26)
GREY = (85, 85, 85)
RULE = (221, 221, 221)
WHITE = (255, 255, 255)

W, H = 1024, 1024
MARGIN = 40
CONTENT = W - 2 * MARGIN


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, max_width):
    """Split text into lines that fit max_width pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


LEAD = {
    "kicker": "MIDDLE EAST",
    "headline": ["TANKERS HIT MINES", "IN THE STRAIT OF HORMUZ"],
    "summary": (
        "Iran says two oil tankers struck naval mines and caught fire "
        "in the Strait of Hormuz, the world's busiest oil waterway."
    ),
}

STORIES = [
    {
        "kicker": "MARKETS",
        "headline": "AI rally fades as Nvidia sinks",
        "summary": "Nvidia fell about 6% and Tokyo's Nikkei dropped 2.8%.",
    },
    {
        "kicker": "CLIMATE",
        "headline": "COP31 collapses in Antalya",
        "summary": "No deal at COP31 as oil states block a fossil-fuel phase-out.",
    },
    {
        "kicker": "SPACE",
        "headline": "Pakistan's first astronaut reaches Tiangong",
        "summary": "Zeeshan Ali becomes the first foreign visitor to Tiangong.",
    },
    {
        "kicker": "COLOMBIA",
        "headline": "All hostages freed in Cartagena siege",
        "summary": "Forces stormed a supermarket and freed the last hostages.",
    },
    {
        "kicker": "FOOTBALL",
        "headline": "Senegal wins back Africa Cup title",
        "summary": "A sports court restored Senegal as Africa Cup champions.",
    },
]

MARKETS = "MARKETS   \u2022   NIKKEI -2.8%   \u2022   S&P 500 -0.5%   \u2022   BRENT $87.49"


def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # Masthead: navy bar with the paper's name.
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.text((W // 2, 76), "THE WORLD TODAY",
           font=font("DejaVuSerif-Bold.ttf", 84), fill=WHITE, anchor="mm")

    # Date strip, directly under the masthead.
    d.rectangle([0, 148, W, 212], fill=RED)
    d.text((W // 2, 180), "WEDNESDAY, 25 NOVEMBER 2026",
           font=font("DejaVuSans-Bold.ttf", 40), fill=WHITE, anchor="mm")

    # Lead story.
    d.rectangle([MARGIN, 236, MARGIN + 12, 484], fill=RED)
    x = MARGIN + 32
    d.text((x, 236), LEAD["kicker"], font=font("DejaVuSans-Bold.ttf", 26),
           fill=RED, anchor="la")
    head_f = font("DejaVuSans-Bold.ttf", 56)
    d.text((x, 268), LEAD["headline"][0], font=head_f, fill=NAVY, anchor="la")
    d.text((x, 332), LEAD["headline"][1], font=head_f, fill=NAVY, anchor="la")
    sum_f = font("DejaVuSans.ttf", 28)
    lines = wrap(d, LEAD["summary"], sum_f, W - x - MARGIN)
    y = 410
    for line in lines:
        d.text((x, y), line, font=sum_f, fill=INK, anchor="la")
        y += 38
    d.line([(MARGIN, 504), (W - MARGIN, 504)], fill=NAVY, width=3)

    # Numbered stories.
    kick_f = font("DejaVuSans-Bold.ttf", 26)
    head2_f = font("DejaVuSans-Bold.ttf", 30)
    sum2_f = font("DejaVuSans.ttf", 25)
    num_f = font("DejaVuSans-Bold.ttf", 30)
    row_y = 524
    row_h = 84
    for i, story in enumerate(STORIES):
        # Red number disc.
        d.ellipse([MARGIN, row_y + 6, MARGIN + 46, row_y + 52], fill=RED)
        d.text((MARGIN + 23, row_y + 29), str(i + 1), font=num_f,
               fill=WHITE, anchor="mm")
        tx = MARGIN + 64
        # Kicker in red, headline in navy, on one line.
        d.text((tx, row_y + 6), story["kicker"], font=kick_f, fill=RED, anchor="la")
        kw = d.textlength(story["kicker"], font=kick_f)
        d.text((tx + kw + 14, row_y + 4), story["headline"], font=head2_f,
               fill=NAVY, anchor="la")
        d.text((tx, row_y + 46), story["summary"], font=sum2_f, fill=GREY, anchor="la")
        if i < len(STORIES) - 1:
            d.line([(MARGIN, row_y + row_h - 6), (W - MARGIN, row_y + row_h - 6)],
                   fill=RULE, width=2)
        row_y += row_h

    # Markets strip along the bottom. Shrink the font until the line fits.
    d.rectangle([0, 948, W, H], fill=NAVY)
    strip_size = 28
    while True:
        strip_f = font("DejaVuSans-Bold.ttf", strip_size)
        if d.textlength(MARKETS, font=strip_f) <= W - 2 * MARGIN:
            break
        strip_size -= 1
    d.text((W // 2, 986), MARKETS, font=strip_f, fill=WHITE, anchor="mm")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
