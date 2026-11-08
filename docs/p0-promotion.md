# 1.5.0 documentation promotion checklist

Status: 1.5.0 is published on PyPI, documentation PR #3 is merged, and both
published-package and live-site acceptance are complete. The
[publication verification report](releases/1.5.0-verification.md) records the
separate package, installation and online checks.

`Home.py`, `site_pages/`, `pages/`, and `docs/components/` are source mirrors
of the main library repository. Change shared examples there first. Copy the
support matrix and P0 acceptance record with them so relative links remain
usable.

This update includes Sheet, Elements containers, Item, and Data Table. All
104 shared files, `CHANGELOG.md`, both 1.5.0 release reports, the support matrix
and P0 acceptance record match the November 7, 2026 commit
[test: record v1.5.0 publication and live acceptance](https://github.com/ObservedObserver/streamlit-shadcn-ui/commit/a6c18cf07af96375e743e858e1a406830a358bd6).
Home and Getting Started read the installed package version from distribution
metadata. The reports identify the original package release source separately.

`requirements.txt` pins the published `streamlit-shadcn-ui==1.5.0` package.
The host dependencies are pinned to Streamlit 1.60.0 and Starlette 1.3.1.
The published PyPI package passed 45 browser cases with that combination.
A fresh install that resolves Starlette 1.10 can hit an upstream gzip/ASGI
static-asset failure. Streamlit 1.61.1 declares a Starlette upper bound below
1.4 in its [dependency metadata](https://github.com/streamlit/streamlit/blob/1.61.1/lib/pyproject.toml#L83-L95).
Changing this host combination requires fresh installed-package and browser
acceptance.

## Publication and installation

- [x] Confirm `streamlit-shadcn-ui==1.5.0` is published on PyPI. The wheel and
  source archive match the release source recorded in the verification report.
- [x] Verify the published wheel and source archive against the release hashes.
- [x] Mirror the final release source, including Homepage and Getting Started
  displays that read the installed package version. Check exact file parity
  and record the source revision here.
- [x] Update `requirements.txt` to `streamlit-shadcn-ui==1.5.0` after publication.
  Retain `streamlit==1.60.0` and `starlette==1.3.1` for this deployment.
- [x] Install the published package in a clean environment. Verify imports
  come from that environment's `site-packages`, with no editable source
  checkout on the import path.
- [x] Exercise the records page, Sheet, nested panels, Item actions and
  existing examples with the installed package. Verify callbacks, reruns,
  keyboard and focus behavior, narrow layouts and default shadcn appearance.
- [x] Recheck Python examples, Markdown snippets and shared-source parity.
- [x] Mark PR #3 ready and merge after publication and installation checks
  pass. [PR #3](https://github.com/ObservedObserver/streamlit-shadcn-ui-docs/pull/3)
  merged on November 7, 2026.

The coordinator downloaded the public PyPI wheel and source archive and
confirmed both SHA-256 hashes match the local release artifacts. Installation
used `uv --no-cache --reinstall` from the public PyPI simple index. Metadata
reported 1.5.0, imports resolved to the environment's `site-packages`, and no
`direct_url.json` pointed at a local checkout.

All 45 published-package browser cases passed on Python 3.14.2 across Chromium,
Firefox and WebKit: 21 Sheet, six Elements containers, three Item and 15 Data
Table cases.
The first containers run hit a Firefox test race when it clicked an old tab
while a native Streamlit rerun was reordering the controls. Trace review
confirmed the cause. The test now waits for the new order; all six container
cases then passed. Runtime code was unchanged.

All 55 documentation apps ran against the public package without Python
exceptions on both Python 3.14.2 and Python 3.10.9. The second environment
matches Community Cloud's configured Python 3.10 version. Source checks also
passed for 55 Python files and six Python snippets in the four changed
component documents. The 109 mirrored files match the recorded main source
byte for byte. Requirements pin the verified package and host versions.

## Live verification

- [x] Wait for Community Cloud to install the updated requirements and serve
  the updated app at [shadcn.streamlit.app](https://shadcn.streamlit.app/).
- [x] Confirm Home and Getting Started report installed package version
  `1.5.0`, and the Streamlit main menu reports the expected host version.
- [x] Verify navigation, Sheet, Item, Elements containers and Data Table,
  including editing and saving a record. Check the rendered default controls.
- [x] Record the live verification result separately from package acceptance.
  A successful commit, merge or deployment job does not prove the live app
  has updated.

The Cloud console retained the historical repository name
`steamlit-shadcn-ui-docs`. GitHub confirmed it is an alias of the same renamed
repository, not a separate deployment repository. A manual reboot of the
existing app loaded the merged source and package. Hosting settings did not
change.

The coordinator checked the public site in the real Chrome browser after the
reboot. Getting Started reported installed package 1.5.0, Home reported 1.5.0
and 49 documented components, and the app menu reported Streamlit 1.60.0.
Sheet Save preserved an edited name while the panel stayed open; Done closed
it. Item Manage returned its selected action. Elements preserved drafts
across tabs, and its expansion and bounded scrolling worked. Data Table
filtered Beta and Alpha, opened the record editor and saved the name
`Alpha verified` back to the table. The example session held these edits.

Published-package acceptance and live-site acceptance are complete. The
verification report records their different environments and coverage.
