import React, { ReactNode } from 'react';
import BlueTriangleImg from './images/BlueTriangle.svg';

interface Props {
    msg: string
}

interface State {
}

const blueTriangleZoom: string = "BlueTriangle-zoom 1 0.5s linear";

/**
 * Blue triangle component.
 */
class BlueTriangle extends React.Component<Props, State> {

    render(): ReactNode {
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
