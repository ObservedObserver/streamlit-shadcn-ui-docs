# Streamlit Shadcn UI documentation

[![PyPI - Version](https://img.shields.io/pypi/v/streamlit-shadcn-ui)](https://pypi.org/project/streamlit-shadcn-ui/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shadcn.streamlit.app/)

Deployment mirror for the documentation app maintained in the
[Streamlit Shadcn UI repository](https://github.com/ObservedObserver/streamlit-shadcn-ui).
The main repository is the source of truth for `Home.py`, `site_pages/`,
`pages/`, `docs/components/`, and the published migration guide.

The app uses Streamlit Components V2 with checked-in shadcn source backed
by Base UI. It requires Python 3.10 or newer and Streamlit 1.60 or newer.

The 1.5.0 documentation update adds Sheet, Item, an interactive Data Table,
and Tabs, Accordion, Collapsible and Scroll Area composition in Elements.
The Data Table example opens a Sheet to edit and save a record. The catalog
contains 49 documented components.

The examples pin the published `streamlit-shadcn-ui==1.5.0` package. The
documentation host pins Streamlit 1.60.0 and Starlette 1.3.1, the combination
used for P0 acceptance. The [promotion checklist](docs/p0-promotion.md) tracks
the separate installed-package and live-site verification.

## Installation

```bash
pip install streamlit-shadcn-ui
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run Home.py
```
