let url = window.location.href;

function fetchPage(url) {
    return fetch(url).then(res => res.text());
}

function createModal(page) {
    let overlay = document.createElement('div');
    overlay.className = 'overlay';

    let modal = document.createElement('div');
    modal.className = 'modal';
    modal.innerHTML = page;

    let closeModal = document.createElement('button');
    closeModal.textContent = 'X';
    closeModal.className = 'close-modal';

    overlay.appendChild(modal);
    overlay.appendChild(closeModal);

    return overlay;
}

document.querySelector('.navigation').addEventListener('click', e => {
    if (e.target.tagName === 'A') {
        e.preventDefault();
        let page = e.target.href;
        let htmlText = '';
        fetchPage(page).then(res => {
            let fromIndex = res.indexOf('<main>');
            let toIndex = res.indexOf('</main>');
            htmlText = res.substring(fromIndex, toIndex);
        }).then(() => {
            let modal = createModal(htmlText);
            document.body.appendChild(modal);
            closeModal();
        });
    }
});

function closeModal() {
    //close the overlay
    document.querySelector('.close-modal').addEventListener('click', e => {
        document.body.removeChild(document.querySelector('.overlay'));
    });
}