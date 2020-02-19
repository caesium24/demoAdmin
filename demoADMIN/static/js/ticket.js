/* Global Variables */
const ticket = document.querySelector('.ticket');
const adminText = document.querySelector('.ticket-admin');
const dateText = document.querySelector('.ticket-date');
const descText = document.querySelector('.ticket-desc');

/* Event Listeners */
loadEventListeners();

function loadEventListeners() {
    ticket.addEventListener("click", showTicket);
}
/* Event Listeners */

/* Ticket expansion */
function showTicket(e) {
    if (ticket.style.height == "50px") {
        ticket.style.height = "200px";
        ticket.style.overflowY = "scroll";
        adminText.style.display = "inline-block";
        dateText.style.display = "inline-block";
        descText.style.display = "inline-block";
    } else {
        ticket.style.height = "50px";
        ticket.style.overflow = "hidden";
        adminText.style.display = "none";
        dateText.style.display = "none";
        descText.style.display = "none";
    }
}
/* Ticket expansion */