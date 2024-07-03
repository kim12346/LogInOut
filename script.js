$('.closebtn').click(function(){
    $('.join').hide()
})

$('.log-joinbtn').click(function(){
    $('.join').show()
})

$('.closebtn2').click(function(){
    $('.inform').hide()
})

// 만약 아이디와 비번이 일치하면 화면 나오기 등
$('.log-chkbtn').click(function(){
    $('.inform').show()
})