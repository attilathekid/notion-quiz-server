$(function (){

  // Grade the quiz when the user submits it
  $('#quiz').submit(function (event){

    //prevent reloading page and hide the quiz
    event.preventDefault();
    $(this).hide(function (){

      //display screen dependent upon result
      if ($(this).serialize()==="answer="+correct){
        $("#correct-answer").show();
      } else {
        $("#wrong-answer").show();
      }
    })
  })
})
