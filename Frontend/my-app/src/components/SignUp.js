import React, { Component, useState } from "react";
import axiosInstance from "axios";
//import {useNavigate} from 'react-router-dom';

function SignUp() {
  //const navigate = useNavigate();

  const initialFormData = Object.freeze({
    phone: '',
    user_name: '',
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

    try {
      axiosInstance
        .post('http://127.0.0.1:8000/api/register/', {
          phone: FormData.phoneno,
          user_name: FormData.username,
          password: FormData.password,
        })

        .then((res) => {

          console.log(res.data);
        })

    }

    catch (error) {
      console.error(error.res.data);     // NOTE - use "error.response.data` (not "error")
    }
  }

  return (

    <div className="form-comp cfb">
      <h1>Sign Up!</h1>
      <form className="sign-up-form cfb">
        <label>
          Phoneno:
          <br />
          <input type="number"
            name="phoneno"
            placeholder="Enter phoneno"
            onChange={handleChange}
          />
        </label>
        <label>
          User Name:
          <br />
          <input type="text"
            name="username"
            placeholder="Enter user name"

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













export default SignUp;