document.querySelectorAll('button[data-notify="true"]').forEach( elem => {
    elem.addEventListener("click", () => {markReadNotification(elem) });
});


async function markReadNotification(elem) {
    const slug = elem.parentNode.getAttribute("data-slug");
    const isUnread = elem.parentNode.getAttribute("data-is-unread") === 'True';
    const redirect = elem.getAttribute("data-link");
    console.log(isUnread);

    if(isUnread) {
        const url = `/inbox/notifications/mark-as-read/${slug}/`;
            await fetch(url).then().catch(console.log);
    }
    
    window.location.href = elem.getAttribute("data-link");

    if(window.location.pathname === redirect.split("#")[0]) {
        window.location.reload();
    }
}

async function deleteNotification(elem) {
    const slug = elem.parentNode.getAttribute("data-slug");
    const url = `/inbox/notifications/delete/${slug}/`;

    await fetch(url).then().catch(console.log);
    elem.parentNode.remove();
}