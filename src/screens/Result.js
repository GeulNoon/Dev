import React, { Component } from 'react';

class Subject extends Component{
  render(){
    return (
      <header>
        <h1>{this.props.title}</h1>
        {this.props.sub}
      </header>
    );
  }
}

class Result extends Component {
  render() {
    return (
      <div>
          <Subject title="학습결과" sub="학습결과 기능입니다."></Subject>
      </div>
    );
  }
}

export default Result;
