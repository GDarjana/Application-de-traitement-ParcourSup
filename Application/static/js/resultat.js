
/*
* Parcours des cellules du tableau et identifie ceux qui ont un "∆" , puis leur attribue une couleur en fonction du contenu.
*/
var cells = document.getElementById("tableau").getElementsByTagName("td");
for (var i = 0 ; i<cells.length;i++){
    var index = Array.prototype.indexOf.call(cells[i].parentNode.children, cells[i])
    var corresponding_th = document.querySelector('#tableau th:nth-child(' + (index+1) + ')')
    //---------------------- ∆ matières ----------------------------//
    if ((corresponding_th.innerText).includes('∆')==true){
 //Positif
 if (cells[i].innerText >0.01 && cells[i].innerText <0.5) cells[i].style.backgroundColor='#b6eda4';
 else if (cells[i].innerText >=0.5 && cells[i].innerText <1) cells[i].style.backgroundColor='#a1ed87';
 else if (cells[i].innerText >=1 && cells[i].innerText <2) cells[i].style.backgroundColor='#90f170';
 else if (cells[i].innerText >=2 && cells[i].innerText <4) cells[i].style.backgroundColor='#4ecf42';
 else if (cells[i].innerText >=4 && cells[i].innerText <6) cells[i].style.backgroundColor='#1fd40f';
 else if (cells[i].innerText >=6 && cells[i].innerText <=7) cells[i].style.backgroundColor='#15b007';
 else if (cells[i].innerText >7) cells[i].style.backgroundColor='#0e9c02';
 
 //Négatif
 else if (cells[i].innerText <-0.01 && cells[i].innerText >-0.5) cells[i].style.backgroundColor='#e6877e';
 else if (cells[i].innerText <=-0.5 && cells[i].innerText >-1) cells[i].style.backgroundColor='#e6877e';
 else if (cells[i].innerText <=-1 && cells[i].innerText >-2) cells[i].style.backgroundColor='#e67065';
 else if (cells[i].innerText <=-2 && cells[i].innerText >-4) cells[i].style.backgroundColor='#d95448';
 else if (cells[i].innerText <=-4 && cells[i].innerText >-6) cells[i].style.backgroundColor='#c44337';
 else if (cells[i].innerText <=-6 && cells[i].innerText >-7) cells[i].style.backgroundColor='#ad3226';
 else if (cells[i].innerText <-7) cells[i].style.backgroundColor='#8f1c11';
 
    }
    //---------------------- Matières ----------------------------//
    if ((corresponding_th.innerText).includes('Math Terminale')==true){
 cells[i].style.backgroundColor='#f7a457';
 corresponding_th.style.backgroundColor='#f7a457';
    }
    if ((corresponding_th.innerText).includes('Physique/Chimie Terminale')==true){
 cells[i].style.backgroundColor='#f1ea60';
 corresponding_th.style.backgroundColor='#f1ea60';
    }
    if ((corresponding_th.innerText).includes('SVT Terminale')==true){
 cells[i].style.backgroundColor='#e88ff7';
 corresponding_th.style.backgroundColor='#e88ff7';
    }
    //---------------------- TOTAUX ----------------------------//
    if ((corresponding_th.innerText).includes('Total terminale')==true){
 cells[i].style.backgroundColor='#91daff';
    }
    if ((corresponding_th.innerText).includes('Bilan Total')==true){
 cells[i].style.fontWeight='bold';
    }
}
/*
* Création des en-têtes.
*/
var table = document.getElementById("tableau");
var header = table.createTHead();
var row = header.insertRow(0);

var terminale_math = false;
var terminale_pc = false;
var terminale_svt = false;

var headers = document.getElementById("tableau").getElementsByTagName("th");
var len = headers.length;


var premiere_math = false;
var premiere_pc = false;
var premiere_svt = false;

