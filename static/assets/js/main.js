/*===== MENU SHOW =====*/
const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId)

    if (toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('show')
        })
    }
}
showMenu('nav-toggle', 'nav-menu')


/*==================== REMOVE MENU MOBILE ====================*/
const navLink = document.querySelectorAll('.nav__link');

function linkAction() {
    /*Active link*/
    navLink.forEach(n => n.classList.remove('active'));
    this.classList.add('active');

    /*Remove menu mobile*/
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction));


/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '65px',
    duration: 2000,
    reset: true
});

/*SCROLL HOME*/
sr.reveal('.home__subtitle', {});
sr.reveal('.button', { delay: 200 });
sr.reveal('.home__img', {});
sr.reveal('.home__social-icon', { interval: 200 });

sr.reveal('.Box', {});
sr.reveal('.bannergreeting', { interval: 200 });
sr.reveal('.bannerbody', { interval: 250 });



sr.reveal('.line', { delay: 500 });


/*SCROLL ABOUT*/
sr.reveal('.about__img', { delay: 250 })
sr.reveal('.about__subtitle', { delay: 250 })
sr.reveal('.about__profession', { delay: 100 })
sr.reveal('.about__text', { delay: 350 })
sr.reveal('.about__social-icon', { delay: 450, interval: 200 })
sr.reveal('.more__about__img', { delay: 450 })

/*SCROLL EXPLORE */
sr.reveal('.explore-title', {});
sr.reveal('.explore__box', { delay: 150, interval: 200 });

/*SCROLL FEATURED */
sr.reveal('.section-title', {});
sr.reveal('.', {});
sr.reveal('.featured-item', { interval: 150 });

/*SCROLL Projects */
sr.reveal('.project_item', { interval: 250 });
sr.reveal('.category', { delay: 450, interval: 150 });


/*SCROLL SEARCH */
// sr.reveal('.article-meta', {});
// sr.reveal('.bx', {});
// sr.reveal('.all', {});
sr.reveal('.tag', {});

/*SCROLL CONTACT*/
sr.reveal('.contact_message', {})
sr.reveal('.contact__subtitle', {})
sr.reveal('.contact__text', { delay: 90 })
sr.reveal('.contact__input', { delay: 100 })
sr.reveal('.contact__button', {})



// /*====== Dark Light Theme==========*/ 
// Using localStorage to store the key value pairs in the browser with no expiration date, similar to cookies but they have expiration date
// The big difference is that data is never sent back to the server
// For privacy concerns or if it is only client side, we can use localStorage

let darkMode = localStorage.getItem('darkMode'); // see if there is darkMode in localStorage
const darkModeToggle = document.querySelector('#icon');

// check if dark mode is enabled 
// if it is enabled, turn it off
// if it is disabled, turn it on

const enableDarkMode = () => {
    // 1. add the class darkmode to the body
    document.body.classList.add('dark-theme');
    // 2. update darkMode in the localStorage
    localStorage.setItem('darkMode', 'enabled');
};

const disableDarkMode = () => {
    // 1. add the class darkmode to the body
    document.body.classList.remove('dark-theme');
    // 2. update darkMode in the localStorage
    localStorage.setItem('darkMode', null);
};

if (darkMode === 'enabled') {
    darkModeToggle.className = "bx bx-sun";
    enableDarkMode();
}

darkModeToggle.addEventListener('click', () => {
    darkMode = localStorage.getItem('darkMode');
    if (darkMode !== 'enabled') {
        enableDarkMode();
        darkModeToggle.className = "bx bx-sun";
        console.log(darkMode);
    } else {
        disableDarkMode();
        darkModeToggle.className = "bx bx-moon";
        console.log(darkMode);

    }
})


// var icon = document.getElementById("icon");

// icon.onclick = function() {
//     document.body.classList.toggle("dark-theme");
//     if (document.body.classList.contains("dark-theme")) {
//         icon.className = "bx bx-sun";
//     } else {
//         icon.className = "uil uil-moon";

//     }
// }


// CHAT

// class Chatbox {
//     constructor() {
//         this.args = {
//             openButton: document.querySelector('.chatbox__button'),
//             chatBox: document.querySelector('.chatbox__support'),
//             sendButton: document.querySelector('.send__button')
//         }

//         this.state = false;
//         this.messages = [];
//     }

//     display() {
//         const { openButton, chatBox, sendButton } = this.args;

//         openButton.addEventListener('click', () => this.toggleState(chatBox))

//         sendButton.addEventListener('click', () => this.onSendButton(chatBox))

//         const node = chatBox.querySelector('input');
//         node.addEventListener("keyup", ({ key }) => {
//             if (key === "Enter") {
//                 this.onSendButton(chatBox)
//             }
//         })
//     }

//     toggleState(chatbox) {
//         this.state = !this.state;

//         // show or hides the box
//         if (this.state) {
//             chatbox.classList.add('chatbox--active')
//         } else {
//             chatbox.classList.remove('chatbox--active')
//         }
//     }

//     onSendButton(chatbox) {
//         var textField = chatbox.querySelector('input');
//         let text1 = textField.value
//         if (text1 === "") {
//             return;
//         }

//         let msg1 = { name: "User", message: text1 }
//         this.messages.push(msg1);

//         fetch('http://127.0.0.1:5000/predict', {
//                 method: 'POST',
//                 body: JSON.stringify({ message: text1 }),
//                 mode: 'cors',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//             })
//             .then(r => r.json())
//             .then(r => {
//                 let msg2 = { name: "Sam", message: r.answer };
//                 this.messages.push(msg2);
//                 this.updateChatText(chatbox)
//                 textField.value = ''

//             }).catch((error) => {
//                 console.error('Error:', error);
//                 this.updateChatText(chatbox)
//                 textField.value = ''
//             });
//     }

//     updateChatText(chatbox) {
//         var html = '';
//         this.messages.slice().reverse().forEach(function(item, index) {
//             if (item.name === "Sam") {
//                 html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
//             } else {
//                 html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
//             }
//         });

//         const chatmessage = chatbox.querySelector('.chatbox__messages');
//         chatmessage.innerHTML = html;
//     }
// }


// const chatbox = new Chatbox();
// chatbox.display();