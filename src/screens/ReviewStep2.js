//오답노트의 문제풀기:요약하기
import React, { Component } from 'react';
import NavigationBar from '../components/NavigationBar';
import { DragBlock } from '../components/DragBlock';
import styled from "styled-components";
import { NavLink } from "react-router-dom";
import NextIcon from "../image/NextIcon.png";

//문단내용 박스
const TextBox = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80vw;
  height: 30vh;
  background-color: #e5e5e5;
  font-size: 11px;
  border: none;
`;

//순서배열, 직접작성 선택 버튼
const Button = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 40px;
  font-size: 14px;
  color: black;
  background-color: white;
  :hover {
    background-color: #5b6d5b;
    color: white;
  }
  border: 1px solid grey;
`;
//메인함수
class ReviewStep2 extends Component {
  state = {
    contents: [
      {id: 'ReviewStep1', title: '1단계', desc: '전문보기', type: 1},
      {id: 'ReviewStep2', title: '2단계', desc: '요약하기', type: 0},
      {id: 'ReviewStep3', title: '3단계', desc: '어휘풀기', type: 1},
      {id: 'ReviewStep4', title: '4단계', desc: '결과보기', type: 1},
    ],
    isSelected: true
  }
  render() {
    const { isSelected } = this.state; /*순서배열, 직접작성 중 선택 여부*/
    let Input = null;
    /*isSelected가 true일 시 순서배열, 아닐 시 직접작성*/
    if (isSelected) {
      Input = <DragBlock/>;
    } else {
      Input = <input placeholder='요약하신 문장을 입력해주세요.' 
      style={{width: '80vw', height: '50px', marginTop: 20, backgroundColor: '#f6f6f6', borderWidth: '1px'}}/>;
    }
    return (
      <div style={{display:'flex'}}>
        <NavigationBar list={this.state.contents}  prev={"Review"}/> {/*화면 좌측 단계이동 바*/}
        <div style={{width: '90vw', display:'flex', flexDirection: 'column', alignItems: 'center', paddingLeft: '9vw'}}>
          <div style={{width: '80vw', marginBottom: '20px'}}>          
            <div className='pointer'>틀린 문제</div>
          </div>
          <div style={{display:'flex', flexDirection: 'column', alignItems: 'center'}}>
            <TextBox>문단 내용</TextBox>
            <div style={{width: '80vw', display:'flex', margin: 10}}>
              <Button onClick={()=>{ this.setState({isSelected: true}); }} > 순서배열 </Button>
              <Button onClick={()=>{ this.setState({isSelected: false}); }} > 직접입력 </Button>
            </div>
            {Input}
          </div>
          <div style={{width: '80vw', display: 'flex', justifyContent: 'end'}}>
            <NavLink to="/Review/ReviewStep3">
              <img alt="" src ={NextIcon} width='37.5px' height='37.5px'/>               
            </NavLink>  {/*다음 단계 버튼*/}
          </div>
        </div>
      </div>
    );
  }
}

export default ReviewStep2;