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

class MyPage extends Component {
  render() {
    return (
      <div>
          <Subject title="내정보" sub="내정보 기능입니다."></Subject>
      </div>
    );
  }
}

export default MyPage;
