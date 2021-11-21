
const typeList = {
  1: ['text', 'number', 'number', 'number']
}
const nameList = {
  1: ['taskName', 'neededTime', 'upperDifficulty', 'lowerDifficulty']
}

// 追加するやつ
let addTask = document.getElementById("addTask");
addTask.addEventListener('click', function(){
  console.log("add");
  let taskInfo = document.getElementById("taskInfo");
  // 行を追加
  let newData = taskInfo.insertRow(-1);
  // 列を追加
  for (var i = 0; i <= 3; i++){
    let newInput = newData.insertCell(i);

    let input = document.createElement("input");
    input.setAttribute("type", typeList[1][i]);
    input.setAttribute("step", 1);
    input.setAttribute("name", nameList[1][i]);

    newInput.appendChild(input);
  }
});

// 消すやつ
let deleteTask = document.getElementById("deleteTask");
deleteTask.addEventListener('click', function(){
  let taskForm = document.getElementById("taskForm");
  if (taskForm.hasChildNodes()){
    if (taskForm.childElementCount == 1){
      console.log("え、タスクないの？？");
    }
    else{
      taskForm.removeChild(taskForm.lastChild);
    }
  }
})