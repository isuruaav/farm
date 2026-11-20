const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
function node(dataset={}){
  const attributes=new Map(),listeners=new Map(),classes=new Set();
  return {dataset,attributes,listeners,hidden:false,tabIndex:0,focused:false,
    classList:{toggle(name,enabled){if(enabled)classes.add(name);else classes.delete(name);}},
    setAttribute(name,value){attributes.set(name,value);},focus(){this.focused=true;},
    addEventListener(name,callback){listeners.set(name,callback);}};
}
const choices=['poultry','feed','mushrooms'].map(slug=>node({industryChoice:slug}));
const panels=['poultry','feed','mushrooms'].map(slug=>node({industryPanel:slug}));
const list=node(),gallery=node({gallerySrc:'assets/images/industries/mushrooms.jpg',galleryCaption:'Illustrative mushrooms'});
const explorer={querySelector:()=>list,querySelectorAll:selector=>selector==='[data-industry-choice]'?choices:panels};
let ready,opened;
const document={addEventListener(name,callback){if(name==='DOMContentLoaded')ready=callback;},querySelectorAll(selector){return selector==='[data-industry-explorer]'?[explorer]:selector==='[data-gallery-src]'?[gallery]:[];},querySelector(){return null;}};
vm.runInNewContext(fs.readFileSync('assets/js/experience.js','utf8'),{document,URLSearchParams,location:{search:''},openGalleryModal:(src,caption)=>opened={src,caption}});
ready();
assert.equal(list.attributes.get('role'),'tablist');
assert.equal(choices[0].attributes.get('aria-selected'),'true');
assert.deepEqual(panels.map(panel=>panel.hidden),[false,true,true]);
let prevented=false;
choices[1].listeners.get('click')({preventDefault(){prevented=true;}});
assert.ok(prevented);assert.equal(choices[1].tabIndex,0);assert.equal(choices[0].tabIndex,-1);
assert.deepEqual(panels.map(panel=>panel.hidden),[true,false,true]);
choices[1].listeners.get('keydown')({key:'End',preventDefault(){}});
assert.equal(choices[2].attributes.get('aria-selected'),'true');assert.ok(choices[2].focused);
choices[2].listeners.get('keydown')({key:'ArrowRight',preventDefault(){}});
assert.equal(choices[0].attributes.get('aria-selected'),'true');
assert.equal(panels[2].attributes.get('aria-labelledby'),'sector-choice-mushrooms');
gallery.listeners.get('click')();
assert.deepEqual(opened,{src:'assets/images/industries/mushrooms.jpg',caption:'Illustrative mushrooms'});
console.log('PASS: Industry tab selection, keyboard navigation, focus state, panel accessibility and local gallery actions.');
