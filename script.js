function contagemPI(){
    for(n=0; n<101; n++){
        if (n%2!=0){
            console.log(n+" - Ímpar" );
        }
        else{
            console.log(n+" - Par")
        }
    
    }

}
function calculo(){
    num1=parseFloat(prompt("Insira o primeiro valor: "))
    num2=parseFloat(prompt("Insira o segundo valor: "))
    escolha=parseInt(prompt("Escolha sua operação matematica: \n[1]Adição\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n[5]Mostrar todas as opereções"))    
    switch (escolha) {
        case 1:
            resultado=num1+num2
            resultado.toFixed(2)
            alert("A soma dos valores é: " +resultado.toFixed(2))
            break;
        case 2:
            resultado=num1-num2
            resultado.toFixed(2)
            alert("A subtração dos valores é: " +resultado.toFixed(2))
            break;
        case 3:
            resultado=num1*num2
            resultado.toFixed(2)
            alert("A multiplicação dos valores é: " +resultado.toFixed(2))
            break;
        case 4:
            resultado=num1/num2
            resultado.toFixed(2)
            alert("A divisão dos valores é: " +resultado.toFixed(2))
            break;
        case 5:
            resultado1=num1+num2
            resultado1.toFixed(2) 

            resultado2=num1-num2
            

            resultado3=num1*num2
            

            resultado4=num1/num2
            
            alert("O resultado de todas as operações: \n Soma: "+resultado1.toFixed(2)+ "\n Subtração: " + resultado2.toFixed(2) + "\n Multiplicação: " + resultado3.toFixed(2)+ "\n Divisão: "+ resultado4.toFixed(2))
        
        default:
            break;
    }

}
document.getElementById("button1").addEventListener("click", contagemPI);
document.getElementById("button2").addEventListener("click",calculo)