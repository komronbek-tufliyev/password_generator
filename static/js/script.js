
document.getElementById('btn_copy').addEventListener(
    'click', 
    ()=>{
        let text = document.getElementById('password');
        console.log(text);
        
        text.select();
        text.setSelectionRange(0, 99999);
        
        navigator.clipboard.writeText(text.value);
        alert("Copied password: " + text.value);
        console.log('Password copied!');
        // document.getElementById('password').nodeValue=text;
    }
)