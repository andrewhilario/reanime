var editbtn = document.getElementById('edit')
var editInfo = document.getElementById('edit-info')
var cancelBtn = document.getElementById('cancel')
var profCred = document.getElementById('user-info')
var review = document.getElementById('review')
var id_text = document.getElementById('id_text')
var id_rate = document.getElementById('id_rate')
var search = document.getElementById("search")

function editInfoShow(){
    editbtn.addEventListener('click', ()=>{
        editInfo.style.display = 'block'
        profCred.style.display = 'none'
    })
    cancelBtn.addEventListener('click', ()=>{
        editInfo.style.display = 'none'
        profCred.style.display = 'block'
    })
    review.addEventListener('click', ()=>{
        location.reload = ()=>{
            id_text.value=' '
            id_rate.value=' '
        }
    })

}
editInfoShow()

search.onclick = ()=>{
    location.href = "/search"
}