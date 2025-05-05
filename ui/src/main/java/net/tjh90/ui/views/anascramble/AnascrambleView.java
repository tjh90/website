package net.tjh90.ui.views.anascramble;

import java.util.List;

import com.vaadin.flow.component.Component;
import com.vaadin.flow.component.Unit;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.html.Div;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.dom.Style;
import com.vaadin.flow.dom.Style.Position;
import com.vaadin.flow.router.Route;

import net.tjh90.ui.HasTitle;
import net.tjh90.ui.views.CssClassNames;

/// Defines the Anascramble view elements. UI logic is handled in [AnascrambleViewModel].
@Route("anascramble")
public class AnascrambleView extends VerticalLayout implements HasTitle {

    public static final String NAV_LABEL = "Anascramble";

    private static final String TITLE = "Anascramble";

    private static final String SCRAMBLE_FLD_LBL = "Letters to scramble";
    private static final String SCRAMBLE_BTN_TEXT = "Scramble!";

    private static final float SCRAMBLE_CONTAINER_SIZE = 400.0f;

    private final TextField lettersFld = new TextField(SCRAMBLE_FLD_LBL);
    private final Button scrambleBtn = new Button(SCRAMBLE_BTN_TEXT);
    private final Div scrambleContainer = new Div();

    private final AnascrambleViewModel viewModel;

    public AnascrambleView() {
        setPadding(true);
        setWidthFull();
        setDefaultHorizontalComponentAlignment(Alignment.CENTER);

        // Add container for scrambled letters.
        scrambleContainer.setWidth(SCRAMBLE_CONTAINER_SIZE, Unit.PIXELS);
        scrambleContainer.setHeight(SCRAMBLE_CONTAINER_SIZE, Unit.PIXELS);
        scrambleContainer.setClassName(CssClassNames.SCRAMBLE_CONTAINER);
        Style style = scrambleContainer.getStyle();
        if (style != null) {
            style.setPosition(Position.RELATIVE);
        }
        add(scrambleContainer);

        // Add entry field and button.
        add(lettersFld);
        add(scrambleBtn);

        viewModel = new AnascrambleViewModel(this, new AnascrambleModel());
    }

    public TextField getLettersFld() {
        return lettersFld;
    }

    public Button getScrambleBtn() {
        return scrambleBtn;
    }

    public float getScrambleContainerSize() {
        return SCRAMBLE_CONTAINER_SIZE;
    }

    @Override
    public String getTitle() {
        return TITLE;
    }

    public void setScrambledLetters(final List<Component> scrambledLetters) {
        scrambleContainer.removeAll();
        scrambleContainer.add(scrambledLetters);
    }
}
