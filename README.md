[![news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Ahmadmukafi/news-image-20261117-r1/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Ahmadmukafi/news-image-20261117-r1/reward.svg)](https://make.fun/bounty/news-image-20261117)

# The World in One Image — Tuesday 17 November 2026

An editorial front page that sums up the day's world news in a single
1024×1024 image. The image is drawn entirely in code (`draw.py`, PIL):
a newspaper front page with a masthead, a lead story, and four more
stories — every headline legible, no photograph, no generated image.

## Stories covered (all reported 17 November 2026)

1. **Bridges under fire (lead)** — Ukraine struck the Kerch Bridge to
   Crimea and a road span collapsed, the second hit in under 24 hours;
   Russia answered with ballistic missiles on two bridges over the
   Dnipro in Kyiv. Sources: BBC, Al Jazeera, AP.
2. **Hormuz** — Two oil tankers struck mines and caught fire near the
   Strait of Hormuz; the USS Theodore Roosevelt arrived, giving the US
   three carriers in the region. Sources: Al Jazeera, Reuters.
3. **Trump heads to Asia** — Trump arrived in Manila for ASEAN, then
   flies to Shenzhen for APEC and a planned three-way meeting with Xi
   Jinping and Vladimir Putin on Thursday. Source: AP.
4. **Five EU states plan a Rwanda return hub** — Germany, Denmark,
   Austria, Greece and the Netherlands will set up a joint facility in
   Rwanda for rejected asylum seekers.
5. **Vulcan rocket fails** — A ULA Vulcan rocket failed minutes after
   launch from Cape Canaveral, destroying 40 Amazon Leo satellites.
   Source: ULA / Spaceflight Now.

## How it works

`main.ts` copies the bundled `entry.png` (rendered by `draw.py`) to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). The program runs
twice and writes byte-identical output; it uses no network.

## License

MIT — see `LICENSE`.
