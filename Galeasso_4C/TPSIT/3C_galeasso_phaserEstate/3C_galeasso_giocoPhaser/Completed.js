class Completed extends Phaser.Scene{
    constructor(){
        super("Completed")
    }

    preload(){
        this.load.image('completed', './Assets/completed.png');
    }

    create(){
        var completed;
        completed=this.add.image(500, 274, 'completed').setDepth(50).setVisible(true).setScale(3.5);
    }

    update(time, delta){
    }

}

export default Completed;