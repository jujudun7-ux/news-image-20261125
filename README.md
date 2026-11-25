# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/jujudun7-ux/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/jujudun7-ux/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A newspaper front page that sums up the world's news of Wednesday,
25 November 2026, in one image. The lead story is the two tankers
reported hit by mines in the Strait of Hormuz; the page also covers
the AI sell-off, the collapse of the COP31 climate talks, Pakistan's
first astronaut reaching Tiangong, the freed hostages in Cartagena,
and Senegal winning back the Africa Cup title, with a markets strip
along the bottom.

This is an entry for the make.fun bounty
[news-image-20261125](https://make.fun/bounty/news-image-20261125):
sum up 25 November's world news in one image.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. It writes the same bytes on every run.

## How the image was made

`entry.png` (1024x1024) was drawn by `draw.py` with Pillow, in a flat
newspaper style: a navy masthead, a red date strip, one lead story and
five numbered stories, and a markets strip. The stories and figures
were checked against news reports of the day; see `NEWS.md` for the
six stories and their sources.
