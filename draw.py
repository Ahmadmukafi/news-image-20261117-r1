#!/usr/bin/env python3
"""Render the news-image-20261117 front page: Tuesday 17 November 2026.

Draws a 1024x1024 editorial front page with PIL only. Deterministic:
same script, same bytes. Stories (all reported 17 Nov 2026 by BBC,
Al Jazeera, AP, Reuters, ULA):
  1. Ukraine strikes the Kerch Bridge (road span collapses); Russia
     hits two Kyiv bridges over the Dnipro in return.
  2. Tankers hit mines near the Strait of Hormuz; third US carrier
     (USS Theodore Roosevelt) arrives in the Middle East.
  3. Trump arrives in Manila for ASEAN, then to Shenzhen for APEC
     and a planned Xi-Trump-Putin meeting on Thursday.
  4. Five EU states plan a joint migrant return hub in Rwanda.
  5. ULA Vulcan rocket fails; 40 Amazon Leo satellites lost.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
NAVY = (20, 33, 61)
RED = (193, 18, 31)
STEEL = (70, 110, 140)
GOLD = (201, 162, 39)
TEAL = (14, 110, 110)
ORANGE = (230, 120, 30)
YELLOW = (245, 200, 60)
GREY = (90, 90, 90)

FD = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


F_TITLE = font("DejaVuSerif-Bold.ttf", 68)
F_DATE = font("DejaVuSans-Bold.ttf", 20)
F_KICK = font("DejaVuSans-Bold.ttf", 19)
F_HEAD = font("DejaVuSerif-Bold.ttf", 56)
F_SUB = font("DejaVuSans.ttf", 24)
F_BODY = font("DejaVuSans.ttf", 20)
F_CAP = font("DejaVuSans.ttf", 16)
F_PH = font("DejaVuSerif-Bold.ttf", 30)
F_PB = font("DejaVuSans.ttf", 18)
F_PB_B = font("DejaVuSans-Bold.ttf", 18)
F_FOOT = font("DejaVuSans.ttf", 15)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(text, fnt, x, y, max_w, leading, color=INK):
    for line in wrap(text, fnt, max_w):
        d.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def rule(x0, y, x1, color=INK, w=2):
    d.line([(x0, y), (x1, y)], fill=color, width=w)


def starburst(cx, cy, r, color):
    pts = []
    for i in range(24):
        ang = math.pi * i / 12
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=color)


# ---------- Masthead ----------
d.rectangle([0, 0, W, 96], fill=NAVY)
d.text((512, 8), "THE WORLD", font=F_TITLE, fill=(255, 255, 255), anchor="ma")
d.line([(24, 88), (1000, 88)], fill=GOLD, width=2)
# dateline strip
d.rectangle([0, 96, W, 130], fill=(255, 255, 255))
d.text((24, 102), "TUESDAY 17 NOVEMBER 2026", font=F_DATE, fill=RED)
d.text((1000, 102), "IN ONE IMAGE", font=F_DATE, fill=NAVY, anchor="ra")
rule(0, 130, W, INK, 3)

# ---------- Lead story: bridges ----------
d.text((24, 144), "EUROPE  ·  WAR IN UKRAINE", font=F_KICK, fill=RED)
d.text((24, 170), "BRIDGES", font=F_HEAD, fill=INK)
d.text((24, 228), "UNDER FIRE", font=F_HEAD, fill=INK)
d.text((24, 292), "Ukraine strikes Kerch Bridge;", font=F_SUB, fill=INK)
d.text((24, 320), "Russia hits Kyiv crossings", font=F_SUB, fill=INK)
para(
    "Kyiv says its strike collapsed a road span of the bridge linking "
    "Russia to occupied Crimea — the second hit in under 24 hours. "
    "Moscow answered with ballistic missiles on two Dnipro bridges in "
    "Kyiv, cutting heat, water and power. Russia says it downed a "
    "record 1,300+ drones.",
    F_BODY, 24, 352, 560, 27,
)

# Lead illustration: bridge panel x 616..1000, y 144..470
d.rectangle([616, 144, 1000, 470], fill=NAVY)
d.rectangle([616, 144, 1000, 470], outline=GOLD, width=3)
for (dx, dy) in [(660, 178), (720, 164), (790, 184), (860, 168), (940, 188)]:
    d.ellipse([dx - 4, dy - 3, dx + 4, dy + 3], fill=(255, 255, 255))
    d.line([(dx - 12, dy), (dx - 5, dy)], fill=(255, 255, 255), width=2)
d.rectangle([636, 318, 760, 334], fill=(220, 220, 220))
d.rectangle([896, 318, 980, 334], fill=(220, 220, 220))
d.polygon([(760, 318), (830, 360), (818, 374), (752, 334)], fill=(220, 220, 220))
for px in (660, 700, 740, 920, 960):
    d.line([(px, 334), (px, 360)], fill=(220, 220, 220), width=4)
starburst(828, 318, 44, ORANGE)
starburst(828, 318, 26, YELLOW)
d.ellipse([800, 238, 856, 288], fill=(120, 120, 120))
d.ellipse([760, 220, 806, 260], fill=(150, 150, 150))
d.ellipse([850, 228, 890, 260], fill=(140, 140, 140))
d.rectangle([616, 388, 1000, 470], fill=STEEL)
for wx in range(630, 990, 40):
    d.arc([wx, 408, wx + 36, 436], 180, 360, fill=(255, 255, 255), width=3)
    d.arc([wx + 10, 440, wx + 46, 462], 180, 360, fill=(255, 255, 255), width=3)
d.text((616, 478), "The Kerch Bridge, struck for a second day.", font=F_CAP, fill=GREY)
rule(0, 512, W, INK, 2)

# ---------- Row 2: Hormuz | Trump Asia ----------
d.text((24, 528), "MIDDLE EAST  ·  HORMUZ", font=F_KICK, fill=RED)
d.text((24, 552), "TANKERS HIT AS", font=F_PH, fill=INK)
d.text((24, 586), "THIRD U.S. CARRIER", font=F_PH, fill=INK)
d.text((24, 620), "ARRIVES", font=F_PH, fill=INK)
d.rectangle([24, 662, 500, 742], fill=(226, 232, 240))
d.polygon([(60, 706), (200, 706), (190, 734), (70, 734)], fill=(40, 40, 40))
for cx in (90, 120, 150, 180):
    d.rectangle([cx, 686, cx + 22, 706], fill=TEAL)
d.rectangle([300, 694, 470, 712], fill=(90, 90, 90))
d.rectangle([440, 670, 460, 694], fill=(90, 90, 90))
d.ellipse([410, 676, 434, 700], fill=RED)
for a in range(8):
    ang = math.pi * a / 4
    d.line([(422 + 14 * math.cos(ang), 688 + 14 * math.sin(ang)),
            (422 + 22 * math.cos(ang), 688 + 22 * math.sin(ang))],
           fill=RED, width=3)
starburst(250, 724, 20, ORANGE)
para(
    "Two tankers struck mines and caught fire near the Strait of "
    "Hormuz. The USS Theodore Roosevelt joined two U.S. carriers "
    "there.",
    F_PB, 24, 750, 470, 23,
)
d.line([(512, 528), (512, 836)], fill=INK, width=2)
d.text((524, 528), "ASIA  ·  DIPLOMACY", font=F_KICK, fill=RED)
d.text((524, 552), "TRUMP HEADS TO ASIA", font=F_PH, fill=INK)
d.text((524, 586), "FOR XI–PUTIN TALKS", font=F_PH, fill=INK)
for i, (fx, cols) in enumerate([
        (524, [(200, 30, 40), (255, 255, 255), (200, 30, 40)]),
        (640, [(220, 30, 30), (220, 30, 30), (220, 30, 30)]),
        (756, [(255, 255, 255), (0, 60, 160), (220, 30, 30)])]):
    for j, c in enumerate(cols):
        d.rectangle([fx, 668 + j * 14, fx + 100, 668 + (j + 1) * 14], fill=c)
    d.rectangle([fx, 668, fx + 100, 710], outline=INK, width=2)
d.text((530, 668), "★", font=font("DejaVuSans.ttf", 16), fill=(255, 255, 255))
d.text((646, 668), "★", font=font("DejaVuSans.ttf", 16), fill=(255, 220, 60))
d.text((524, 718), "MANILA  →  SHENZHEN", font=F_PB_B, fill=NAVY)
para(
    "Trump arrived in Manila for ASEAN, then flies to Shenzhen for "
    "APEC — and a planned three-way meeting with Xi and Putin on "
    "Thursday.",
    F_PB, 524, 750, 470, 23,
)
rule(0, 836, W, INK, 2)

# ---------- Row 3: Rwanda hub | Vulcan ----------
d.text((24, 850), "EUROPE  ·  MIGRATION", font=F_KICK, fill=RED)
d.text((24, 874), "FIVE EU STATES PLAN", font=F_PH, fill=INK)
d.text((24, 902), "RWANDA RETURN HUB", font=F_PH, fill=INK)
para(
    "Germany, Denmark, Austria, Greece and the Netherlands plan a "
    "joint Rwanda return hub.",
    F_PB, 24, 936, 470, 22,
)
d.line([(512, 850), (512, 984)], fill=INK, width=2)
d.text((524, 850), "SPACE  ·  TECHNOLOGY", font=F_KICK, fill=RED)
d.text((524, 874), "VULCAN ROCKET FAILS;", font=F_PH, fill=INK)
d.text((524, 902), "40 SATELLITES LOST", font=F_PH, fill=INK)
para(
    "A ULA Vulcan rocket failed after launch from Cape Canaveral, "
    "destroying 40 Amazon Leo satellites.",
    F_PB, 524, 936, 470, 22,
)

# ---------- Footer ----------
rule(0, 988, W, INK, 2)
d.text((24, 996), "Sources: BBC · Al Jazeera · AP · Reuters · ULA", font=F_FOOT, fill=GREY)
d.text((1000, 996), "news-image-20261117", font=F_FOOT, fill=GREY, anchor="ra")

img.save("entry.png", optimize=True)
print("saved entry.png", os.path.getsize("entry.png"), "bytes")
