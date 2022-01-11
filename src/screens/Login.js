import React from 'react';
import { NavLink} from 'react-router-dom' 
import { Formik } from "formik";
import * as Yup from "yup";
import "../styles.css";

function Login() {
  return (
  <Formik
    initialValues={{ email: "", password: "" }}

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
      password: Yup.string()
        .required("패스워드를 입력해야 합니다.")
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

      return(
        <div className="Login" >
          <form className="LoginForm" onSubmit={handleSubmit}>
            <h1>로그인</h1>
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
              <button className="loginButton" type="submit" disabled={isSubmitting}>로그인</button>
              <h5 style={{margin: 10, textAlign: 'right'}}>
                <NavLink to= "/Register" style={{color: "rgb(36, 36, 36)"}}> 아직 글눈의 회원이 아니신가요? </NavLink>
              </h5>
          </form>
        </div>
      );
    }}
  </Formik>
  );
};

export default Login;
