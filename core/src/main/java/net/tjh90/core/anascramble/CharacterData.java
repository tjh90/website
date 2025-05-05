package net.tjh90.core.anascramble;

import net.tjh90.core.Point;

/// A single character to be scrambled.
public record CharacterData(

    char letter,
    Point point

) {}
