const employee = document.querySelectorAll('.employee')

const displayEmployees = (values) =>{
    employee.forEach(element =>{
        element.style.display = "none"
        const name = element.children[1].innerHTML.toUpperCase();
        const position = element.children[2].innerHTML.toUpperCase();
        const job_type = element.children[3].innerHTML.toUpperCase();

        if (name.includes(values) || position.includes(values) || job_type.includes(values)){
            element.style.display = "block"
        }
    })
}

searchEmployee.addEventListener('input', (e) =>{
    displayEmployees(e.target.value.toUpperCase())
})