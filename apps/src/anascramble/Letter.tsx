/**
 * Class to encalsulate letter and position.
 */
class Letter {

    letter: string;
    x: number;
    y: number;

    private readonly buffer: number = 50.0;

    /**
     * Constructor.
     *
     * @param letter the letter.
     * @param x the X coordinate.
     * @param y the y coordinate.
     */
    constructor(letter: string, x: number, y: number) {
        this.letter = letter;
        this.x = x;
        this.y = y;
    }

    /**
     * Check if the current class overlaps any of the others provided in the argument.
     * 
     * @param others an array of other Letters to check for overlapping instances.
     * 
     * @returns true iff the current instance overlaps one supplied in the argument array.
     */
    overlaps = (others: Letter[]): boolean => {
        for (let i: number = 0; i < others.length; i++) {
            const other = others[i];
            const xDiff:number = (this.x - other.x);
            const yDiff:number = (this.y - other.y);

            if(Math.sqrt(xDiff * xDiff + yDiff * yDiff) < this.buffer) {
                return true;
            }
        }

        return false;
    }
}

export default Letter;