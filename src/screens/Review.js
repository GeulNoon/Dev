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

class Review extends Component {
  render() {
    return (
      <div>
          <Subject title="오답노트" sub="오답노트 기능입니다."></Subject>
      </div>
    );
  }
}

export default Review;
