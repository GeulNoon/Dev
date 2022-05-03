//학습하기의 문제풀기:어휘풀기
import React, { useState, useEffect, Component } from 'react';
import NavigationBar from "../components/NavigationBar";
import Choice from "../components/Choice";
import MultipleChoice from "../components/MutipleChoice";
import { NavLink } from "react-router-dom";
import NextIcon from "../image/NextIcon.png";
import styled from "styled-components";
import axios from "axios"

const SubmitButton = styled.button`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 150px;
  height: 30px;
  font-size: 14px;
  color: white;
  background-color: #5b6d5b;
  :hover {
    background-color: #5b6d5b;
    opacity: 0.7;
  }
  border: none;
  margin-bottom: 20px;
`;

//어휘문제 제목 글씨(title(제목)과 sub(설명)을 요소로 전달받음)
class Subject extends Component {
  render() {
    return (
      <header>
        <h1>{this.props.title}</h1>
        {this.props.sub}
      </header>
    );
  }
}

//메인함수
const Step3 = () => {
  const state = {
    contents: [
      {id: 'Step1', title: '1단계', desc: '전문보기', type: 1},
      {id: 'Step2', title: '2단계', desc: '요약하기', type: 1},
      {id: 'Step3', title: '3단계', desc: '어휘풀기', type: 0},
      {id: 'Step5', title: '4단계', desc: '빈칸풀기', type: 1},
      {id: 'Step4', title: '5단계', desc: '결과보기', type: 1},
    ]
  };

  const [Title, setTitle] = useState('');
  const [Example1, setExample1] = useState();
  const [Question1, setQuestion1] = useState();
  const [Question2, setQuestion2] = useState();
  const [Question2W, setQuestion2W] = useState();
  const [Question2S, setQuestion2S] = useState();
  const [Question4, setQuestion4] = useState();
  const [Example2, setExample2] = useState();
  const [Example3, setExample3] = useState();
  const [Example4, setExample4] = useState();


  useEffect(async () => {
    const response = await axios.get(`http://127.0.0.1:8000/api/title`, {params: {'a_id': sessionStorage.getItem('a_id')}});
    setTitle(response.data['title']);
    console.log(Title);
  },[]);

  useEffect(async () => {
    const response = await axios.get(`http://127.0.0.1:8000/api/Step3`, {params: {'a_id': sessionStorage.getItem('a_id'), 's_id': sessionStorage.getItem('s_id')}});
    setExample1(response.data['quiz1']['Choice']);
    setQuestion1(response.data['quiz1']['Test']);
    setQuestion2(response.data['quiz2']['Test']);
    setQuestion2W(response.data['quiz2']['Word']);
    setQuestion2S(response.data['quiz2']['Sentence']);
    setExample2(response.data['quiz2']);
    setExample3(response.data['quiz3']);
    setQuestion4(response.data['quiz4']['Test']);
    setExample4(response.data['quiz4']['Choice']);
    console.log(Example1)
    console.log(Example2)
    console.log(Example3)
    console.log(Example4)
  },[]);

  /*useEffect(() => {
    const fetchUserData = async () => {
      const res = await axios.get(`http://127.0.0.1:8000/api/Step3`, {params: {'a_id': sessionStorage.getItem('a_id'), 's_id': sessionStorage.getItem('s_id')}});
      setExample1(res.data['quiz']["Choice"]);
      console.log(Example1)
    }
    fetchUserData()
  },[Example1]);*/

  const [answer, setAnswer] = useState([
    { id: 1, value: "" },
    { id: 2, value: "" },
    { id: 3, value: "" },
  ]); //사용자가 입력한 답. 문제 마다 value에 저장
  return (
    <div style={{ display: "flex" }}>
      <NavigationBar list={state.contents} title={Title} prev={"Study"} />{" "}
      {/*화면 좌측 단계이동 바*/}
      <div
        style={{
          width: "90vw",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          paddingLeft: "9vw",
          marginTop: "3vw",
        }}
      >
        <div style={{ width: "80vw" }}>
          <Subject
            title="3단계: 지문 속 어휘 공부하기"
            sub="다양한 어휘 문제를 풀며 본문 속 어휘의 정확한 뜻을 습득해봅시다."
          ></Subject>
        </div>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Choice answer={answer} setAnswer={setAnswer} example = {Example1} question = {Question1} id={1} />{" "}
          {/*객관식 문제*/}
          <MultipleChoice answer={answer} setAnswer={setAnswer} question = {Question2} word = {Question2W} sentence = {Question2S} id={2} />{" "}
          {/*동음이의어 문제*/}
          <Choice answer={answer} setAnswer={setAnswer} example = {Example4} question = {Question4} id={3} />
          {answer.map((ans) => ans.value)}{" "}
          {/*사용자 답 확인하기 위해 임시로 넣었습니다*/}
        </div>
        <div
          style={{
            width: "80vw",
            display: "flex",
            flexDirection: "column",
            alignItems: "flex-end",
          }}
        >
          <SubmitButton>제출하기</SubmitButton>
          <NavLink to="/Study/Step4">
            <img alt="" src={NextIcon} width="37.5px" height="37.5px" />
          </NavLink>{" "}
          {/*다음 단계 버튼*/}
        </div>
      </div>
    </div>
  );
};

export default Step3;
