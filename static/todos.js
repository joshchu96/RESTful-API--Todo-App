//added a click function to the class "delete-todo" allows creating js event listener to the html on client side.
$('.delete-todo').click(deleteTodo)

async function deleteTodo() {
    const id =  $(this).data('id')
    await axios.delete(`/api/todos/${id}`)
    $(this).parent().remove()
}