var index = 4;
for (var i = 0 ; i< len ; i++){
//---------------------- Terminal ----------------------------//
    if ((headers[i].innerText).includes('Math') == true && terminale_math == false){
        var cell = row.insertCell(index);
        cell.colSpan="4";
        cell.innerText="Mathématiques Terminale";
        terminale_math = true;
        len = len -3;
        index++;
    }
    else if ((headers[i].innerText).includes('Physique/Chimie') == true && terminale_pc == false ){
        var cell = row.insertCell(index);
        cell.colSpan="4";
        cell.innerText="Physique/Chimie Terminale";
        terminale_pc = true;
        len = len -3;
        index++;
    }
    else if ((headers[i].innerText).includes('SVT') == true && terminale_svt == false ){
        var cell = row.insertCell(index);
        cell.colSpan="4";
        cell.innerText="Sciences de la Vie et de la Terre Terminale";
        terminale_svt = true;
        len = len -3;
        index++;
    }
    //---------------------- Première ----------------------------//
    else if ((headers[i].innerText).includes('math (1ère)') && premiere_math == false) {
        var cell = row.insertCell(index);
        cell.colSpan="4";
        cell.innerText="Mathématiques Première";
        premiere_math = true;
        len = len-3;
        index++;
    }
    else if ((headers[i].innerText).includes('Physique/Chimie (1ère)') && premiere_pc == false) {
        var cell = row.insertCell(index);
        cell.colSpan="4";
        cell.innerText="Physique/Chimie Première";
        premiere_pc = true;
        len = len-3;
        index++;
    } 
    else if ((headers[i].innerText).includes('SVT (1ère)') && premiere_svt == false) {
        var cell = row.insertCell(index);
        cell.colSpan="4";
        cell.innerText="Sciences de la Vie et de la Terre Première";
        premiere_svt = true;
        len = len-3;
        index++;
    } 
    else{
        var empty_cell = row.insertCell(i);
        empty_cell.style.display='hide';
        if (i<3){
            empty_cell.style.borderTop='1px solid white';
            empty_cell.style.borderLeft='1px solid white';
            empty_cell.style.borderRight='1px solid white';
        }
        else if (i==3){
            empty_cell.style.borderTop='1px solid white';
            empty_cell.style.borderLeft='1px solid white';
        }
        else if (i>index){
            empty_cell.style.display='none';
        }
    }
}
//---------------------- Compétences || Notes Lycée ----------------------------//
var h_competences = (document.getElementById("tableau").rows[0].cells[index]);
h_competences.style.display='table-cell';
h_competences.innerText="Compétences";
h_competences.colSpan='7';
h_competences.style.borderRight='1px solid black';
index++;
var h_lycee = (document.getElementById("tableau").rows[0].cells[index]);
h_lycee.style.display='table-cell';
h_lycee.innerText="Notes anticipées au Lycée";
h_lycee.colSpan='3';
h_lycee.style.borderRight='1px solid black';
index++;
var h_total = (document.getElementById("tableau").rows[0].cells[index]);
h_total.style.display='table-cell';
h_total.innerHTML="<b>TOTAUX</b>";
h_total.colSpan='2';
h_total.style.borderRight='1px solid black';



//---------------------- HOVER ----------------------------//
jQuery(document).ready(function(){
 jQuery('[data-toggle="tooltip"]').tooltip();
});


/*
* Code pour le classement au clique sur l'header de la  colonne concernée , décroissant / croissant .
*/
const compare = (ids, asc) => (row1, row2) => {
const tdValue = (row, ids) => row.children[ids].textContent;
const tri = (v1, v2) => v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2);
return tri(tdValue(asc ? row1 : row2, ids), tdValue(asc ? row2 : row1, ids));
};

const tbody = document.querySelector('tbody');
const thx = document.querySelectorAll('th');
const trxb = tbody.querySelectorAll('tr');
thx.forEach(th => th.addEventListener('click', () => {
let classe = Array.from(trxb).sort(compare(Array.from(thx).indexOf(th), this.asc = !this.asc));
classe.forEach(tr => tbody.appendChild(tr));
}));