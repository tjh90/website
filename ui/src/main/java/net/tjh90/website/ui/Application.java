package net.tjh90.website.ui;

import java.time.Clock;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.vaadin.flow.component.dependency.CssImport;
import com.vaadin.flow.component.dependency.StyleSheet;
import com.vaadin.flow.component.page.AppShellConfigurator;
import com.vaadin.flow.server.AppShellSettings;
import com.vaadin.flow.theme.Theme;

import net.tjh90.website.ui.views.home.HomeView;

/// Main application class.
@SpringBootApplication
@Theme(value = "default")
@CssImport("./fontawesome/css/all.css")
@StyleSheet("https://fonts.googleapis.com/css?family=Gloria%20Hallelujah")
public class Application implements AppShellConfigurator {

    private static final String FAVICON = "favicon.ico";
    private static final String FAVICON_SIZE = "256x256";

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Override
    public void configurePage(final AppShellSettings settings) {
        settings.setPageTitle(HomeView.TITLE);
        settings.addFavIcon(FAVICON, FAVICON, FAVICON_SIZE);
    }

    @Bean
    public Clock clock() {
        return Clock.systemDefaultZone();
    }
}
