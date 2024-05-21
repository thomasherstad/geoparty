function log(id) {
    console.log(id);
  }; 

// document.getElementsByClassName("question-tile").addEventListener("click", toggle_question);

// function toggle_question(){
// document.getElementById("question-card").style.display = "show"
// };

const element = document.getElementById("0,0");

element.addEventListener("click", show_question_card);

function show_question_card() {
  document.getElementById("question-card").style.display = "block";
}

//FOR LATER
function hide_question_card() {
  document.getElementById("question-card").style.display = "none";
}