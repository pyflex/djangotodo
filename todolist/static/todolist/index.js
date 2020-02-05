document.addEventListener("DOMContentLoaded", () => {
    
    
    
    const msg = document.getElementById("msg");
    const todoButton = document.getElementById("addTodo");
    const todoItem = document.getElementById("todoItem");

    todoButton.disabled = true;

    if (document.querySelector(".close")) {
        const cross = document.querySelector(".close");
        cross.addEventListener("click", () => {
            msg.remove();
        })
    }

    

    todoItem.addEventListener("input", () => {
        if (!todoItem.value.length == 0) {
            todoButton.disabled = false;
        } else {
            todoButton.disabled = true;
        }      
    })

    
})