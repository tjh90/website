package net.tjh90.ui.views.anascramble;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;

import net.tjh90.ui.Point;

public class LetterScramblerTest {

    private static final String TEST_LETTERS = "TestLetters";

    /// Test that the letters returned from the scrambler are the same letters as those that appear in the test string.
    @Test
    public void letterScramblerTest() {
        CharacterScrambler letterScrambler = new CharacterScrambler();
        List<CharacterData> scrambledLetters = letterScrambler.scramble(TEST_LETTERS);

        assertEquals(TEST_LETTERS.length(), scrambledLetters.size());

        // Check that all letters in the original test string are present in the scrambled letter list.
        List<Character> testLetters = new ArrayList<>(TEST_LETTERS.chars().mapToObj(c -> (char) c).toList());
        for (CharacterData letter : scrambledLetters) {
            char ch = letter.letter();

            int chInd = testLetters.indexOf(ch);
            assertTrue(chInd >= 0);

            testLetters.remove(chInd);
        }
    }

    /// Test that the positions of the letters returned from the scrambler are adequately spaced.
    @Test
    public void letterPositionTest() {
        CharacterScrambler letterScrambler = new CharacterScrambler();
        List<CharacterData> scrambledLetters = letterScrambler.scramble(TEST_LETTERS);

        List<Point> points = scrambledLetters.stream().map(l -> l.point()).toList();
        int pointsCount = points.size();
        for (int i = 0; i < pointsCount; i++) {
            Point p0 = points.get(i);
            for (int j = i + 1; j < pointsCount; j++) {
                Point p1 = points.get(j);
                assertTrue(Point.distanceSquared(p0, p1) > 50.0);
            }
        }
    }
}
