class Win extends Phaser.Scene{
    constructor(){
        super("Win")
    }

    preload(){
        this.load.image('win', './Assets/win.png');
        this.load.image('bianco', './Assets/bianco.jpg');
    }

    create(){
        var win;
        win=this.add.image(500, 274, 'win').setDepth(50).setVisible(true).setScale(2);
        this.sfondo = this.add.image(500, 274, 'bianco').setDepth(20).setScale(3.5);
    }

    update(time, delta){
    }

}

export default Win;