package net.tjh90.ui.components;

import com.vaadin.flow.component.Component;
import com.vaadin.flow.component.Tag;
import com.vaadin.flow.dom.Element;

/**
 * A Font Awesome icon tag.
 */
@Tag("i")
class Icon extends Component {

    private static final String ATTR_CLASS = "class";

    public Icon(final String cssClassName) {
        Element element = getElement();
        element.setAttribute(ATTR_CLASS, cssClassName);
    }
}
