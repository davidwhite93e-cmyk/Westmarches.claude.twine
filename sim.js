var fs=require("fs");eval(fs.readFileSync("/tmp/check2.js","utf8"));
var v=State.variables;
var fights={wolf:{name:"Wolf",hp:11,guard:1,pool:4,dmg:2},veyle:{name:"Veyle",hp:26,guard:2,pool:5,dmg:2},vess:{name:"Vess",hp:20,guard:2,pool:5,dmg:2},kess0:{name:"Kessrick",hp:32,guard:2,pool:6,dmg:3},wraith:{name:"Wraith",hp:18,guard:2,pool:5,dmg:3}};
function setupChar(cl,party,trust){v.race="Human";v.class=cl;v.bg="Old Soldier";v.extraSkill="Stealth";v.base=Object.assign({},setup.classes[cl].rec);setup.finalize();v.party=party.slice();v.trust={};party.forEach(function(p){v.trust[p]=trust;});v.dread=0;v.potions=1;v.partyBoost=0;}
function fight(def){setup.startFight(Object.assign({},def));var f=v.fight,r=0;
 while(f.hp>0&&v.hp>0&&r<40){r++;
  if(v.hp<=5&&v.potions>0)setup.act("potion");else if(v.sparks>0&&(r===1||v.hp<v.maxhp/2))setup.act("feat");else setup.act("strike");}
 return f.hp<=0&&v.hp>0;}
var parties={"solo":[],"kess":["kess"],"wren":["wren"],"osric":["osric"],"pip":["pip"],"sable":["sable"],"gar":["gar"],"tam":["tam"],"kess+wren":["kess","wren"],"osric+gar":["osric","gar"],"pip+sable":["pip","sable"]};
var N=1500;
["Blade","Spellwright","Voice"].forEach(function(cl){console.log(cl);
 Object.keys(parties).forEach(function(pk){var row=[];
  Object.keys(fights).forEach(function(k){var w=0;for(var i=0;i<N;i++){setupChar(cl,parties[pk],0);if(fight(fights[k]))w++;}row.push(k+" "+(100*w/N).toFixed(0)+"%");});
  console.log("  "+pk.padEnd(11),row.join("  "));});});
