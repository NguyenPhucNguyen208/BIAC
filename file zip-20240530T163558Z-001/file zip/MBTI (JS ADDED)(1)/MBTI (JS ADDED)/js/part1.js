
const cautraloi = document.querySelectorAll('.cautraloi');
const submitbut = document.getElementById('submit');
const quiz = document.getElementById('question');
let cauhoihientai = 0;
let socaudung = 0;
let tinhcach1;


load_cauhoi()



function load_cauhoi(){
  submitbut.disabled = true;
  remove_answer();

  fetch('../text/data1.json')
    .then(res => res.json())
    .then(data => {
      document.getElementById('tongsocauhoi').textContent = data.question.length; 
    const cauhoi = document.getElementById('title');
    const a_cautraloi = document.getElementById('a_cautraloi');
    const b_cautraloi = document.getElementById('b_cautraloi');

    //hien thi cau hoi va cau tra loi
    const get_cauhoi = data.question[cauhoihientai];
    console.log(get_cauhoi);

    cauhoi.innerText = get_cauhoi.title;
    a_cautraloi.innerText = get_cauhoi.cau_a;
    b_cautraloi.innerText = get_cauhoi.cau_b;

    document.getElementById('caudung').value = get_cauhoi.cau_dung
  })
  .catch(error => console.log(error));
}

//chon cau tra loi
function get_answer(){
  let answer = undefined;
  cautraloi.forEach((cautraloi) => {
    if(cautraloi.checked){
      answer = cautraloi.id;
    }
  })
  return answer;
}

//remove cau tra loi
function remove_answer(){
  cautraloi.forEach((cautraloi) =>{
    cautraloi.checked = false;
  })
}

//disabled button
cautraloi.forEach((elem) => {
  elem.addEventListener("change", function(event) {
    submitbut.removeAttribute('disabled');
  });
});


//su kien click
submitbut.addEventListener("click", () => {
  const answer = get_answer();
  if(answer){
    if(answer === document.getElementById('caudung').value){
      socaudung++;
      console.log(socaudung);
    }
  }

  cauhoihientai++;
  load_cauhoi();


  if (socaudung > 4) {
    tinhcach1 = 'E';
  } else {
    tinhcach1 = 'I';
  }

  if(cauhoihientai < document.getElementById('tongsocauhoi').value){
    load_cauhoi();
  }else{
    // Lưu trữ giá trị biến trong lưu trữ web
    localStorage.setItem('tinhcach1', tinhcach1);
    quiz.innerHTML = `
      <h3>Bạn đã hoàn thành phần 1</h3>
      <button onclick="window.location.href = 'part2.html'">Sang phần 2</button>
    `  

  }

})
















