# Repository instructions

## Preserve shadcn default styles

未经用户明确允许，不得修改或覆盖 shadcn 的默认样式。
Do not modify or override shadcn's default styles without the user's explicit
permission for the specific change.

- Render examples with the public `streamlit_shadcn_ui` API and the existing
  shadcn variants. Do not restyle controls through injected CSS, HTML wrappers,
  inherited styles, theme variables, or private frontend changes.
- This includes dimensions, padding, typography, text alignment, colors,
  borders, radii, shadows, focus rings, and interaction styles. Page layout
  must not override the controls' default appearance.
- Updating examples, improving touch usability, or publishing the site does
  not itself authorize style changes. If a change is needed, explain the
  affected defaults and proposed change, then obtain explicit permission.
  Reuse permission already given for that scope.
- Compare rendered examples with the package's default controls before shipping.
  Do not hide a library style defect with a documentation-only CSS override.

## Documentation mirror

The `ObservedObserver/streamlit-shadcn-ui` repository is the source of truth
for `Home.py`, `site_pages/`, `pages/`, and `docs/components/`. Make shared
example changes there first, then sync them here.

Pin `requirements.txt` to a version already published on PyPI. Validate the
examples with that installed package. Verify the live version and rendered
controls after pushing; a successful push alone is not a completed deployment.

Use semantic commit messages and leave unrelated user changes out of commits.
