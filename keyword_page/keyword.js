document.addEventListener('DOMContentLoaded', ()=>{
    var interval = window.setInterval(rollingCallback, 2000);
})
function rollingCallback(){
    //.prev 클래스 삭제
    document.querySelector('.rollingbanner .prev').classList.remove('prev');

    //.current -> .prev
    let current = document.querySelector('.rollingbanner .current');
    current.classList.remove('current');
    current.classList.add('prev');

    //.next -> .current
    let next = document.querySelector('.rollingbanner .next');
    //다음 목록 요소가 널인지 체크
    if(next.nextElementSibling == null){
        document.querySelector('.rollingbanner ul li:first-child').classList.add('next');
    }else{
        //목록 처음 요소를 다음 요소로 선택
        next.nextElementSibling.classList.add('next');
    }
    next.classList.remove('next');
    next.classList.add('current');
}