//validation
function checkPasswordMatch() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
  
    if (password !== confirmPassword) {
      document.getElementById("confirmPassword").setCustomValidity("Passwords do not match.");
    } else {
      document.getElementById("confirmPassword").setCustomValidity("");
    }
  }
const url = "http://127.0.0.1:8000/reg/";
const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
const regBtn = document.getElementById("reg");
const logBtn = document.getElementById("log");
regBtn.addEventListener("click", submit_reg);
logBtn.addEventListener("click", submit_auth);
signupBtn.onclick = () => {
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
};
loginBtn.onclick = () => {
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
};
signupLink.onclick = () => {
  signupBtn.click();
  return false;
};
async function submit_reg(event){
  event.preventDefault();
  let response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify({
      "status": "create",
      "nickname": document.getElementById("nickname").value,
      "email": document.getElementById("email").value,
      "password":  document.getElementById("password").value,
    })
  });
  let res = await response.json();
  if (res["status"] == "account exist"){
    let error = document.getElementById("error-reg");
    error.textContent = "Аккаунт с таким email вже існує";
    error.style.display = "flex";
  }
  else if (res["status"] == "created"){
      document.location.href='http://127.0.0.1:8000/';
  }
  
} 

async function submit_auth(event){
  event.preventDefault();
  let response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify({
      "status": "validate",
      "email": document.getElementById("email-login").value,
      "password":  document.getElementById("password-login").value,
    })
  });
  let res = await response.json();
  if (res["status"] == "checked"){
    document.location.href='http://127.0.0.1:8000/';
  }
  else if (res["status"] == "not exist"){
    let error = document.getElementById("error-login");
    error.textContent = "Такого аккаунту не існує";
    error.style.display = "flex";
  } 
}