// Change all functions and variables to camelCase
// BUG: Submit button moves left when it shows up again after being hidden

const teams = [setup_data['team1_name'], setup_data['team2_name']];
const categories = [setup_data['category1'], setup_data['category2'], setup_data['category3'], setup_data['category4'], setup_data['category5']];
const points = [100, 200, 300, 400, 500]; //Not used for tile html, but used for question heading
let scores = [0, 0]

let chosenCategory = undefined;
let chosenPoints = undefined;
let activeTeam = undefined;
let activeQuestion = undefined;
let userAnswer = undefined;
let llmResponse = undefined;
let currentID = undefined;

let questionInfo = {
  'category': '',
  'points': '',
  'team': '',
  'question': '',
  'answer': ''
};

let msg = JSON.stringify(questionInfo)

const questionText = document.getElementById("question-text");
const questionTiles = document.querySelectorAll(".question-tile");
const categoryTiles = document.querySelectorAll(".category");


const teamAnswerButtons = document.getElementById("team-select-buttons");
const team1AnswerButton = document.getElementById("team1-btn");
const team2AnswerButton = document.getElementById("team2-btn");

const userAnsForm = document.getElementById("ans-form");
const ansSubmitButton = document.getElementById("submit-ans-btn");
const answerTextField = document.getElementById("user-ans-field");
const responseText = document.getElementById("answer-text");
const correctButtons = document.getElementById("correct-buttons");
const correctButton = document.getElementById("correct-btn");
const incorrectButton = document.getElementById("incorrect-btn");
const closeButton = document.getElementById("close-button");

questionTiles.forEach(questionTile => {
  questionTile.addEventListener("click", logQuestionTile);
  questionTile.addEventListener("click", showQuestionCard);
  questionTile.addEventListener("click", updateCategoryText);
  questionTile.addEventListener("click", updatePointsText);
  questionTile.addEventListener("click", setChosenCategory);
  questionTile.addEventListener("click", setChosenPoints);
  questionTile.addEventListener("click", requestLLM);
});

team1AnswerButton.addEventListener("click", teamAnsButton);
team2AnswerButton.addEventListener("click", teamAnsButton);
ansSubmitButton.addEventListener("click",clickAnsSubmit);
correctButton.addEventListener("click", clickCorrectButton);
incorrectButton.addEventListener("click", clickIncorrectButton);

closeButton.addEventListener("click", hideQuestionCard)

updatePointsDOM();


function updateQuestionInfo(){
  questionInfo.category = chosenCategory;
  questionInfo.points = chosenPoints;
  questionInfo.question = activeQuestion;
  questionInfo.team = activeTeam;
  questionInfo.answer = userAnswer;
  msg = JSON.stringify(questionInfo)
}

//----constructor for informasjonssending----
/* function setActiveTeam() {
  team_id = Number(this.id.charAt(4)) -1;
  activeTeam = team_id;
  console.log(activeTeam)
}; */

function setChosenPoints(){
  const nPoints = Number(this.id.charAt(2));
  chosenPoints = points[nPoints];
}

function setChosenCategory(){
  const nCategory = Number(this.id.charAt(0));
  chosenCategory = categories[nCategory];
}

//Quick and dirty to see if it works
function setActiveQuestion(){
  activeQuestion = questionText.innerHTML;
}
//getAnswer()
//getResponse()

//----destructor for sending information----
function destructQuestionInformation(){
  chosenCategory = undefined;
  chosenPoints = undefined;
  activeTeam = undefined;
  activeQuestion = undefined;
  userAnswer = undefined;
  llmResponse = undefined;
}


//Constructor for question card
function showQuestionCard() {
  document.getElementById("question-card").style.display = "block";
  responseText.style.display = "none";
};

