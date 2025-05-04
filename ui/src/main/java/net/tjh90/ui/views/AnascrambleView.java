package net.tjh90.ui.views;

import com.vaadin.flow.component.Text;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.router.Route;

import net.tjh90.ui.HasTitle;

@Route("anascramble")
public class AnascrambleView extends VerticalLayout implements HasTitle {

    public static final String NAV_LABEL = "Anascramble";

    private static final String TITLE = "Anascramble";

    public AnascrambleView() {
        setPadding(true);
        setWidthFull();

        add(new Text("Anascramble"));
    }

    @Override
    public String getTitle() {
        return TITLE;
    }
}
