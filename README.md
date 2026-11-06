# Streamlit Shadcn UI documentation

> Draft only: this branch prepares the next component documentation update.
> Its new examples require an unpublished package and must not be deployed
> with the retained `streamlit-shadcn-ui==1.4.0` pin. Complete the
> [promotion checklist](docs/p0-promotion.md) before merging.

[![PyPI - Version](https://img.shields.io/pypi/v/streamlit-shadcn-ui)](https://pypi.org/project/streamlit-shadcn-ui/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shadcn.streamlit.app/)

Deployment mirror for the documentation app maintained in the
[Streamlit Shadcn UI repository](https://github.com/ObservedObserver/streamlit-shadcn-ui).
The main repository is the source of truth for `Home.py`, `site_pages/`,
`pages/`, `docs/components/`, and the published migration guide.

The app uses Streamlit Components V2 with checked-in shadcn source backed
by Base UI. It requires Python 3.10 or newer and Streamlit 1.60 or newer.

The deployed examples are pinned to `streamlit-shadcn-ui==1.4.0`. The Charts
page demonstrates line, area, bar, pie, radar, and radial charts with shadcn's
colorful light and dark palettes. **Use Cases > V2 Elements** demonstrates
composing multiple controls in one React tree.

## Installation

```bash
pip install streamlit-shadcn-ui
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run Home.py
```
