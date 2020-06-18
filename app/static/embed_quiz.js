
$(document).ready(function(){

    let active = $('#container-intro')
    const quiz = $('#quiz')

    $('#start-button').click(function(){
        active.hide()
        active = quiz.children().first()
        active.show()
        $('#next-button-container').show()

    })

    $('#next-button').click(function(){
        active.hide()
        active = active.next()
        active.show()
        if(!active.next().length){  // I know I know, sorry
            $('#next-button-container').hide()
        }
    })

})
