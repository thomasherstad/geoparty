//IDEA: Hamburger: Add points, reopen question, change category, end game, restart game
//TODO: Create function to update points

const teams = [undefined, undefined];
const categories = [undefined]*5;
const points = [100, 200, 300, 400, 500]; //Not used for tile html, but used for question heading
let scores = [undefined, undefined]
let active_team = undefined;
let llm_question = undefined;
let user_answer = undefined;
let llm_response = undefined;

const question_text = document.getElementById("question-text");
const question_tiles = document.querySelectorAll(".question-tile");
const category_tiles = document.querySelectorAll(".category");
const answer_text = document.getElementById("answer-text");

const team1_answer_button = document.getElementById("team1-btn");
const team2_answer_button = document.getElementById("team2-btn");

const user_ans_form = document.getElementById("ans-form");
const ans_submit_btn = document.getElementById("submit-ans-btn");
const response_text_field = document.getElementById("answer-text");
const correct_btn = document.getElementById("correct-btn");
const incorrect_btn = document.getElementById("incorrect-btn")


populate_html(teams, categories);

question_tiles.forEach(question_tile => {
  question_tile.addEventListener("click", log_question_tile);
  question_tile.addEventListener("click", show_question_card);
  question_tile.addEventListener("click", update_category_text);
  question_tile.addEventListener("click", update_points_text);
});

team1_answer_button.addEventListener("click", team_ans_button);
team2_answer_button.addEventListener("click", team_ans_button);

ans_submit_btn.addEventListener("click", set_user_answer);
correct_btn.addEventListener("click", create_response_text);




function show_question_card() {
  document.getElementById("question-card").style.display = "block";
  update_question_text(llm_question) //Has to change to llm_question at some point
};

//Destructor for question card
function hide_question_card() {
  //Need to add all functionality to reset the card
  document.getElementById("question-card").style.display = "none";
  active_team = undefined;
  user_ans_form.style.display = "none";
  active_team = undefined;
  team1_answer_button.style.backgroundColor = "var(--main-color)";
  team2_answer_button.style.backgroundColor = "var(--main-color)";
  user_answer = undefined;
  response_text_field.style.display = "none";
};

function update_question_text(q) {
  document.getElementById("question-text").innerHTML = q;
};

function log_question_tile() {
  console.log(this.id)
}

function update_category_text() {
  const n_category = Number(this.id.charAt(0));
  text = categories[n_category];
  document.getElementById("question-category").innerHTML = text.toUpperCase();
};

function update_points_text() {
  const n_points = Number(this.id.charAt(2))
  text = String(points[n_points]);
  document.getElementById("question-points").innerHTML = text.toUpperCase();
};

function show_answer_field() {
  document.getElementById("user-ans-field").placeholder = active_team + " Answer";
  document.getElementById("ans-form").style.display = "block";
};

function set_active_team() {
  team_id = Number(this.id.charAt(4)) -1;
  active_team = team_id;
  console.log(active_team)
};

// Combined show_answer_field() and set_active_team() because it didn't work to just add the two functions
// Should fix and separate into functions again to make it cleaner
function team_ans_button() {
  team_id = Number(this.id.charAt(4)) -1;
  active_team = team_id;

  document.getElementById("user-ans-field").placeholder = teams[active_team] + " Answer";
  user_ans_form.style.display = "block";

  console.log("Active team is " + active_team)
  
  if(active_team === 0){
    team1_answer_button.style.backgroundColor = "var(--accent-color)";
    team2_answer_button.style.backgroundColor = "var(--main-color)";
  }
  else if(active_team === 1){
    team2_answer_button.style.backgroundColor = "var(--accent-color)";
    team1_answer_button.style.backgroundColor = "var(--main-color)";
  }
};

function populate_html(team_list, category_list) {
  document.getElementById("team1").innerHTML = team_list[0];
  document.getElementById("team1-btn").innerHTML = team_list[0];
  document.getElementById("team2").innerHTML = team_list[1];
  document.getElementById("team2-btn").innerHTML = team_list[1];

  //Can populate the points here to add functionality for different point structures

  let i = 0;
  category_tiles.forEach(category_tile => {
    category_tile.innerHTML = category_list[i];
    console.log(i);
    i = i+1;
  })
};

function set_user_answer(){
  user_answer = document.getElementById("user-ans-field").value;
};

function update_response_text(a) {
  response_text_field.innerHTML = a;
};

function show_response_text(){
  response_text_field.style.display = "block";
}

function create_response_text(){
  update_response_text(llm_response);
  show_response_text();
}