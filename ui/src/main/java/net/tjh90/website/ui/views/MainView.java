package net.tjh90.website.ui.views;

import com.vaadin.flow.component.Component;
import com.vaadin.flow.component.applayout.AppLayout;
import com.vaadin.flow.component.applayout.DrawerToggle;
import com.vaadin.flow.component.checkbox.Checkbox;
import com.vaadin.flow.component.html.H1;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.sidenav.SideNav;
import com.vaadin.flow.component.sidenav.SideNavItem;
import com.vaadin.flow.router.Layout;

import net.tjh90.website.ui.views.anascramble.AnascrambleView;
import net.tjh90.website.ui.views.home.HomeView;

/// Defines the main application view elements.
@Layout
public class MainView extends AppLayout {

    private static final String DARK_MODE = "Dark mode";

    private final MainViewModel viewModel;

    private H1 title = new H1();
    private SideNavItem darkModeItem = new SideNavItem(DARK_MODE);
    private Checkbox darkModeCheckbox = new Checkbox(false);

    public MainView() {
        addToNavbar(createHeaderContent());
        addToDrawer(createSideNav());

        viewModel = new MainViewModel(this);
    }

    private Component createHeaderContent() {
        HorizontalLayout layout = new HorizontalLayout();
        layout.setWidthFull();
        layout.setClassName(CssClassNames.HEADER);

        layout.addToStart(new DrawerToggle());

        layout.addToMiddle(title);

        return layout;
    }

    private SideNav createSideNav() {
        SideNav nav = new SideNav();

        nav.addItem(new SideNavItem(HomeView.NAV_LABEL, HomeView.class));
        nav.addItem(new SideNavItem(AnascrambleView.NAV_LABEL, AnascrambleView.class));

        darkModeItem.setSuffixComponent(darkModeCheckbox);
        nav.addItem(darkModeItem);

        return nav;
    }

    @Override
    public void afterNavigation() {
        viewModel.onNavigation();
    }

    H1 getTitle() {
        return title;
    }

    Checkbox getDarkModeCheckbox() {
        return darkModeCheckbox;
    }

    SideNavItem getDarkModeItem() {
        return darkModeItem;
    }
}
