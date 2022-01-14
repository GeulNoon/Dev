import React from "react";
import { Formik } from "formik";
import * as Yup from "yup";
import "../styles.css";
import user from "../image/user.png";

function Register() {
  return (
  <Formik
    initialValues={{ email: "", password: "", nickname: ""}}

    onSubmit={(values, { setSubmitting }) => {
      setTimeout(() => {
        console.log("Logging in", values);
        setSubmitting(false);
      }, 500);
    }}

    validationSchema={Yup.object().shape({
      email: Yup.string()
        .email("이메일 형식으로 입력해야 합니다.")
        .required("이메일을 입력해야 합니다."),
      nickname: Yup.string()
        .required("닉네임을 입력해야 합니다."),
      password: Yup.string()
        .required("패스워드를 입력해야 합니다.")
        .min(8, "패스워드는 8글자 이상이어야 합니다.")
        .matches(/(?=.*[0-9])/, "패스워드는 반드시 숫자를 포함해야 합니다."),
      confirmPassword: Yup.string()
        .required("패스워드확인을 입력해야 합니다.")
        .oneOf([Yup.ref('password'), null], "패스워드가 일치하지 않습니다."),
      grade: Yup.string()
        .matches(/([1-6])/, "학년은 1-6 사이의 정수만 입력하셔야 합니다.")
        .max(1, "학년은 1-6 사이의 정수만 입력하셔야 합니다.")
    })}
  >
    {props => {
      const {
        values,
        touched,
        errors,
        isSubmitting,
        handleChange,
        handleBlur,
        handleSubmit
      } = props;

      return (
        <div className="Register" >
          <form className="RegisterForm" onSubmit={handleSubmit}>
          <h1 style={{textAlign: "left"}}>회원가입</h1>
            <div className="container0">
              <div className="container1">
                <img src ={user} width='150' height='150' />
              </div>
              <div className="container2">
                <label htmlFor="email">이메일</label>
                  <input
                    name="email"
                    type="text"
                    placeholder="이메일"
                    value={values.email}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    className={errors.email && touched.email && "error"}
                  />
                {errors.email && touched.email && (
                  <div className="input-feedback">{errors.email}</div>
                )}
                <hr/>
                <label htmlFor="email">패스워드</label>
                    <input
                      name="password"
                      type="password"
                      placeholder="패스워드"
                      value={values.password}
                      onChange={handleChange}
                      onBlur={handleBlur}
                      className={errors.password && touched.password && "error"}
                    />
                {errors.password && touched.password && (
                  <div className="input-feedback">{errors.password}</div>
                )}
                <hr/>
                <label htmlFor="email">패스워드 확인</label>
                    <input
                      name="confirmPassword"
                      type="password"
                      placeholder="패스워드 확인"
                      value={values.confirmPassword}
                      onChange={handleChange}
                      onBlur={handleBlur}
                      className={errors.confirmPassword && touched.confirmPassword && "error"}
                    />
                {errors.confirmPassword && touched.confirmPassword && (
                  <div className="input-feedback">{errors.confirmPassword}</div>
                )}
                <hr/>
                <label htmlFor="email">닉네임</label>
                  <input
                    name="nickname"
                    type="nickname"
                    placeholder="닉네임"
                    value={values.nickname}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    className={errors.nickname && touched.nickname && "error"}
                  />
              {errors.nickname && touched.nickname && (
                <div className="input-feedback">{errors.nickname}</div>
              )}
              <hr/>
              <div className="container3">
                <div className="container4">
                  <label htmlFor="email">소속</label>
                    <select>
			                <option key="Elementary" value="Elementary">초등학교 </option>
                      <option key="Middle" value="Middle">중학교</option>
		      	          <option key="High" value="High">고등학교</option>
                      <option key="University" value="University">대학교</option>
                      <option key="Worker" value="Worker">직장인</option>
                      <option key="etc" value="etc">기타</option>
	      	          </select>
                </div>
                <div className="container5">
                  <label htmlFor="email">학년</label>
                    <input
                      name="grade"
                      type="grade"
                      placeholder="학년"
                      value={values.grade}
                      onChange={handleChange}
                      onBlur={handleBlur}
                      className={errors.grade && touched.grade && "error"}
                    />
                  {errors.grade && touched.grade && (
                    <div className="input-feedback">{errors.grade}</div>
                  )}
                </div>
              </div>
            </div>
            </div>
            <button className="registerButton" type="submit" disabled={isSubmitting}>가입하기</button>   
          </form>
        </div>
      );
    }}
  </Formik>
  );
};

export default Register;
