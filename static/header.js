let nav = document.createElement("NAV");
let txt;
if(user !== ''){
    txt = `<li class=\'nav-item\'><a href=\'/user/${user}\' class=\'profile link nav-link\'>Профиль</a></li>`;
} else{
    txt = '<li class="nav-item"><a href=\'/auth/register\' class="profile link nav-link">Зарегистрироваться</a></li>';
}
nav.classList.add('header')
nav.classList.add('navbar')
nav.classList.add('navbar-expand-lg')
nav.classList.add('bg-body-tertiary')
nav.innerHTML = '<div id="header_main" class="container-fluid">' +
    '<a class="navbar-brand" href="/">LikeMinded</a> ' +
    '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\n' +
    '<span class="navbar-toggler-icon"></span>\n' +
    '</button>' +
    '<div class="collapse navbar-collapse" id="navbarSupportedContent">' +
    '<ul class="navbar-nav me-auto mb-2 mb-lg-0">' +
    '<li class="nav-item"><a href=\'/main\' class="link nav-link">Главная</a></li> ' +
    '<li class="nav-item"><a href=\'/\' class="link nav-link">Написать</a></li> ' +
    txt +
    '<li class="nav-item"><a href=\'/search\' class="link nav-link">Поиск</a></li> ' +
    '</div>' +
    '</div><br>'
document.body.appendChild(nav);