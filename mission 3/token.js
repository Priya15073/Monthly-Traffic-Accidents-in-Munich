 const axios = require('axios')
//
 const hotpTotpGenerator = require('hotp-totp-generator')


const URL = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge';

const body= {
"github":"https://github.com/Priya15073/Monthly-Traffic-Accidents-in-Munich",
"email":"priya15073@iiitd.ac.in",
"url":"https://num-accident-prediction.herokuapp.com/docs",
"notes":"" // Not mandatory
}

const paswd=hotpTotpGenerator.totp({
  key: 'priya15073@iiitd.ac.inDPSCHALLENGE',
  X: 120,
  T0: 0,
  algorithm: 'sha512',
  digits: 10
});
console.log(paswd);
const head = {
  'Authorization': `Basic ${paswd}`,
  'Content-Type': 'application/json'

};
console.log(head)
axios
  .post(URL, body,{headers:head})
  .then((response) => console.log('Response', response))
  .catch((error) => console.log('Error', error));
