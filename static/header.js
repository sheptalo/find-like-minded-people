let nav = document.createElement("NAV");
nav.classList.add('header')
nav.classList.add('navbar')
nav.classList.add('navbar-expand-lg')
nav.classList.add('bg-body-tertiary')
nav.innerHTML = '<div id="header_main" class="container-fluid">' +
    '<a class="navbar-brand" href="/">LikeMinded</a> ' +
    '<a href=\'/main\' class="link">Главная</a> ' +
    '<a href=\'/\' class="link">Найти</a> ' +
    '<a href=\'/\' class="profile link">Профиль</a> ' +
    '</div>'
document.body.appendChild(nav);