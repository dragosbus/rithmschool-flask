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
        //mantain the default behavior for index page
        if (e.target.href.indexOf('index') < 0) {
            e.preventDefault();

            let htmlText = '';
            fetchPage(e.target.href).then(res => {
                let fromIndex = res.indexOf('<main>');
                let toIndex = res.indexOf('</main>');
                htmlText = res.substring(fromIndex, toIndex);
            }).then(() => {
                let modal = createModal(htmlText);
                document.body.appendChild(modal);
                closeModal();
            });
        }
    }
});

function closeModal() {
    //remove the overlay
    document.querySelector('.close-modal').addEventListener('click', e => {
        document.body.removeChild(document.querySelector('.overlay'));
    });
}