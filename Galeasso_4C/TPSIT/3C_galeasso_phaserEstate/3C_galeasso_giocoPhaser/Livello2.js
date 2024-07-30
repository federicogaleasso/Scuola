var flag;

class Livello2 extends Phaser.Scene{
    constructor(){
        super("Livello2")
    }

    preload(){
        this.load.image('TileMap', './Assets/Sfondo.png');
        this.load.image('omino', './Assets/Omino.png');
        this.load.image('star', './Assets/star.png');
        this.load.image('serpente', './Assets/serpente.png');
        this.load.image('fuoco', './Assets/fuoco.png');
        this.load.image('cactus', './Assets/cactus.png');
        this.load.image('completed', './Assets/completed.jpg');
        this.load.image('bianco', './Assets/bianco.jpg');
    }

    create(){

        var stars;
        var serpente;
        var fuoco;
        var cactus;

        this.cameras.main.setBounds(0, -1150, 3000, 2000);
        this.physics.world.setBounds(0, 0, 3000, 2000);

        const level = [
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
            [ 0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,39,0,0,0,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,39,39,0,0,,0,0,0 ],
            [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,39,39,39,0,,0,0,0,0 ],
            [ 39,39,0,0,39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,39,39,39,39,0,0,0,0,0,0 ],
            [ 39,39,0,0,39,0,0,0,39,39,0,0,0,0,0,0,0,0,0,0,0,35,36,37,0,0,0,0,39,39,39,39,39,35,36,37,0,0,0 ],
            [ 39,39,39,39,39,0,0,0,39,39,0,0,39,0,0,39,39,39,39,39,39,39,39,39,39,0,0,0,39,39,39,39,39,39,39,39,39,39,39 ]
        ];

        const map = this.make.tilemap({ data: level, tileWidth: 16, tileHeight: 16 });
        const tiles = map.addTilesetImage("TileMap");
        const layer = map.createLayer(0, tiles, 0, 0).setScale(4.84);

        this.omino = this.physics.add.sprite(100, 400, 'omino').setScale(0.25).setDepth(1);
        serpente = this.physics.add.sprite(1800, 450, 'serpente').setScale(0.12);
        fuoco = this.physics.add.sprite(230, 700, 'fuoco').setScale(0.09);
        cactus = this.physics.add.sprite(750, 668, 'cactus').setScale(0.15);
        this.cameras.main.startFollow(this.omino);
        this.tastiera = this.input.keyboard.createCursorKeys();
        this.omino.setCollideWorldBounds(true);

        layer.setCollision([39,13,20,21,26,27]);
        layer.setCollisionBetween(14,15);

        this.physics.add.collider(this.omino,layer);
        this.physics.add.collider(serpente,layer);
        this.physics.add.collider(serpente,this.omino);

        this.physics.add.collider(fuoco, layer);
        this.physics.add.collider(this.omino, fuoco);

        this.physics.add.collider(cactus, layer);

        stars = this.physics.add.group({
            key: 'star',
            repeat: 0,
            setXY: {
                x: 2950,
                y: 0,
                stepX: 70
            }
        });
        this.physics.add.collider(stars, layer);
        //this.physics.add.collider(this.omino, stars);

        this.physics.add.overlap(this.omino, stars, () => {
            flag=1;
        });

        this.tweens.add({
            targets: serpente,
            props: {
                x: {
                    value: 1300,
                    duration: 2000,
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

        this.physics.add.overlap(this.omino, cactus, () => {
            this.scene.start("GameOver");
        });

        this.completed = this.add.image(500, 274, 'completed').setDepth(50).setScale(1).setScrollFactor(0).setVisible(false);
        this.sfondo = this.add.image(500, 274, 'bianco').setDepth(20).setScale(3.5).setScrollFactor(0).setVisible(false);
        this.testo = this.add.text(410, 30, 'Livello 2', { fontSize: '35px', fill: '#FFED33' }).setDepth(50).setScrollFactor(0); 
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

        if(this.omino.body.position.y>1000){
            this.scene.start("GameOver");
        }

        if(flag==1 && this.tastiera.space.isDown){
            this.scene.start("Livello3");
        }

        if(flag==1){
            this.completed.setVisible(true);
            this.sfondo.setVisible(true);
            //this.testo.setVisible(false);
        }
    }

}

export default Livello2;