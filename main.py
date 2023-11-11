@namespace
class SpriteKind:
    Item = SpriteKind.create()
    Button = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(1)
    Item2.destroy(effects.rings, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Item, on_on_overlap)

def on_overlap_tile(sprite2, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def on_a_pressed():
    global projectile
    if controller.A.is_pressed():
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . 3 1 1 3 . . . . . . 
                            . . . . . 2 1 1 1 1 2 . . . . . 
                            . . . . . 2 1 1 1 1 2 . . . . . 
                            . . . . . . 3 1 1 3 . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite3, location2):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile2)

def on_on_overlap2(sprite4, otherSprite2):
    info.change_life_by(-1)
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap2)

def on_overlap_tile3(sprite5, location3):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile3)

def on_on_overlap3(sprite6, otherSprite3):
    info.change_score_by(100)
    Button2.destroy(effects.confetti, 200)
sprites.on_overlap(SpriteKind.player, SpriteKind.Button, on_on_overlap3)

def on_on_overlap4(sprite7, otherSprite4):
    info.change_life_by(-1)
    otherSprite4.destroy(effects.spray, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

projectile: Sprite = None
Button2: Sprite = None
Item2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . f f f . f f f f . f f f . 
            f f f f f c c c c f f f f f 
            f f f f b c c c c b f f f f 
            f f f c 3 c c c c 3 c f f f 
            . f 3 3 c c c c c c 3 3 f . 
            . f c c c c 4 4 c c c c f . 
            . f f c c 4 4 4 4 c c f f . 
            . f f f b f 4 4 f b f f f . 
            . f f 4 1 f d d f 1 4 f f . 
            . . f f d d d d d d f f . . 
            . . e f e 4 4 4 4 e f e . . 
            . e 4 f b 3 3 3 3 b f 4 e . 
            . 4 d f 3 3 3 3 3 3 c d 4 . 
            . 4 4 f 6 6 6 6 6 6 f 4 4 . 
            . . . . f f f f f f . . . . 
            . . . . f f . . f f . . . .
    """),
    SpriteKind.player)
info.set_life(3)
myEnemy = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ...........fff..........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.enemy)
mySprite.set_position(500, 120)
myEnemy.set_position(70, 70)
scene.set_background_color(7)
tiles.set_tilemap(tilemap("""
    level1
"""))
MyEnemy2 = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ...........fff..........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.enemy)
MyEnemy2.set_position(143, 81)
myEnemy3 = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ...........fff..........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.enemy)
myEnemy3.set_position(70, 100)
Item2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . 4 4 4 5 5 4 4 4 . . . . 
            . . . 3 3 3 3 4 4 4 4 4 4 . . . 
            . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
            . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
            . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
            . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
            . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
            . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
            . . . 4 2 2 2 2 2 2 2 2 4 . . . 
            . . . . 4 4 2 2 2 2 4 4 . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Item)
Item2.set_position(539, 104)
Button2 = sprites.create(img("""
        b b b b b b b b b b b b b b b b 
            b c b a 3 3 3 3 3 3 3 3 a b c b 
            b b a 3 3 3 3 3 3 3 3 3 3 a b b 
            b b 3 3 3 3 3 3 3 3 3 3 3 3 b b 
            b b 3 3 3 3 3 3 3 3 3 3 3 3 b b 
            b b 3 3 3 3 3 3 3 3 3 3 3 3 b b 
            b b 3 3 3 3 3 3 3 3 3 3 3 3 b b 
            b b 3 3 3 3 3 3 3 3 3 3 3 3 b b 
            b b 1 3 3 3 3 3 3 3 3 3 3 1 b b 
            b b 1 3 3 3 3 3 3 3 3 3 3 1 b b 
            b b 3 1 3 3 3 3 3 3 3 3 1 3 b b 
            b b 3 3 1 1 1 1 1 1 1 1 3 3 b b 
            b b c 3 3 3 3 3 3 3 3 3 3 c b b 
            b b b c c c c c c c c c c b b b 
            b c b b b b b b b b b b b b c b 
            b b b b b b b b b b b b b b b b
    """),
    SpriteKind.Button)
Button2.set_position(10, 88)
Turrets = sprites.create(img("""
        . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c b . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . c 4 . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . e 4 . . . . . . . 
            . . . . . . e e 5 2 . . . . . . 
            . . . . . . e 4 5 2 . . . . . . 
            . . . . . c c c 2 2 2 . . . . . 
            . . . . e e 4 4 4 5 2 2 . . . . 
            . . e f f f c c 2 2 f f 2 2 . . 
            . e e e e 2 2 4 4 4 4 5 4 2 2 . 
            e e e e e e 2 2 4 4 4 5 4 4 2 2 
            e e e e e e 2 2 4 4 4 4 5 4 2 2
    """),
    SpriteKind.enemy)
Turrets.set_position(345, 250)

def on_on_update():
    controller.move_sprite(mySprite)
    scene.camera_follow_sprite(mySprite)
    myEnemy.follow(mySprite, 20)
    MyEnemy2.follow(mySprite, 20)
    myEnemy3.follow(mySprite, 20)
    if mySprite.x < 0:
        mySprite.set_image(assets.image("""
            myImage0
        """))
    elif mySprite.x >= 0:
        mySprite.set_image(img("""
            . f f f . f f f f . f f f . 
                        f f f f f c c c c f f f f f 
                        f f f f b c c c c b f f f f 
                        f f f c 3 c c c c 3 c f f f 
                        . f 3 3 c c c c c c 3 3 f . 
                        . f c c c c 4 4 c c c c f . 
                        . f f c c 4 4 4 4 c c f f . 
                        . f f f b f 4 4 f b f f f . 
                        . f f 4 1 f d d f 1 4 f f . 
                        . . f f d d d d d d f f . . 
                        . . e f e 4 4 4 4 e f e . . 
                        . e 4 f b 3 3 3 3 b f 4 e . 
                        . 4 d f 3 3 3 3 3 3 c d 4 . 
                        . 4 4 f 6 6 6 6 6 6 f 4 4 . 
                        . . . . f f f f f f . . . . 
                        . . . . f f . . f f . . . .
        """))
    if mySprite.x < 0:
        mySprite.set_image(img("""
            . . . . f f f f f . f f f . 
                        . . . f f c c c c f f f f f 
                        . . f c c c c c c b f f f f 
                        . . f c c c c c c 3 c f f f 
                        . f c c c c c c c c 3 3 f . 
                        . f c c 4 c c c c c f f f . 
                        . f f e 4 4 c c c f f f f . 
                        . f f e 4 4 f b f 4 4 f f . 
                        . . f f d d f 1 4 d 4 f . . 
                        . . . f d d d d 4 f f f . . 
                        . . . f e 4 4 4 e e f . . . 
                        . . . f 3 3 3 e d d 4 . . . 
                        . . . f 3 3 3 e d d e . . . 
                        . . . f 6 6 6 f e e f . . . 
                        . . . . f f f f f f . . . . 
                        . . . . . . f f f . . . . .
        """))
    elif mySprite.x > 0:
        mySprite.set_image(img("""
            . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 e f f . 
                        . f f 4 4 f b f 4 4 e f f . 
                        . . f 4 d 4 1 f d d f f . . 
                        . . f f f 4 d d d d f . . . 
                        . . . f e e 4 4 4 e f . . . 
                        . . . 4 d d e 3 3 3 f . . . 
                        . . . e d d e 3 3 3 f . . . 
                        . . . f e e f 6 6 6 f . . . 
                        . . . . f f f f f f . . . . 
                        . . . . . f f f . . . . . .
        """))
game.on_update(on_on_update)

def on_forever():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . 3 1 1 3 . . . . . . 
                    . . . . . 2 1 1 1 1 2 . . . . . 
                    . . . . . 2 1 1 1 1 2 . . . . . 
                    . . . . . . 3 1 1 3 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Turrets,
        0,
        -100)
    pause(2000)
forever(on_forever)
