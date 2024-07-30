import Livello1 from "./Livello1.js";
import Livello2 from "./Livello2.js";
import Livello3 from "./Livello3.js";
import Livello4 from "./Livello4.js";
import Livello5 from "./Livello5.js";
import GameOver from "./GameOver.js";
import Completed from "./Completed.js";
import Win from "./Win.js";
let config = {
    width: 1000,
    height: 550,
    parent: 'inizio',
    backgroundColor: 0x6888ff,
    physics:{
        default:"arcade",
        arcade:{gravity:{y:500},debug:false},
        
    },
    scene: [Livello1, Livello2, Livello3, Livello4, Livello5, GameOver, Win, Completed]
 };

 let game = new Phaser.Game(config);

 