import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter, Route, Routes} from 'react-router-dom';

import EightballApp from './eightball/EightballApp';
import AnascrambleApp from './anascramble/AnascrambleApp';

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='eightball' element={<EightballApp />} />
        <Route path='anascramble' element={<AnascrambleApp />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
