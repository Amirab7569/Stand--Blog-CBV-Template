function like(slug, pk){
    let element = document.getElementById("like")
    let count = document.getElementById("count")
    $.get(`/like/${pk}/${slug}/`).then(response =>{
        if (response["response"] == "like") {
            element.className = "fa fa-heart"
            count.innerText = Number(count.innerText) + 1;
        }else{
            element.className = "fa fa-heart-o" 
            count.innerText = Number(count.innerText) - 1;
        }
    })
}