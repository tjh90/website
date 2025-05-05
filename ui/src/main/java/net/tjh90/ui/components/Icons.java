package net.tjh90.ui.components;

import net.tjh90.ui.views.CssClassNames;

public enum Icons {

    /// Github brand icon.
    GITHUB(CssClassNames.GITHUB_ICON),

    /// Book icon used for PhD thesis.
    PHD_THESIS(CssClassNames.PHD_THESIS_ICON),

    /// Document icon used for paper.
    PAPER(CssClassNames.PAPER_ICON);

    private final String cssClassName;

    /// Constructor.
    ///
    /// @param cssClassName the Font Awesome class name for the icon.
    private Icons(final String cssClassName) {
        this.cssClassName = cssClassName;
    }

    /// @returns a new [Icon] using the supplied `cssClassName`.
    public Icon create() {
        return new Icon(cssClassName);
    }
}
