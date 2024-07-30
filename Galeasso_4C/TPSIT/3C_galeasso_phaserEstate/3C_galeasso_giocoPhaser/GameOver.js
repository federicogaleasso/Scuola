class GameOver extends Phaser.Scene{
    constructor(){
        super("GameOver")
    }

    preload(){
        this.load.image('gameover', './Assets/gameover.png');
        this.load.image('bianco', './Assets/bianco.png');
    }

    create(){
        var gameover;
        gameover=this.add.image(500, 274, 'gameover').setDepth(50).setVisible(true).setScale(1.2);
        this.sfondo = this.add.image(500, 274, 'bianco').setDepth(20).setScale(3.5);
    }

    update(time, delta){
    }

}

export default GameOver;