const searchInput = document.querySelector('#search')
const list = document.querySelector('.charlist')
const characters = list.querySelectorAll('a')

let charList = []

characters.forEach(character=>{
    const nodeName = character.querySelectorAll('[charname]')
    const nodeRace = character.querySelectorAll('[race]')
    const nodeClasses = character.querySelectorAll('[classes]')
    const charInfo = {name: nodeName.item(0).textContent, race: nodeRace.item(0).textContent,
         classes: nodeClasses.item(0).textContent, card: character}
    charList.push(charInfo)
})
searchInput.addEventListener('input', e =>{
    const value = e.target.value.toLowerCase()
    charList.forEach(char =>{
        const isVisible = char.name.toLowerCase().includes(value) ||char.race.toLowerCase().includes(value) 
        ||char.classes.toLowerCase().includes(value)
        char.card.toggleAttribute('hidden', !isVisible)
    })
})