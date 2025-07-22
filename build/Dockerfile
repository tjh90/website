# Dockerfile for creating a package from the website .jar.

FROM ubuntu:24.04 AS website-base

SHELL [ "/bin/bash", "-c" ]

# Install updates and add user for running the application.
ENV USER=website
RUN apt-get update && \
    apt-get upgrade -y && \
    useradd -m -s /bin/bash $USER

########################################################################################################################

FROM website-base AS website-build-jre

ARG JDK_VERSION="8"

ARG CMD_PATH="/usr/local/bin/CreateJre.sh"
COPY CreateJre.sh $CMD_PATH

# Install required packages and the JDK.
RUN \
    # Add the Adoptium repository to the apt sources and update.
    apt-get install -y apt-transport-https gpg wget && \
    wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | \
        gpg --dearmor | \
        tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null && \
    VERSION_CODENAME=$(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) && \
    echo "deb https://packages.adoptium.net/artifactory/deb $VERSION_CODENAME main" | \
        tee /etc/apt/sources.list.d/adoptium.list > /dev/null && \
    apt-get update && \
\
    # Install the JDK.
    apt-get install --no-install-recommends -y fakeroot temurin-${JDK_VERSION}-jdk && \
\
    # Clean up the apt cache.
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
\
    chmod +x $CMD_PATH

USER $USER
WORKDIR /opt

# Create a JRE for running the website .jar.
CMD [ "CreateJre.sh" ]

########################################################################################################################

FROM website-base AS website-run

COPY --chown=$USER ./target/website-*.jar /home/$USER/website.jar

# Set up user.
USER $USER
WORKDIR /home/$USER

CMD [ "bash", "-c", "/opt/jre/bin/java -jar website.jar" ]
