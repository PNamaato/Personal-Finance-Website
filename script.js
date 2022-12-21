// homepage functionality
const menu = document.querySelector('#mobile_menu')
const menuLinks = document.querySelector('.navbar_menu')
const navLogo = document.querySelector('#navbar_logo')

//diplay mobile menu
const mobileMenu = () =>{
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
}

menu.addEventListener('click', mobileMenu)

// showactive menu when scrolling
const highLightMenu = () =>{
    const elem = document.querySelector('.highlight')
    const OverviewMenu = document.querySelector('#overview-page')
    const goalMenu = document.querySelector('#goals-page')
    const incomeMenu = document.querySelector('#income-page')
    let scrollPos = window.scrollY


    // adds higlight class to my menu items
    if (window.innerWidth > 960 && scrollPos< 600){
        OverviewMenu.classList.add('highlight')
        goalMenu.classList.remove('highlight')
        return
    } 
    else if (window.innerWidth > 960 && scrollPos< 1400){
        goalMenu.classList.add('highlight')
        OverviewMenu.classList.remove('highlight')
        incomeMenu.classList.remove('highlight')
        return
    }
    else if (window.innerWidth > 960 && scrollPos< 2345){
        incomeMenu.classList.add('highlight')
        goalMenu.classList.remove('highlight')        
        return
    }

    if (elem && window.innerWidth < 960 && scrollPos < 600 || elem){
        elem.classList.remove('highlight')
    }
}

window.addEventListener('scroll', highLightMenu)
window.addEventListener('click', highLightMenu)

//close mobile menu when clicking on a new menu item
const hideMobileMenu = () => {
    const menuBars = document.querySelector(".is-active")
    if (window.innerWidth <= 768 && menuBars){
        menu.classList.toggle('is-active')
        menuLinks.classList.remove('active')
    }
}

menuLinks.addEventListener('click', hideMobileMenu)
navLogo.addEventListener('click', hideMobileMenu)
// =======================================================================================================================================
