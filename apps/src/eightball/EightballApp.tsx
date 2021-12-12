import React, { ReactNode } from 'react';
import BlueTriangle from './BlueTriangle';

import EightBall from './images/EightBall.svg';
import EightBallBase from './images/EightBallBase.svg';

interface Props {
}

interface State {
    animation: string,
    blueTriangleVisible: boolean,
    imgSrc: string,
    msg: string
}

const idleAnimation: string = 'EightBallIcon-idle infinite 5s ease-in-out';
const shakeAnimation: string = 'EightBallIcon-shake 5 0.2s linear';
const defaultMsg: string = 'Nope';

/**
 * 8-ball app.
 */
class EightballApp extends React.Component<Props, State> {

    /**
     * Constructor.
     *
     * @param props properties.
     */
    constructor(props: Props) {
        super(props);

        this.state = {
            animation: idleAnimation,
            blueTriangleVisible: false,
            imgSrc: EightBall,
            msg: defaultMsg
        };
    }

    /**
     * Handle a button click.
     */
    handleBtnClick = (): void => {
        if(this.state.imgSrc === EightBall) {
            this.shake();
        } else {
            this.reset();
        }        
    }

    /**
     * Shake the 8 ball.
     */
    shake = (): void => {
        this.setState({
            animation: shakeAnimation,
        });

        fetch('/predict')
            .then(res => res.json())
            .then(json => this.setState({msg: json.msg}))
            .catch(error => this.setState({msg: defaultMsg}));

        setTimeout(() => this.setState({
            blueTriangleVisible: true,
            imgSrc: EightBallBase
        }), 1000);

    }

    /**
     * Reset the 8 ball.
     */
    reset = (): void => {
        this.setState({
            animation: idleAnimation,
            blueTriangleVisible: false,
            imgSrc: EightBall
        });
    }

    render(): ReactNode {
        return (
            <div className='App'>
                <div className='Container'>
                    <img
                        className='EightBallIcon'
                        src={this.state.imgSrc}
                        alt='8 ball'
                        style={{animation: this.state.animation}} />
                    <button
                        onClick={this.handleBtnClick}>
                        {this.state.imgSrc === EightBall ? 'Shake!' : 'Reset'}
                    </button>
                </div>
                {this.state.blueTriangleVisible &&  <BlueTriangle msg={this.state.msg}/>}
            </div>
        );
    }
}

export default EightballApp;
