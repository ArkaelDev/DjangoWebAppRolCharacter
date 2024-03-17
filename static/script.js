const imageView = document.querySelector("#imageview"); 
const inputFile = document.querySelector("#image-form"); 

window.addEventListener('load',(event) => {
  const option = inputFile.value;
  if (option){loadImage(option)}
});

inputFile.addEventListener('change', (event) =>{
  const option = event.currentTarget.value;
  loadImage(option ? option : 'user-circle');
});
function loadImage(option){
  let imgLink = `../static/img/${option}.svg`;
  imageView.style.backgroundImage = `url('${imgLink}')`;
  imageView.textContent = '';
  imageView.style.border = 0;
  imageView.style.backgroundColor = '#F2F4F3'
}
