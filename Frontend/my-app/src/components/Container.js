import React, {useState} from 'react';

// styling
import '../App.css';

// components
import SignIn from './SignIn';
import SignUp from './SignUp';

const Container = () => {
  const [welcome, setWelcome] = useState(false)

  const setBannerClass = () => {
    const classArr = ["banner-side cfb"]
    if (welcome) classArr.push('send-right')
    return classArr.join(' ')
  }

  const setFormClass = () => {
    const classArr = ["form-side cfb"] 
    if (welcome) classArr.push('send-left')
    return classArr.join(' ')
  }

  return (
    <div className="Container cfb">

      <div className={setBannerClass()}> 

        {welcome ? 
          <h2>Already have an account?</h2>
            : <h2>Are you a new user?</h2>}

        <button onClick={()=> setWelcome(!welcome)}>
          {welcome ?
            "Sign In"
              : "Create Account"}
        </button>
      </div>

      <div className={setFormClass()}> 
          {welcome ? 
            <SignUp /> 
              : <SignIn/>
          }
          
      </div>
    </div>
  );
}

export default Container;