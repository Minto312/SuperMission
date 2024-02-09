enchant();
window.onload = function(){
  core = new Core(320, 320);
  core.fps = 16;
  core.preload('img/chara1.png','img/map.png');
  core.onload = function(){
  var map = new Map(16,16);
  map.image = core.assets['img/map.png'];
  map.loadData([
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,3,2,3,3,3,2,3,3,3,3,3],
[3,3,3,3,3,3,3,3,3,2,2,3,3,3,2,2,3,3,3,3],
[3,3,3,3,3,3,3,3,2,2,2,3,3,3,2,2,2,3,3,3],
[0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1],
]);//二次元配列
  core.rootScene.addChild(map);
  var kuma = new Sprite(32,32);
  kuma.image = core.assets['img/chara1.png'];
  kuma.frame = 5;
  kuma.x = 10;
  kuma.y = 224;
  kuma.scaleX = 1;
  kuma.scaleY = 1;
  kuma.addEventListener('enterframe',function(){
    if(core.input.right){
       kuma.rotation = 0;
       kuma.scaleX = 1;
       kuma.frame = core.frame % 2 + 6;
       this.x += 6;
    }
    if(core.input.left){
       kuma.rotation = 0;
       kuma.scaleX = -1;
       kuma.frame = core.frame % 2 + 6;
       this.x -= 5;
    }
    if(core.input.up){
       kuma.scaleX = -1;
       kuma.rotation = 90;
       kuma.frame = core.frame % 2 + 6;
       this.y -= 5;
    }
    if(core.input.down){
       kuma.scaleX = 1;
       kuma.rotation = 90;
       kuma.frame = core.frame % 2 + 6;
       this.y += 5;
    }
});//enterframe
  core.rootScene.addChild(kuma);
  var a = new Sprite(32,32);
  a.image = core.assets['img/chara1.png'];
  a.frame = 8;
  a.x = 186;
  a.y = 294;
  a.scaleX = 1;
  a.scaleY = 1;
  a.rotation = -90;
  core.rootScene.addChild(a);
  var b = new Sprite(32,32);
  b.image = core.assets['img/chara1.png'];
  b.frame = 10;
  b.x = 170;
  b.y = 160;
  b.scaleX = 1;
  b.scaleY = 1;
  b.onenterframe = function(){
  b.rotate(30);
};
  core.rootScene.addChild(b);
  var text = new Label('東海樟風');
  text.color = '#ff00ff';
  text.font = '14px sans-serif';
  text.x = 200;
  text.y = 30;
  core.rootScene.addChild(text);
};//core.onload
  core.start();
};//window.onload