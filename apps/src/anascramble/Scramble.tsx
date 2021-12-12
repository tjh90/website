import React, { ReactNode } from 'react';
import CSS from 'csstype';

import Letter from './Letter';

interface Props {
    word: string
}

interface State {
}

type ParagraphArray = React.DetailedHTMLProps<React.HTMLAttributes<HTMLParagraphElement>, HTMLParagraphElement>[];

/**
 * Class for displaying scrambled letters.
 */
class Scramble extends React.Component<Props, State> {

    private static readonly OFFSET_X: number = 175;
    private static readonly OFFSET_Y: number = 175;
    private static readonly LIMIT_X: number = 400;
    private static readonly LIMIT_Y: number = 150;

    /**
     * @returns the scrambled letter view.
     */
    createScramble = (): ParagraphArray => {
        // Get the letters from the props.
        const letters: string[] = this.props.word.split('')
            .map((l) => l.toUpperCase()).sort(() => 0.5 - Math.random());

        // Place the first letter at the origin.
        let letterPositions: Letter[] = [new Letter(letters[0], 0.0, 0.0)];

        let offset: number = 50.0;
        const offsetIncr: number = 1.0;
        for (let i: number = 1; i < letters.length; i++) {
            let theta: number = 2 * Math.PI * Math.random();
            let x: number = Math.max(-Scramble.LIMIT_X, Math.min(Scramble.LIMIT_X, offset * Math.sin(theta)));
            let y: number = Math.max(-Scramble.LIMIT_Y, Math.min(Scramble.LIMIT_Y, offset * Math.cos(theta)));

            let letter: Letter = new Letter(letters[i], x, y);
            let tries: number = 0;
            while(letter.overlaps(letterPositions)) {
                let theta: number = 2 * Math.PI * Math.random();
                letter.x = Math.max(-Scramble.LIMIT_X, Math.min(Scramble.LIMIT_X, offset * Math.sin(theta)));
                letter.y = Math.max(-Scramble.LIMIT_Y, Math.min(Scramble.LIMIT_Y, offset * Math.cos(theta)));

                if(tries % 10 == 0) {
                    offset += offsetIncr;
                }
            }

            letterPositions.push(letter);
        }

        // Create tags and return.
        return letterPositions.map((l, i) => {
            return <p key={i} style={this.getStyle(l.x, l.y)}>{l.letter}</p>
        });
    }

    /**
     * Get style for an individual letter.
     * 
     * @param x the x offset from the parent HTML element.
     * @param y the y offset from the parent HTML element.
     * 
     * @returns style to use for the letter HTML element.
     */
    getStyle = (x:number, y: number): CSS.Properties => {

        const style: CSS.Properties = {
            color: 'var(--dark-blue)',
            left: `${x + Scramble.OFFSET_X}px`,
            position: 'absolute',
            top: `${y + Scramble.OFFSET_Y}px`
        };

        return style;
    }

    render(): ReactNode {
        const content = this.createScramble();

        return (
            <div className='scrambleContainer'>
                {content}
            </div>
        );
    }
}

export default Scramble;
