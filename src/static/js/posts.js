function deleteConfirmation(id){
    const response = confirm("estas seguro?")

    if(response){
        window.location.href = "/posts/delete/" + id
    }
}