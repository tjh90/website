package net.tjh90.ui;

import com.vaadin.flow.component.Component;
import com.vaadin.flow.component.applayout.AppLayout;
import com.vaadin.flow.component.applayout.DrawerToggle;
import com.vaadin.flow.component.html.H1;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.sidenav.SideNav;
import com.vaadin.flow.component.sidenav.SideNavItem;
import com.vaadin.flow.router.Layout;

import net.tjh90.ui.views.AnascrambleView;
import net.tjh90.ui.views.HomeView;
import net.tjh90.ui.views.css.CssClassNames;

@Layout
public class MainView extends AppLayout {

    private H1 title = new H1();

    public MainView() {
        addToNavbar(createHeaderContent());
        addToDrawer(createSideNav());
    }

    private Component createHeaderContent() {
        HorizontalLayout layout = new HorizontalLayout();
        layout.setWidthFull();
        layout.setClassName(CssClassNames.HEADER);

        layout.addToStart(new DrawerToggle());

        layout.addToMiddle(title);

        return layout;
    }

    private static SideNav createSideNav() {
        SideNav nav = new SideNav();

        nav.addItem(new SideNavItem(HomeView.NAV_LABEL, HomeView.class));
        nav.addItem(new SideNavItem(AnascrambleView.NAV_LABEL, AnascrambleView.class));

        return nav;
    }

    @Override
    public void afterNavigation() {
        String titleText = HomeView.TITLE;
        if (getContent() instanceof HasTitle titledComponent) {
            titleText = titledComponent.getTitle();
        }
        title.setText(titleText);

        setDrawerOpened(false);
    }
}
