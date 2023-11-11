// Código generado automáticamente. No editar.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const tile1 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level2":
            case "level2":return tiles.createTilemap(hex`1000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
`, [myTiles.transparency16], TileScale.Sixteen);
            case "level1":
            case "level1":return tiles.createTilemap(hex`230010000101010101010101010101010101010101222828282828282828282828282828282829130b0b0b0b0b0b0b0b0b0b0b0b0b0b130123262020202020202020202626202720262a0f08080708080808070807080808082c0123262026202626202626202626202020262a130b0b060b0b0b0b060b060b0b0b0b130123262026202626202626202626262026262a0b0b0b1408080808120b060b0b0b100a0123262026202020202626202626262026262a2d0b0b0b0b0b0b0b0b0b0f080a0b0f110123262026261e2c262626202626262026262a090708080807080807081213060b061e0123262020202020202020202020262026202a18061a1c19061a19061a1c19060b061a0123262026202626262026262620262026202a18061b1d18061b180f080a18060b061b0123262026202626262026262620262026202a1806151617061b18061b06180f08111b0123262026202626262026262020202026202a1009080a13061b18061b0618061c061b012326202620262626202626201e2c2026202a061a19061b061b18061b06180616061b012326202620262626202626202c1e2026202a061b18061b0f0808111b06181408121b0123262026202020202020202020202026202a061517061b061517061b061616161616012425202520252525252525252525252b202a140808121b140808121b1408080808081f20202020202020202020202020202020202b02030504050302030d030e0c020c050401212121212121212121212121212121212121`, img`
22222222222222222222222222222222222
2222222222222222222.........22...22
................222.2.22.22.22...22
222.2222.2.22222222.2.22.22.222.222
222......2.222..222.2....22.222.222
.222222222...2..222.22..222.222.222
...........2.2..222...........2.2.2
2.222.22.222.2.2222.2.222.222.2.2.2
2.222.22...2.2.2222.2.222.222.2.2.2
2.222.22.2.2...2222.2.222.22....2.2
....2.22.2.2.2.2222.2.222.22....2.2
.22.2.22.2.2.2.2222.2.222.22....2.2
.22.2....2.2...2222.2...........2.2
.22.2.22.2.22222222.2.22222222222.2
....2....2........................2
22222222222222222222222222222222222
`, [myTiles.transparency16,sprites.dungeon.floorMixed,sprites.builtin.crowd2,sprites.builtin.crowd3,sprites.builtin.crowd5,sprites.builtin.crowd8,sprites.vehicle.roadVertical,sprites.vehicle.roadIntersection3,sprites.vehicle.roadHorizontal,sprites.vehicle.roadIntersection1,sprites.vehicle.roadTurn2,sprites.builtin.brick,sprites.builtin.crowd9,sprites.builtin.crowd6,sprites.builtin.crowd0,sprites.vehicle.roadIntersection2,sprites.vehicle.roadTurn1,sprites.vehicle.roadIntersection4,sprites.vehicle.roadTurn4,sprites.castle.saplingPine,sprites.vehicle.roadTurn3,sprites.skillmap.islandTile6,sprites.skillmap.islandTile7,sprites.skillmap.islandTile8,sprites.skillmap.islandTile5,sprites.skillmap.islandTile2,sprites.skillmap.islandTile0,sprites.skillmap.islandTile3,sprites.skillmap.islandTile1,sprites.skillmap.islandTile4,sprites.dungeon.hazardLava0,sprites.dungeon.stairWest,sprites.dungeon.floorLight2,sprites.dungeon.floorDark5,sprites.dungeon.darkGroundNorthWest0,sprites.dungeon.darkGroundWest,sprites.dungeon.darkGroundSouthWest0,sprites.dungeon.darkGroundSouth,sprites.dungeon.darkGroundCenter,sprites.dungeon.chestClosed,sprites.dungeon.darkGroundNorth,sprites.dungeon.darkGroundNorthEast0,sprites.dungeon.darkGroundEast,sprites.dungeon.darkGroundSouthEast0,sprites.dungeon.hazardLava1,sprites.swamp.swampTile16], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "myTile":
            case "tile1":return tile1;
            case "transparency16":return transparency16;
        }
        return null;
    })

}
// Código generado automáticamente. No editar.
