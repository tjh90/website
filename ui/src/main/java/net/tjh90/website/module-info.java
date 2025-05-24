module net.tjh90.website.ui {
    requires net.tjh90.website.core;

    // Spring Boot modules.
    requires spring.boot;
    requires spring.boot.autoconfigure;
    requires spring.context;
    requires spring.jcl;

    // Vaadin (automatic) modules.
    requires flow.data;
    requires flow.html.components;
    requires flow.server;
    requires vaadin.app.layout.flow;
    requires vaadin.button.flow;
    requires vaadin.checkbox.flow;
    requires vaadin.lumo.theme;
    requires vaadin.ordered.layout.flow;
    requires vaadin.side.nav.flow;
    requires vaadin.text.field.flow;
}
