
console.log("Start Script")
var rows = 10;
var cols = 10;
var squareSize = 50;
var hitCount = 0;
var hitCount_Max = 0;
//var role = true;
//var gameplay = true;

var playground = document.getElementById("gameboard"); // connecting Playground
//var playground_2 =  document.getElementById("gameboard_2"); // connecting Playground_2


var gameBoard_1= [
    [0,0,0,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,0,0,0],
    [0,1,0,0,0,0,1,0,0,0],
    [0,1,0,0,0,0,1,0,0,0],
    [1,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,1,0,0]
]
/*
var gameBoard_2 = [
    [1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,0,0,0],
    [0,1,0,0,0,0,1,0,0,0],
    [0,1,0,0,0,0,1,0,0,0],
    [1,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,1,0,0]
]
*/

make_board(playground, gameBoard_1)
console.log("make_board_1");

//make_board(playground_2, gameBoard_2)
//console.log("make_board_2");

playground.addEventListener("click", function(e) {fire(e, gameBoard_1)},true);
/*
if (role == true){
    console.log("Player_1");
    // set event listener for click 
    
}else{
    console.log("Player_2");
    playground_2.addEventListener("click", function(e) {fire(e, gameBoard_2)},true);
}
*/


console.log("second Step");
function make_board(playground, gameBoard){
    // Make the playground in html using js 
    for (i = 0; i < cols; i++) {
        for (j = 0; j < rows; j++) {
            
            // Create a div element for each box in the table 
            var square = document.createElement("div"); 
            playground.appendChild(square);

        // give each div element an id 
            square.id = 's' + j + i;
        
        
        // founding out the max hit-points 
            if (gameBoard[i][j]==1){
                hitCount_Max++;
            }
            /*
            if(gameBoard[i][j]==2){ // hit one 
                square.style = "background = 'red'";
            }

            if(gameBoard[i][j]==3){ // hit not ship for now  
                square.style = "background = '#2A2A2A'";
            }

            if(gameBoard[i][j]==0){ // Not hit for now  
                square.style = "background = '#065af5'";
            }
            */

            // set each grid square's coordinates: multiples of the current row or column number
            var topPosition = j * squareSize;
            var leftPosition = i * squareSize;			
            
            // use CSS absolute positioning to place each grid square on the page
            square.style.top = topPosition + 'px';
            square.style.left = leftPosition + 'px';						
        }
    }
}


function fire(event, gameBoard) {
    
    // if item clicked (e.target) is not the parent element on which the event listener was set (e.currentTarget)
    if (event.target !== event.currentTarget) {
        console.log(gameBoard);
        // extract row and column # from the HTML element's id
        var row = event.target.id.substring(1,2);
        var col = event.target.id.substring(2,3);
        //alert("Clicked on row " + row + ", col " + col);
        
        // --------------------------------- Not hit --------------------------------------
        if (gameBoard[row][col] == 0) {
            event.target.style.background = '#2A2A2A';
            gameBoard[row][col] = 3;  // 3 = miss
            
            // ----------------------------------- Hit ----------------------------------------
        } else if (gameBoard[row][col] == 1) {
            event.target.style.background = 'red';
            gameBoard[row][col] = 2;  // 2 = hit
            
            
            // increment hitCount each time a ship is hit
            hitCount++;
            // Win alert
            if (hitCount >=  hitCount_Max) {
                alert("You win!");
            }
            
           
           
           // ---------------------------- double hit box ---------------------------------------
        } else if (gameBoard[row][col] > 1) {
            alert("You already fired at this location.");
        }
        
        
    }
    event.stopPropagation(); // Stop form propagandizing of the event to the father 
    
    //role = !role
    //return null

}