//Destructor for question card
function hideQuestionCard() {
  //Need to add all functionality to reset the card
  document.getElementById("question-card").style.display = "none";
  userAnsForm.style.display = "none";
  team1AnswerButton.style.backgroundColor = "var(--main-color)";
  team2AnswerButton.style.backgroundColor = "var(--main-color)";
  responseText.style.display = "none";
  correctButtons.style.display = "none";
  ansSubmitButton.style.display = "inline-block";
  questionText.innerHTML = '';
  answerTextField.value = '';
  responseText.innerHTML = '';
  teamAnswerButtons.style.display = "none";
  destructQuestionInformation();
};

function logQuestionTile() {
  currentID = this.id
  console.log(currentID)
}

function updateCategoryText() {
  const nCategory = Number(this.id.charAt(0));
  text = categories[nCategory];
  document.getElementById("question-category").innerHTML = text.toUpperCase(); //Needs upper case
};

function updatePointsText() {
  const nPoints = Number(this.id.charAt(2))
  text = String(points[nPoints]);
  document.getElementById("question-points").innerHTML = text;
};

function showAnswerField() {
  document.getElementById("user-ans-field").placeholder = activeTeam + " Answer";
  document.getElementById("ans-form").style.display = "block";
};

// Combined showAnswerField() and setActiveTeam() because it didn't work to just add the two functions
// TODO: Should fix and separate into functions again to make it cleaner
function teamAnsButton() {
  team_id = Number(this.id.charAt(4)) -1;
  activeTeam = team_id;

  document.getElementById("user-ans-field").placeholder = teams[activeTeam] + " Answer";
  userAnsForm.style.display = "block";

  console.log("Active team is " + activeTeam)
  
  if(activeTeam === 0){
    team1AnswerButton.style.backgroundColor = "var(--accent-color)";
    team2AnswerButton.style.backgroundColor = "var(--main-color)";
  }
  else if(activeTeam === 1){
    team2AnswerButton.style.backgroundColor = "var(--accent-color)";
    team1AnswerButton.style.backgroundColor = "var(--main-color)";
  }
};

function setUserAnswer(){
  userAnswer = document.getElementById("user-ans-field").value;
};

function hideSubmitButton(){
  ansSubmitButton.style.display = "none"
}

function showResponseField(){
  responseText.style.display = "block";
};

function showCorrectButtons(){
  correctButtons.style.display = "block";
};

function clickAnsSubmit(){
  setUserAnswer();
  hideSubmitButton();
  showResponseField();
  setActiveQuestion();
  requestLLM();
};

function updatePointsDOM() {
  document.getElementsByClassName("score")[0].innerHTML = scores[0];
  document.getElementsByClassName("score")[1].innerHTML = scores[1];
};

function awardPoints(awarded_points, team_id){
  scores[team_id] = scores[team_id] + awarded_points;
};

function clickCorrectButton(){
  awardPoints(chosenPoints, activeTeam);
  updatePointsDOM();
  //points animation?
  hideQuestionCard();
  setInactiveQuestion(currentID);
}

function clickIncorrectButton(){
  //points animation?
  hideQuestionCard();
  setInactiveQuestion(currentID);
}

//Just a cosmetic way to do it for now
function setInactiveQuestion(id){
  tile = document.getElementById(id);
  //tile.style.backgroundColor = '--var(main-color)';
  //tile.style.border = 'none';
  //tile.innerHTML = '';
  tile.style.visibility = 'hidden'
  //BUG: The following somehow only changes last tile, regardless of id
  //tile.style.display = 'none';
};


async function requestLLM(){
  updateQuestionInfo()
  console.log('Requesting question...')
  console.log(msg)
  let response = await fetch("/question?message=" + msg);
  let new_text = await response.json();
  console.log(new_text)
  if (activeQuestion == undefined){
    questionText.innerHTML = new_text;
    teamAnswerButtons.style.display = "block"
  }
  else if (activeQuestion){
    responseText.innerHTML = new_text;
    showCorrectButtons();
  }
} 