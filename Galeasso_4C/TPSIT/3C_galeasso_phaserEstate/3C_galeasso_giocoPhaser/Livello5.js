var flag;

class Livello5 extends Phaser.Scene{
    constructor(){
        super("Livello5")
    }

    preload(){
        this.load.image('TileMap', './Assets/Sfondo.png');
        this.load.image('omino', './Assets/Omino.png');
        this.load.image('star', './Assets/star.png');
        this.load.image('serpente', './Assets/serpente.png');
        this.load.image('fuoco', './Assets/fuoco.png');
        this.load.image('ragno', './Assets/ragno.png');
        this.load.image('aquila', './Assets/aquila.png');
        this.load.image('albero', './Assets/albero.png');
        this.load.image('ascia', './Assets/ascia.png');
        this.load.image('completed', './Assets/completed.jpg');
        this.load.image('bianco', './Assets/bianco.jpg');
    }

    create(){

        var stars;
        var serpente;
        var fuoco;
        var ragno;
        var aquila;
        var albero;
        var ascia;

        this.cameras.main.setBounds(0, -1150, 3000, 2000);
        this.physics.world.setBounds(0, 0, 3000, 2000);

        const level = [
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0 ],
            [ 0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,15,15,15,0,0,0,0,0,0,0,0,0,0,15,15,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,15,15,15,15,15,0,0,0,0,0,0,0,0,15,15,15,15,15,0,0,0,25,0,0,25,0,0,25,0,0,25,0,0,0,0,0,0 ],
            [ 0,15,15,15,15,15,15,15,0,0,0,0,0,0,15,15,15,15,15,15,15,0,29,30,31,29,30,31,29,30,31,29,30,31,0,0,0,0,0 ],
            [ 15,15,15,15,15,15,15,15,15,39,39,39,39,15,15,15,15,15,15,15,15,15,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14]
        ];

        const map = this.make.tilemap({ data: level, tileWidth: 16, tileHeight: 16 });
        const tiles = map.addTilesetImage("TileMap");
        const layer = map.createLayer(0, tiles, 0, 0).setScale(4.84);

        this.omino = this.physics.add.sprite(50, 700, 'omino').setScale(0.25).setDepth(1);
        serpente = this.physics.add.sprite(2500, 100, 'serpente').setScale(0.12);
        aquila = this.physics.add.sprite(500, 400, 'aquila').setScale(0.20);
        //albero = this.physics.add.sprite(2870, 200, 'albero').setScale(0.4);
        //ascia = this.physics.add.sprite(2070, 400, 'ascia').setScale(0.04);
        fuoco = this.physics.add.sprite(850, 700, 'fuoco').setScale(0.15);
        this.cameras.main.startFollow(this.omino);
        this.tastiera = this.input.keyboard.createCursorKeys();
        this.omino.setCollideWorldBounds(true);

        layer.setCollision([35,36,37,39,13,20,21,26,27]);
        layer.setCollisionBetween(14,15);

        this.physics.add.collider(this.omino,layer);

        this.physics.add.collider(serpente,layer);
        this.physics.add.collider(serpente,this.omino);

        // this.physics.add.collider(albero, layer);
        // this.physics.add.collider(albero, this.omino);

        // this.physics.add.collider(ascia, layer);

        this.physics.add.collider(fuoco, layer);

        aquila.body.setAllowGravity(false);

        stars = this.physics.add.group({
            key: 'star',
            repeat: 0,
            setXY: {
                x: 2970,
                y: 0,
                stepX: 70
            }
        });
        this.physics.add.collider(stars, layer);
        //this.physics.add.collider(this.omino, stars);

        this.physics.add.overlap(this.omino, stars, () => {
            this.scene.start("Win");
        });

        this.tweens.add({
            targets: serpente,
            props: {
                x: {
                    value: 1800,
                    duration: 1000,
                    flipX: true
                },
            },
            ease: 'Linear',
            yoyo: true,
            repeat: -1
        });

        this.tweens.add({
            targets: aquila,
            props: {
                x: {
                    value: 1300,
                    duration: 1100,
                    flipX: true
                },
            },
            ease: 'Linear',
            yoyo: true,
            repeat: -1
        });

        this.physics.add.overlap(this.omino, serpente, () => {
            this.scene.start("GameOver");
        });

        this.physics.add.overlap(this.omino, fuoco, () => {
            this.scene.start("GameOver");
        });

        this.physics.add.overlap(this.omino, aquila, () => {
            this.scene.start("GameOver");
        });

        // this.physics.add.overlap(this.omino, ascia, () => {
        //     albero.destroy(true);
        //     ascia.setVisible(false);
        // });

        this.completed = this.add.image(500, 274, 'completed').setDepth(50).setScale(1).setScrollFactor(0).setVisible(false);
        this.sfondo = this.add.image(500, 274, 'bianco').setDepth(20).setScale(3.5).setScrollFactor(0).setVisible(false);
        this.testo = this.add.text(410, 30, 'Livello 5', { fontSize: '35px', fill: '#FFED33' }).setDepth(50).setScrollFactor(0); 
    }

    update(time, delta){

        if(this.tastiera.left.isDown){
            this.omino.setVelocityX(-320);
            this.omino.setFlipX(true)
        }
        else if(this.tastiera.right.isDown){
            this.omino.setVelocityX(320);
            this.omino.setFlipX(false)
        }
        else{
            this.omino.setVelocityX(0);
        }
        if((this.tastiera.up.isDown) && this.omino.body.blocked.down){
            this.omino.setVelocityY(-330);
        }
        if(this.omino.positionY<300){
            this.scene.start("GameOver");
        }

        if(this.omino.body.position.y>1000){
            this.scene.start("GameOver");
        }
    }

}

export default Livello5;