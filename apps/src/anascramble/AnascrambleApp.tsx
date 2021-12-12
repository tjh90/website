import React, { ReactElement, ReactNode } from 'react';

import Scramble from './Scramble';

interface Props {
}

interface State {
    scramble: ReactElement,
    word: string
}

/**
 * Anascrable app.
 */
class AnascrambleApp extends React.Component<Props, State> {

    /**
     * Constructor.
     *
     * @param props properties.
     */
    constructor(props: Props) {
        super(props);

        this.state = {
            scramble: <Scramble word='' />,
            word: ''
        };
    }

    /**
     * Perform check on keyboard events to filter out non-alphabetical characters.
     * 
     * @param e the event.
     */
    filterInput = (e: React.KeyboardEvent<HTMLInputElement>):void => {
        const key: string = e.key;
        const re: RegExp = /[a-zA-Z]/
        if(!key.match(re)) {
            e.preventDefault();
        }
    }

    /**
     * Handle button click - scramble the word.
     */
    handleBtnClick = ():void => {
        this.setState({scramble: <Scramble word={this.state.word} />});
    }

    render(): ReactNode {
        const word: string = this.state.word;
        const isBtnDisabled: boolean = word.length < 3 || word.length > 30;

        return (
            <div className='App'>
                <div className='Container'>
                    {this.state.scramble}
                    <form>
                        <label>Letters to scramble:</label>
                        <input
                            type='text'
                            onChange={(e) => this.setState({word: e.target.value})}
                            onKeyDown={(e) => this.filterInput(e)} />
                    </form>
                    <button
                        className={isBtnDisabled ? 'Disabled' : ''}
                        disabled={isBtnDisabled}
                        onClick={this.handleBtnClick}>
                        Scramble!
                    </button>
                </div>
            </div>
        );
    }
}

export default AnascrambleApp;