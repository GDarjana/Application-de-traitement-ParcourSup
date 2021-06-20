// fonction forçant l'utilisateur à n'entrer que des nombres dans les zones de texte
function validate(evt) {
    var theEvent = evt || window.event;

    // Handle paste
    if (theEvent.type === 'paste') {
        key = event.clipboardData.getData('text/plain');
    } else {
    // Handle key press
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    }
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
            theEvent.returnValue = false;
            if(theEvent.preventDefault) theEvent.preventDefault();
    }
}

let math = document.querySelector('#Math');
math.addEventListener('change', function (evt) {
    if (math.checked) {
        document.getElementById("poidsNoteMath").readOnly = false;
        document.getElementById("poidsClassementMath").readOnly = false;
    }
    else{
        document.getElementById("poidsNoteMath").readOnly = true;
        document.getElementById("poidsClassementMath").readOnly = true;
    }
});

let pc = document.querySelector('#PC');
pc.addEventListener('change', function (evt) {
    if (pc.checked) {
        document.getElementById("poidsNotePC").readOnly = false;
        document.getElementById("poidsClassementPC").readOnly = false;
    }
    else{
        document.getElementById("poidsNotePC").readOnly = true;
        document.getElementById("poidsClassementPC").readOnly = true;
    }
});

let svt = document.querySelector('#SVT');
svt.addEventListener('change', function (evt) {
    if (svt.checked) {
        document.getElementById("poidsNoteSVT").readOnly = false;
        document.getElementById("poidsClassementSVT").readOnly = false;
    }
    else{
        document.getElementById("poidsNoteSVT").readOnly = true;
        document.getElementById("poidsClassementSVT").readOnly = true;
    }
});