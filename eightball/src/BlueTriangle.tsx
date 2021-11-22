import React from 'react';
import BlueTriangleImg from './images/BlueTriangle.svg';

import './App.css';

interface Props {
    msg: string
}

interface State {
}

const blueTriangleZoom: string = "BlueTriangle-zoom 1 0.5s linear";

class BlueTriangle extends React.Component<Props, State> {

    render() {
        return (
            <div
                className="BlueTriangle"
                style={{animation: blueTriangleZoom}}>

              <img
                  src={BlueTriangleImg}
                  alt="Blue triangle" />
              <p>{this.props.msg}</p>
            </div>
        );
    }
}

export default BlueTriangle;
