package net.tjh90.ui.views;

import com.vaadin.flow.component.AbstractField.ComponentValueChangeEvent;
import com.vaadin.flow.component.UI;
import com.vaadin.flow.component.checkbox.Checkbox;
import com.vaadin.flow.component.html.H1;
import com.vaadin.flow.component.sidenav.SideNavItem;
import com.vaadin.flow.dom.Element;
import com.vaadin.flow.dom.ThemeList;
import com.vaadin.flow.theme.lumo.Lumo;

import net.tjh90.ui.HasTitle;
import net.tjh90.ui.views.home.HomeView;

/// Defines UI logic for the [MainView].
public class MainViewModel {

    private final MainView view;

    /// Constructor.
    ///
    /// @param view  the [MainView] instance to bind to.
    public MainViewModel(final MainView view) {
        this.view = view;

        SideNavItem darkModeItem = view.getDarkModeItem();
        Checkbox darkModeCheckbox = view.getDarkModeCheckbox();

        Element darkModeItemElement = darkModeItem.getElement();
        if (darkModeItemElement != null) {
            darkModeItemElement.addEventListener(ElementEvents.CLICK,
                    _ -> darkModeCheckbox.setValue(!darkModeCheckbox.getValue()));
        }

        if (darkModeCheckbox != null) {
            darkModeCheckbox.addValueChangeListener(MainViewModel::applyTheme);
        }
    }

    public static void applyTheme(final ComponentValueChangeEvent<Checkbox, Boolean> event) {
        boolean isDarkMode = event.getValue();
        UI ui = UI.getCurrent();
        Element element = ui != null ? ui.getElement() : null;
        ThemeList themeList = element != null ? element.getThemeList() : null;
        if (themeList == null) {
            return;
        }

        if (isDarkMode) {
            themeList.add(Lumo.DARK);
        } else {
            themeList.remove(Lumo.DARK);
        }
    }

    public void onNavigation() {
        H1 title = view.getTitle();
        if (title == null) {
            return;
        }

        String titleText = HomeView.TITLE;
        if (view.getContent() instanceof HasTitle titledComponent) {
            titleText = titledComponent.getTitle();
        }
        title.setText(titleText);

        view.setDrawerOpened(false);
    }
}
