$(document).ready(function() {
    var $mainOutput = $('#output');
    var op = '' 
    var num1 = ''

    var clearData = function() {
        op = ''
        num1 = ''
    };

    var clearOutput = function() {
        $mainOutput.html('');
    };

    $('.nums').click(function() {
        num2 = $(this).val() 
        content = $mainOutput.html()
        if(num1 == '' && num2 == '.') return; 
        if(num2 == '.' && ('+-*/.').indexOf(content[content.length-1]) != -1) return; //不能连续输入小数点
        if(num1 == '') {
            $mainOutput.html('');
            $mainOutput.append(num2);
        }
        else{
            $mainOutput.append(num2);
        }
        num1 = num2
    });

    $('#clearButton').click(function() {
        $mainOutput.html('0');
        clearData();
    });

    $('#deleteButton').click(function() {
        input = $mainOutput.html()
        if (input != '0') {
            input = input.substring(0, input.length-1)    
            if (input[input.length-1] == ')'){
                input = input.substring(1,input.length-1)
            }
            $mainOutput.html(input);
            if (input == '') {
                clearData();
                $mainOutput.html('0');
            }
        }
    });

    $('.btn-operate').click(function() { //+-*/
    var newOp = $(this).val();
    if(num1 == '') return;
    content = $mainOutput.html()
    if(('+-*/').indexOf(content[content.length-1]) != -1) return; //不能连续输入操作符

    if((op=='+' || op=='-') && (newOp=='*' || newOp=='/')){ 
        newStr = '(' + content + ')' + newOp //添加一对括号
    }
    else{
        newStr = content + newOp
    }
    $mainOutput.html(newStr)
    op = newOp
    });


    $('#resultButton').click(function() {
       content = $mainOutput.html()
       if (content == '') return ;
       if ('+-*/'.indexOf(content[content.length-1]) != -1) return;
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var result = xmlhttp.responseText;
                $mainOutput.html(result);
                num1 = result
                op = ''
            }
        }
        xmlhttp.open("POST","api/getresult")
        xmlhttp.setRequestHeader('content-type', 'application/json'); 
        xmlhttp.send(JSON.stringify({'expr':$mainOutput.html()}));
    });
});
