/* Global Variables */
const menuCol = document.querySelector("#col-button");
const menuRet = document.querySelector("#ret-button");
const menuRetDiv = document.querySelector(".menu-return")
const menu = document.querySelector('.section-menu');
const conSec = document.querySelector('.content-section');
const dashLink = document.getElementById('dash-link');
const metricsLink = document.getElementById('metrics-link');
const alertsLink = document.getElementById('alerts-link');
const ticketsLink = document.getElementById('tickets-link');
const site01Link = document.getElementById('site01-link');
const site02Link = document.getElementById('site02-link');
const site03Link = document.getElementById('site03-link');
const site04Link = document.getElementById('site04-link');
const site05Link = document.getElementById('site05-link');
const site06Link = document.getElementById('site06-link');

/* Global Variables */

/* Event Listeners */
loadEventListeners();

function loadEventListeners() {
    menuRet.addEventListener("click", menuOpen);
    menuCol.addEventListener("click", menuClose);
}
/* Event Listeners */

/* Active menu border*/
function activeMenuLink(e) {
    if (conSec.classList[1] === 'dash-page') {
        dashLink.setAttribute("style", "border-color: #258afe;");
    }
    if (conSec.classList[1] === 'metrics-page') {
        metricsLink.setAttribute("style", "border-color: #258afe;");
    }
    if (conSec.classList[1] === 'alerts-page') {
        alertsLink.setAttribute("style", "border-color: #258afe;");
    }
    if (conSec.classList[1] === 'tickets-page') {
        ticketsLink.setAttribute("style", "border-color: #258afe;");
    }

}
/* Active menu border*/

/* Active site border*/
function activenavLink(e) {
    if (conSec.classList[2] === 'site01') {
        site01Link.setAttribute("style", "border-color: #258afe;");
    }
    if (conSec.classList[2] === 'site02') {
        site02Link.setAttribute("style", "border-color: #258afe;");
    }
    if (conSec.classList[2] === 'site03') {
        site03Link.setAttribute("style", "border-color: #258afe;");
    }
    if (conSec.classList[2] === 'site04') {
        site04Link.setAttribute("style", "border-color: #258afe;");
    }
    if (conSec.classList[2] === 'site05') {
        site05Link.setAttribute("style", "border-color: #258afe;");
    }
    if (conSec.classList[2] === 'site06') {
        site06Link.setAttribute("style", "border-color: #258afe;");
    }

}
/* Active site border*/

/* Menu open/close functionality */
function menuClose(e) {
    if (menu.style.display === "flex") {
        menu.style.display = "none";
        menuRetDiv.style.display = "flex";
    }
}

function menuOpen(e) {
    if (menu.style.display === "none") {
        menuRetDiv.style.display = "none";
        menu.style.display = "flex";
    }
}
/* Menu functionality */

function displayTime() {
    var localTime;

    if (conSec.classList[2] === 'site01') {
        var tzOffset = -6;
    }
    if (conSec.classList[2] === 'site02') {
        var tzOffset = -10;
    }
    if (conSec.classList[2] === 'site03') {
        var tzOffset = +9;
    }
    if (conSec.classList[2] === 'site04') {
        var tzOffset = -5;
    }
    if (conSec.classList[2] === 'site05') {
        var tzOffset = +1;
    }
    if (conSec.classList[2] === 'site06') {
        var tzOffset = +3;
    }
    var tzOffSet = tzOffset;
    var d = new Date();
    var dx = d.toGMTString();
    dx = dx.substr(0, dx.length - 3);
    d.setTime(Date.parse(dx));
    d.setHours(d.getHours() + tzOffset);
    var nhour = d.getHours(),
        nmin = d.getMinutes(),
        nsec = d.getSeconds();
    if (nmin <= 9) nmin = "0" + nmin;
    if (nsec <= 9) nsec = "0" + nsec;

    const clocktext = "" + nhour + ":" + nmin + ":" + nsec + "";
    document.getElementById('local-time').innerHTML = clocktext;
}

displayTime();
setInterval(displayTime, 1000);
activeMenuLink();
activenavLink();