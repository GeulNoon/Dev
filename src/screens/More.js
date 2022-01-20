import React, { Component } from 'react';
import HistoryTable from '../components/HistoryTable';
class More extends Component {
  render() {
    return (
      <div style={{display: 'flex', justifyContent: 'center'}}>
        <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', width: '900px'}}>
          <div style={{display: 'flex', alignItems: 'center', justifyContent:'center', 
            width: '700px', height: '40px', borderRadius: '10px', 
            backgroundColor: '#eff0ef', marginBottom: '20px'}}>
            <h5>학습이력</h5>
          </div>
          <HistoryTable/>
        </div>
      </div>
    );
  }
}

export default More;