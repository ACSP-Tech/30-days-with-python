// Toggle Dropdown
const dropDown = document.querySelector('.navbar');
const dropDownList = document.querySelectorAll('.drop_list');

dropDown.addEventListener('click', e =>{
    const target = e.target

    if(target.id == 'hamburgerMenu'){
        headerNav.classList.toggle('open_nav')
    }
    else if(target.className == 'dropdown_btn'){
        target.parentElement.parentElement.classList.toggle('dropdown')
        target.parentElement.children[1].classList.toggle('rotate')

    }else if(target.className != 'dropdown_btn'){
        for (let i = 0; i < dropDownList.length; i++) {
            dropDownList[i].classList.remove('dropdown');
            
        }
    }
})