package net.tjh90.ui.views.anascramble;

import java.time.Instant;
import java.util.List;

import com.vaadin.flow.component.AbstractField.ComponentValueChangeEvent;
import com.vaadin.flow.component.Component;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.data.value.ValueChangeMode;

import net.tjh90.core.Point;
import net.tjh90.core.anascramble.CharacterData;
import net.tjh90.core.anascramble.CharacterScrambler;
import net.tjh90.ui.components.ScrambledCharacter;

/// Defines UI logic for the [AnascrambleView]. Uses [AnascrambleModel] as the data model.
public class AnascrambleViewModel {

    private static final String ALPHANUMERIC_PATTERN = "[a-zA-Z0-9]";

    private final AnascrambleView view;
    private final AnascrambleModel model;

    /// Constructor.
    ///
    /// @param view  the [AnascrambleView] instance to bind to.
    /// @param model the data model instance.
    public AnascrambleViewModel(final AnascrambleView view, final AnascrambleModel model) {
        this.view = view;
        this.model = model;

        TextField scrambleFld = view.getLettersFld();
        if (scrambleFld != null) {
            scrambleFld.setMinLength(3);
            scrambleFld.setMaxLength(30);
            scrambleFld.setAllowedCharPattern(ALPHANUMERIC_PATTERN);

            scrambleFld.setValueChangeMode(ValueChangeMode.EAGER);
            scrambleFld.addValueChangeListener(this::onValueChangedLettersFld);
        }

        Button scrambleBtn = view.getScrambleBtn();
        if (scrambleBtn != null) {
            scrambleBtn.addClickListener(_ -> onClickScrambleBtn());
        }

        onValueChangedLettersFld(null);
    }

    private void onValueChangedLettersFld(final ComponentValueChangeEvent<TextField, String> event) {
        String letters = event != null ? event.getValue() : "";

        // Set the enabled state of the scramble button.
        boolean isScrambleBtnEnabled = letters != null && letters.length() > 2;
        view.getScrambleBtn().setEnabled(isScrambleBtnEnabled);

        model.setLetters(letters);
    }

    private void onClickScrambleBtn() {
        CharacterScrambler letterScrambler = new CharacterScrambler(Instant.now().toEpochMilli());
        List<CharacterData> letterData = letterScrambler.scramble(model.getLetters());

        // Add an offset to each letter.
        float containerOffset = 0.5f * view.getScrambleContainerSize();
        letterData = letterData.stream().map(l -> addOffset(l, containerOffset)).toList();

        view.setScrambledLetters(
                letterData.stream().map(l -> (Component) new ScrambledCharacter(l.letter(), l.point())).toList());
    }

    private static CharacterData addOffset(final CharacterData letterData, final float containerOffset) {
        Point point = new Point(containerOffset + letterData.point().x(), containerOffset + letterData.point().y());
        return new CharacterData(letterData.letter(), point);
    }
}
