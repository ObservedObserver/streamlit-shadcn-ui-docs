# P0 documentation promotion checklist

Status: draft, blocked on the next package publication and requirements pin
update. Do not merge or deploy this branch yet.

`Home.py`, `site_pages/`, `pages/`, and `docs/components/` are exact source
mirrors of the main library repository. Changes to shared examples must be
made there first. The support matrix is copied with them so its relative
links remain usable.

This draft includes Sheet, Elements containers, Item, and Data Table. All 12
updated source files match the final main snapshot byte for byte, including
the support matrix and P0 acceptance record. The source is the November 6, 2026
commit [feat(data-table): add interactive record management table](https://github.com/ObservedObserver/streamlit-shadcn-ui/commit/4603c1fa6b6efed66ce29efdb9192092f3467e5e),
revision `4603c1fa6b6efed66ce29efdb9192092f3467e5e`.

`requirements.txt` intentionally remains pinned to the published
`streamlit-shadcn-ui==1.4.0`. That version cannot run the new P0 APIs. No next
version is assumed, and no package or live documentation update has been
performed by this draft.

Before promotion:

- [ ] Confirm the library package containing all four P0 changes is published
  on PyPI. Record the actual published version and source revision.
- [ ] Update `requirements.txt` to that published version and revise the
  release notes in README. Remove the draft notice only after validation.
- [ ] Choose and lock a verified Streamlit hosting dependency set before
  promotion. The P0 wheel was independently validated with Streamlit 1.60.0
  and Starlette 1.3.1. A fresh install that resolves Starlette 1.10 can hit an
  upstream gzip/ASGI static-asset failure. Keeping Streamlit 1.60.0 therefore
  requires pinning Starlette 1.3.1; alternatively upgrade Streamlit and repeat
  the installed-package and browser checks. Streamlit 1.61.1 declares a
  Starlette upper bound below 1.4 in its [dependency metadata](https://github.com/streamlit/streamlit/blob/1.61.1/lib/pyproject.toml#L83-L95).
  This draft leaves the existing requirements unchanged.
- [ ] Install from the published package in a clean environment. Do not rely
  on an editable checkout of the library when validating these examples.
- [ ] Exercise the records page, Sheet, nested panels, Item actions and
  existing examples with the installed package. Verify callbacks, reruns,
  keyboard/focus, narrow layouts, and default shadcn appearance.
- [ ] Check exact parity of the shared source files against the release
  source; fix shared examples upstream and re-sync if needed.
- [ ] Merge the documentation update only after these checks pass.
- [ ] Verify the live site separately: confirm the reported package version,
  navigation, new pages, rendered default controls and interaction behavior.
  A successful commit, push, or deployment job is not live verification.

Draft checks passed: all 104 shared example and component-documentation files
match the source snapshot; the support matrix and acceptance record match too.
All 55 Python pages and six Python snippets in the four changed component docs
parse successfully. Requirements are unchanged. Published-package and live-site
checks remain pending until promotion; the source acceptance record documents
the separate development-wheel verification.
