import React from 'react';
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

const idleAnimation: string = "EightBallIcon-idle infinite 5s ease-in-out";
const shakeAnimation: string = "EightBallIcon-shake 5 0.2s linear";
const blueTriangleZoom: string = "BlueTriangle-zoom 1 0.5s linear";

class App extends React.Component<Props, State> {

    constructor(props: Props) {
        super(props);

        this.state = {
            animation: idleAnimation,
            blueTriangleVisible: false,
            imgSrc: EightBall,
            msg: "Nope"
        };
    }

    /**
     * Handle a button click.
     */
    handleBtnClick = () => {
        if(this.state.imgSrc === EightBall) {
            this.shake();
        } else {
            this.reset();
        }        
    }

    /**
     * Shake the 8 ball.
     */
    shake = () => {
        this.setState({
            animation: shakeAnimation,
        });

        setTimeout(() => this.setState({
            blueTriangleVisible: true,
            imgSrc: EightBallBase
        }), 1000);
    }

    /**
     * Reset the 8 ball.
     */
    reset = () => {
        this.setState({
            animation: idleAnimation,
            blueTriangleVisible: false,
            imgSrc: EightBall
        });
    }

    render() {
        return (
            <div className="App">
              <img
                  className="EightBallIcon"
                  src={this.state.imgSrc}
                  alt="8 ball"
                  style={{animation: this.state.animation}} />
              {this.state.blueTriangleVisible &&  <BlueTriangle msg={this.state.msg}/>}
              <button
                  onClick={this.handleBtnClick}>{this.state.imgSrc === EightBall ? "Shake!" : "Reset"}</button>
            </div>
        );
    }
}

export default App;
