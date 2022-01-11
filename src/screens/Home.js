import React ,{Component} from 'react';
import { Route, NavLink, Routes } from "react-router-dom";
import styled from "styled-components";
import Study from "./Study";
import Review from "./Review";
import Result from "./Result";
import Login from "./Login";
import Register from "./Register";

const Button = styled.button`
  width: 200px;
  height: 200px;
  color: white;
  font-size: 36px;
  border: none;
  border-radius: 100px;
  background-color: ${props => props.color};
  :hover {
    background-color: #7f947f;
  }
  margin-left: 100px;
`;

class TOC extends Component{
  render(){
    var list = [];
    var i = 0;
    while (i<this.props.data.length){
      var data = this.props.data[i];
      list.push(
        <Button key={data.id} color={data.color}>
            <NavLink style={{ color: 'white', textDecoration: 'none' }} to={{pathname: `${data.id}`}}>{data.title} </NavLink>
        </Button>);
      i = i+1;
    }
    return (
      <header>
        {list}
      </header>
    );
  }
}

class Home extends Component {
  state = {
    contents: [
      {id: 'Study', title: '학습하기', desc: '학습하기 기능', color: '#5b6d5b'},
      {id: 'Review', title: '오답노트', desc: '오답노트 기능', color: '#94c973'},
      {id: 'Result', title: '학습결과', desc: '학습결과 기능', color: '#4b754b'},
      {id: 'Login' , title: '로그인', desc: '로그인 기능', color: '#5b6d5b'}
    ]
  }
  render() {
    return (
        <div style={{display: 'flex', alignItems:'center', height: '80vh'}}>
        <TOC data={this.state.contents}></TOC>
          <Routes> 
            <Route path="/Study" element={<Study/>}/>
            <Route path="/Review" element={<Review/>}/>
            <Route path="/Result" element={<Result/>}/>
            <Route path="/Login" element={<Login/>}/>
            <Route path="/Register" element={<Register/>}/>
          </Routes>
        </div>
    )
  }
}

export default Home;
