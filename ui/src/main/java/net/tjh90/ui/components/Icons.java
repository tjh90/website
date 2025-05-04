package net.tjh90.ui.components;

import net.tjh90.ui.views.css.CssClassNames;

public enum Icons {

    GITHUB(CssClassNames.GITHUB_ICON),
    PHD_THESIS(CssClassNames.PHD_THESIS_ICON),
    PAPER(CssClassNames.PAPER_ICON);

    private final String cssClassName;

    Icons(final String cssClassName) {
        this.cssClassName = cssClassName;
    }

    public Icon create() {
        return new Icon(cssClassName);
    }
}
