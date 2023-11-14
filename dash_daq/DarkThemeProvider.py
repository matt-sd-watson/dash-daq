# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DarkThemeProvider(Component):
    """A DarkThemeProvider component.
DarkThemeProvider is a component that is placed at the root of
the component tree to make all components match the dark theme

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional):
    The children of this component.

- theme (dict; optional):
    Theme object to override with a custom theme.

    `theme` is a dict with keys:

    - dark (boolean; optional):
        True for Dark mode, False for Light.

    - detail (string; optional):
        Color used for UI details, like borders.

    - primary (string; optional):
        Highlight color.

    - secondary (string; optional):
        Supporting color."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_daq'
    _type = 'DarkThemeProvider'
    @_explicitize_args
    def __init__(self, children=None, theme=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DarkThemeProvider, self).__init__(children=children, **args)
