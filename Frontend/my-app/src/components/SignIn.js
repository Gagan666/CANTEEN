import React, { Component, useState } from "react";
import axiosInstance from "axios";
import { useHistory } from "react-router-dom";

function SignIn() {
  const history = useHistory();
  if (localStorage.getItem("access_token")) {
    history.push('/home');
    document.location.reload();
  }

  //const navigate = useNavigate();

  const initialFormData = Object.freeze({
    email: '',

    password: '',
  });
  const [FormData, updateFormData] = useState(initialFormData);
  const handleChange = (e) => {
    updateFormData({
      ...FormData,
      [e.target.name]: e.target.value.trim(),
    })
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(FormData);

    axiosInstance
      .post('http://127.0.0.1:8000/api/token/', {
        phone: FormData.phone,
        password: FormData.password,
      })
      .then((res) => {
        localStorage.setItem('access_token', res.data.access);
        localStorage.setItem('refresh_token', res.data.refresh);
        axiosInstance.defaults.headers['Authorization'] =
          'JWT ' + localStorage.getItem('access_token');
        console.log("Successfully logged in")
        history.push("/home");
        document.location.reload();
      })
  }
  return (

    <div className="form-comp cfb">
      <h1>Sign In!</h1>
      <form className="sign-up-form cfb">
        <label>
          Phone:
          <br />
          <input type="number"
            name="phone"
            placeholder="Enter Phone"
            onChange={handleChange}
          />
        </label>

        <label>
          Password:
          <br />
          <input type="password"
            name="password"
            placeholder="Enter password"
            onChange={handleChange} />
        </label>

        <button color="primary"
          onClick={handleSubmit}  >
          Submit
        </button>
      </form></div>




  );

}

export default SignIn;